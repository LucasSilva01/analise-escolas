import subprocess
import json
import os
import time
import re
import socket
from datetime import datetime

# --- CONFIGURAÇÕES DO ESTUDO ---
SERVER_IP = "184.72.203.204"  # Seu IP AWS
SERVER_PORT = "5201"
NUM_STREAMS = "10"
DURATION = "30"             # Duração de cada teste de banda
OUTPUT_FILE = "ernestina_abigail_meganet.json"

# --- CONFIGURAÇÃO DO LOOP ---
QTD_RODADAS = 10            # Quantas vezes vai repetir
INTERVALO_ENTRE_TESTES = 20 # Segundos de descanso entre as rodadas

def run_command(cmd_list):
    try:
        result = subprocess.run(cmd_list, capture_output=True, text=True, timeout=120)
        return result.stdout
    except:
        return None

def pegar_info_wifi():
    """Coleta dados do Wi-Fi (Sinal e Link Negociado)"""
    out = run_command(["iwconfig"])
    dados = {"rssi_dbm": None, "link_speed_mbps": None}
    if out:
        match_rssi = re.search(r'Signal level=(-\d+)', out)
        if match_rssi: dados["rssi_dbm"] = int(match_rssi.group(1))
        match_rate = re.search(r'Bit Rate[:=](\d+\.?\d+)', out)
        if match_rate: dados["link_speed_mbps"] = float(match_rate.group(1))
    return dados

def medir_tempo_dns():
    """Mede latência de resolução de nomes"""
    try:
        inicio = time.time()
        socket.gethostbyname("google.com")
        fim = time.time()
        return round((fim - inicio) * 1000, 2)
    except:
        return None

def medir_ping_e_ttl():
    """Mede Ping ICMP e TTL"""
    out = run_command(["ping", "-c", "4", SERVER_IP])
    dados = {"ping_medio": None, "ttl": None}
    if out:
        match_ping = re.search(r'(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+)', out)
        if match_ping: dados["ping_medio"] = float(match_ping.group(2))
        match_ttl = re.search(r'ttl=(\d+)', out, re.IGNORECASE)
        if match_ttl: dados["ttl"] = int(match_ttl.group(1))
    return dados

def rodar_iperf_json(modo_download=True):
    tipo = "DOWNLOAD" if modo_download else "UPLOAD"
    # Adicionei timestamp no print para saber se travou
    print(f"      [{datetime.now().strftime('%H:%M:%S')}] Testando {tipo}...")
    
    cmd = ["iperf3", "-c", SERVER_IP, "-p", SERVER_PORT, "-t", DURATION, "-P", NUM_STREAMS, "-J"]
    if modo_download: cmd.append("-R") 

    raw_json = run_command(cmd)
    
    # Se falhar, retorna dados zerados em vez de None, para não quebrar a tabela
    dados_vazios = {"mbps": 0, "retransmits": 0, "jitter": 0, "erro": True}

    if not raw_json or "error" in raw_json: 
        return dados_vazios

    try:
        dados = json.loads(raw_json)
        mbps = dados['end']['sum_received']['bits_per_second'] / 1_000_000
        retransmits = dados['end']['sum_sent']['retransmits']
        
        total_jitter, count = 0, 0
        for s in dados['end']['streams']:
            val = s['sender'].get('max_rtt', s['sender'].get('rttvar', 0))
            total_jitter += val
            count += 1
        jitter_ms = (total_jitter / count) / 1000 if count > 0 else 0

        return {"mbps": round(mbps, 2), "retransmits": retransmits, "jitter": round(jitter_ms, 3), "erro": False}
    except: 
        return dados_vazios

def salvar_rodada(rodada_atual, ping_data, dns_ms, wifi_data, down, up):
    print(f"      -> Salvando dados da rodada {rodada_atual}...")
    
    registro = {
        "rodada": rodada_atual,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "servidor": SERVER_IP,
        "ambiente": {
            "wifi_sinal_dbm": wifi_data["rssi_dbm"],
            "wifi_link_negociado": wifi_data["link_speed_mbps"],
            "tempo_dns_ms": dns_ms
        },
        "rede": {
            "ping_ms": ping_data["ping_medio"],
            "ttl": ping_data["ttl"],
            "download": down,
            "upload": up
        }
    }

    lista = []
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r') as f: lista = json.load(f)
        except: pass
    
    lista.append(registro)
    
    # Salva imediatamente para não perder dados se acabar a bateria
    with open(OUTPUT_FILE, 'w') as f: json.dump(lista, f, indent=4)
        
    print(f"      [OK] Rodada {rodada_atual} salva com sucesso.")

# loop
if __name__ == "__main__":
    print(f"\n{'='*50}")
    print(f" INICIANDO COLETA DE DADOS PARA O TCC")
    print(f" Alvo: {SERVER_IP}")
    print(f" Total de Rodadas: {QTD_RODADAS}")
    print(f" Intervalo entre rodadas: {INTERVALO_ENTRE_TESTES}s")
    print(f" Arquivo de saída: {OUTPUT_FILE}")
    print(f"{'='*50}\n")

    for i in range(1, QTD_RODADAS + 1):
        print(f"\n>>> INICIANDO RODADA {i} de {QTD_RODADAS} <<<")
        
        # 1. Coleta Métricas Rápidas
        dados_icmp = medir_ping_e_ttl()
        tempo_dns = medir_tempo_dns()
        dados_wifi = pegar_info_wifi()
        
        # 2. Coleta Banda
        res_down = rodar_iperf_json(True)
        time.sleep(2) # Pequena pausa para virar a chave
        res_up = rodar_iperf_json(False)
        
        # 3. Salva
        salvar_rodada(i, dados_icmp, tempo_dns, dados_wifi, res_down, res_up)
        
        # 4. Intervalo (Apenas se não for a última rodada)
        if i < QTD_RODADAS:
            print(f"--- Aguardando {INTERVALO_ENTRE_TESTES} segundos para a próxima rodada ---")
            for s in range(INTERVALO_ENTRE_TESTES, 0, -1):
                print(f"{s}...", end="\r") # Contagem regressiva na mesma linha
                time.sleep(1)
            print(" " * 10 + "\r", end="") # Limpa a linha
            
    print(f"\n\n{'='*50}")
    print(f" COLETA FINALIZADA!")
    print(f" Todos os dados foram salvos em: {os.path.abspath(OUTPUT_FILE)}")
    print(f"{'='*50}")
