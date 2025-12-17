import json
import pandas as pd 
import os

ARQUIVO_JSON = "dados_tcc_escolas_completo.json"
ARQUIVO_EXCEL = "tabela_final_tcc.xlsx"

if not os.path.exists(ARQUIVO_JSON):
    print("Arquivo JSON não encontrado!")
    exit()

with open(ARQUIVO_JSON, 'r') as f:
    dados = json.load(f)

# Transformando o JSON complexo em uma lista plana para o Excel
lista_plana = []

for rodada in dados:
    item = {
        "Rodada": rodada.get("rodada", "N/A"),
        "Data/Hora": rodada["data_hora"],
        # Ambiente
        "Sinal Wi-Fi (dBm)": rodada["ambiente"]["wifi_sinal_dbm"],
        "Link Wi-Fi (Mbps)": rodada["ambiente"]["wifi_link_negociado"],
        "DNS (ms)": rodada["ambiente"]["tempo_dns_ms"],
        # Rede - Ping
        "Ping Ocioso (ms)": rodada["rede"]["ping_ms"],
        "TTL": rodada["rede"]["ttl"],
        # Rede - Download
        "Download (Mbps)": rodada["rede"]["download"]["mbps"],
        "Down Jitter (ms)": rodada["rede"]["download"]["jitter"],
        "Down Perdas": rodada["rede"]["download"]["retransmits"],
        # Rede - Upload
        "Upload (Mbps)": rodada["rede"]["upload"]["mbps"],
        "Up Jitter (ms)": rodada["rede"]["upload"]["jitter"],
        "Up Perdas": rodada["rede"]["upload"]["retransmits"],
    }
    lista_plana.append(item)

# Criando o DataFrame e salvando
df = pd.DataFrame(lista_plana)

# Calculando Médias
medias = df.mean(numeric_only=True)
# Adiciona uma linha de média no final
# df.loc['Média'] = medias 

df.to_excel(ARQUIVO_EXCEL, index=False)

print(f"Sucesso! Tabela criada: {ARQUIVO_EXCEL}")
print("\n--- RESUMO RÁPIDO ---")
print(f"Média Download: {df['Download (Mbps)'].mean():.2f} Mbps")
print(f"Média Upload:   {df['Upload (Mbps)'].mean():.2f} Mbps")
print(f"Média Ping:     {df['Ping Ocioso (ms)'].mean():.2f} ms")
