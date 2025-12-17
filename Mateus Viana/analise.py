import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# ==============================================================================
# 1. CARREGAMENTO DOS DADOS
# ==============================================================================

# Dados do Provedor Local
dados_local = [
    {"rodada": 1, "data_hora": "2025-12-11 10:02:49", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 4.87}, "rede": {"ping_ms": 109.864, "ttl": 46, "download": {"mbps": 96.19, "retransmits": 6920, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.15, "retransmits": 1037, "jitter": 114.183, "erro": False}}},
    {"rodada": 2, "data_hora": "2025-12-11 10:04:18", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.51}, "rede": {"ping_ms": 109.965, "ttl": 46, "download": {"mbps": 95.1, "retransmits": 6624, "jitter": 0.0, "erro": False}, "upload": {"mbps": 28.73, "retransmits": 1118, "jitter": 115.053, "erro": False}}},
    {"rodada": 3, "data_hora": "2025-12-11 10:05:47", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.78}, "rede": {"ping_ms": 110.129, "ttl": 46, "download": {"mbps": 95.45, "retransmits": 4597, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.18, "retransmits": 1232, "jitter": 115.124, "erro": False}}},
    {"rodada": 4, "data_hora": "2025-12-11 10:07:16", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 3.13}, "rede": {"ping_ms": 110.351, "ttl": 46, "download": {"mbps": 93.95, "retransmits": 8767, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.18, "retransmits": 1315, "jitter": 113.945, "erro": False}}},
    {"rodada": 5, "data_hora": "2025-12-11 10:08:44", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.58}, "rede": {"ping_ms": 110.479, "ttl": 46, "download": {"mbps": 91.47, "retransmits": 9076, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.11, "retransmits": 2258, "jitter": 115.155, "erro": False}}},
    {"rodada": 6, "data_hora": "2025-12-11 10:10:13", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.61}, "rede": {"ping_ms": 109.691, "ttl": 46, "download": {"mbps": 94.96, "retransmits": 11577, "jitter": 0.0, "erro": False}, "upload": {"mbps": 28.87, "retransmits": 998, "jitter": 114.944, "erro": False}}},
    {"rodada": 7, "data_hora": "2025-12-11 10:11:42", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 1.87}, "rede": {"ping_ms": 109.823, "ttl": 46, "download": {"mbps": 93.43, "retransmits": 6012, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.08, "retransmits": 2217, "jitter": 117.456, "erro": False}}},
    {"rodada": 8, "data_hora": "2025-12-11 10:13:10", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.61}, "rede": {"ping_ms": 109.985, "ttl": 46, "download": {"mbps": 89.06, "retransmits": 8499, "jitter": 0.0, "erro": False}, "upload": {"mbps": 28.69, "retransmits": 950, "jitter": 115.141, "erro": False}}},
    {"rodada": 9, "data_hora": "2025-12-11 10:14:39", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.52}, "rede": {"ping_ms": 110.068, "ttl": 46, "download": {"mbps": 96.29, "retransmits": 6421, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.01, "retransmits": 2161, "jitter": 115.564, "erro": False}}},
    {"rodada": 10, "data_hora": "2025-12-11 10:16:08", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 19.81}, "rede": {"ping_ms": 110.467, "ttl": 46, "download": {"mbps": 95.98, "retransmits": 7179, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.15, "retransmits": 2262, "jitter": 115.981, "erro": False}}}
]

# Dados da RNP
dados_rnp = [
    {"rodada": 1, "data_hora": "2025-12-11 10:20:36", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 2.53}, "rede": {"ping_ms": 114.047, "ttl": 55, "download": {"mbps": 85.66, "retransmits": 1885, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.7, "retransmits": 330, "jitter": 414.216, "erro": False}}},
    {"rodada": 2, "data_hora": "2025-12-11 10:22:05", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 2.41}, "rede": {"ping_ms": 111.693, "ttl": 55, "download": {"mbps": 91.43, "retransmits": 1941, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.6, "retransmits": 349, "jitter": 415.561, "erro": False}}},
    {"rodada": 3, "data_hora": "2025-12-11 10:23:35", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.71}, "rede": {"ping_ms": 112.099, "ttl": 56, "download": {"mbps": 89.86, "retransmits": 1890, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.54, "retransmits": 383, "jitter": 413.776, "erro": False}}},
    {"rodada": 4, "data_hora": "2025-12-11 10:25:04", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.77}, "rede": {"ping_ms": 111.154, "ttl": 56, "download": {"mbps": 75.88, "retransmits": 1698, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.78, "retransmits": 369, "jitter": 415.38, "erro": False}}},
    {"rodada": 5, "data_hora": "2025-12-11 10:26:33", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 73.75}, "rede": {"ping_ms": 111.539, "ttl": 56, "download": {"mbps": 89.9, "retransmits": 1735, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.7, "retransmits": 405, "jitter": 415.046, "erro": False}}},
    {"rodada": 6, "data_hora": "2025-12-11 10:28:03", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.43}, "rede": {"ping_ms": 111.565, "ttl": 55, "download": {"mbps": 85.49, "retransmits": 1986, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.75, "retransmits": 392, "jitter": 417.491, "erro": False}}},
    {"rodada": 7, "data_hora": "2025-12-11 10:29:32", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.57}, "rede": {"ping_ms": 111.32, "ttl": 56, "download": {"mbps": 92.62, "retransmits": 2115, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.73, "retransmits": 411, "jitter": 416.898, "erro": False}}},
    {"rodada": 8, "data_hora": "2025-12-11 10:31:01", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.4}, "rede": {"ping_ms": 111.497, "ttl": 55, "download": {"mbps": 90.31, "retransmits": 1843, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.63, "retransmits": 338, "jitter": 415.017, "erro": False}}},
    {"rodada": 9, "data_hora": "2025-12-11 10:32:31", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 73.05}, "rede": {"ping_ms": 111.314, "ttl": 55, "download": {"mbps": 86.3, "retransmits": 1821, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.75, "retransmits": 369, "jitter": 415.631, "erro": False}}},
    {"rodada": 10, "data_hora": "2025-12-11 10:34:00", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.62}, "rede": {"ping_ms": 111.715, "ttl": 56, "download": {"mbps": 87.41, "retransmits": 2458, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.71, "retransmits": 421, "jitter": 415.717, "erro": False}}}
]

# ==============================================================================
# 2. PROCESSAMENTO E NORMALIZAÇÃO
# ==============================================================================

# Normaliza os JSONs para DataFrames planos (flat)
df_local = pd.json_normalize(dados_local)
df_local['Provedor'] = 'Local'

df_rnp = pd.json_normalize(dados_rnp)
df_rnp['Provedor'] = 'RNP'

# Combina os dados
df_final = pd.concat([df_local, df_rnp], ignore_index=True)

# ==============================================================================
# 3. GERAÇÃO DOS GRÁFICOS
# ==============================================================================

# Configuração de Estilo
sns.set_style("whitegrid")
# Paleta de cores: Azul para Local, Laranja para RNP (cores de alto contraste)
cores = {"Local": "#1f77b4", "RNP": "#ff7f0e"}

# Cria uma figura com 6 subplots (3 linhas, 2 colunas)
fig, axs = plt.subplots(3, 2, figsize=(16, 15))
fig.suptitle('Comparativo de Desempenho: Provedor Local vs RNP', fontsize=20, weight='bold')

# --- GRÁFICO 1: Velocidade de Download ---
sns.lineplot(data=df_final, x='rodada', y='rede.download.mbps', hue='Provedor', 
             marker='o', palette=cores, ax=axs[0, 0], linewidth=2.5)
axs[0, 0].set_title('Velocidade de Download (Mbps)', fontsize=14)
axs[0, 0].set_ylabel('Mbps')
axs[0, 0].set_ylim(0, 110) # Ajustado para margem

# --- GRÁFICO 2: Velocidade de Upload ---
sns.lineplot(data=df_final, x='rodada', y='rede.upload.mbps', hue='Provedor', 
             marker='o', palette=cores, ax=axs[0, 1], linewidth=2.5)
axs[0, 1].set_title('Velocidade de Upload (Mbps)', fontsize=14)
axs[0, 1].set_ylabel('Mbps')
axs[0, 1].set_ylim(0, 110)

# --- GRÁFICO 3: Latência (Ping) ---
sns.lineplot(data=df_final, x='rodada', y='rede.ping_ms', hue='Provedor', 
             marker='s', palette=cores, ax=axs[1, 0], linewidth=2)
axs[1, 0].set_title('Latência / Ping (ms)', fontsize=14)
axs[1, 0].set_ylabel('Tempo (ms)')
# Nota: O ping é próximo, então não fixamos o zero para ver a variação sutil

# --- GRÁFICO 4: Jitter de Upload (Variação da Latência) ---
# Usando Barplot pois a diferença é muito grande e estática
sns.barplot(data=df_final, x='rodada', y='rede.upload.jitter', hue='Provedor', 
            palette=cores, ax=axs[1, 1], alpha=0.9)
axs[1, 1].set_title('Jitter de Upload (ms) - Estabilidade', fontsize=14)
axs[1, 1].set_ylabel('Jitter (ms)')

# --- GRÁFICO 5: Retransmissões de Download (Qualidade do Link) ---
sns.barplot(data=df_final, x='rodada', y='rede.download.retransmits', hue='Provedor', 
            palette=cores, ax=axs[2, 0], alpha=0.9)
axs[2, 0].set_title('Retransmissões no Download (Menor é melhor)', fontsize=14)
axs[2, 0].set_ylabel('Qtd. Pacotes Retransmitidos')

# --- GRÁFICO 6: Tempo de Resposta DNS ---
sns.lineplot(data=df_final, x='rodada', y='ambiente.tempo_dns_ms', hue='Provedor', 
             marker='^', palette=cores, ax=axs[2, 1], linewidth=2)
axs[2, 1].set_title('Tempo de Resposta DNS (ms)', fontsize=14)
axs[2, 1].set_ylabel('Tempo (ms)')

# Ajustes Finais de Layout
for ax in axs.flat:
    ax.set_xlabel('Rodada de Teste')
    ax.legend(title='Provedor')

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Ajusta para o título principal não cortar
plt.show()

# ==============================================================================
# 4. TABELA RESUMO (Opcional - Imprime médias no console)
# ==============================================================================
resumo = df_final.groupby('Provedor')[
    ['rede.download.mbps', 'rede.upload.mbps', 'rede.ping_ms', 
     'rede.upload.jitter', 'rede.download.retransmits']
].mean().reset_index()

print("\n--- RESUMO DAS MÉDIAS ---")
print(resumo.to_string(index=False))