import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np



# Dados do Provedor Local
dados_local = [
    {"rodada": 1, "data_hora": "2025-12-12 15:13:52", "servidor": "184.72.203.204", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 2.16}, "rede": {"ping_ms": 105.851, "ttl": 47, "download": {"mbps": 81.65, "retransmits": 602, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.36, "retransmits": 2469, "jitter": 112.161, "erro": False}}},
    {"rodada": 2, "data_hora": "2025-12-12 15:15:20", "servidor": "184.72.203.204", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.63}, "rede": {"ping_ms": 105.934, "ttl": 47, "download": {"mbps": 92.76, "retransmits": 1322, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.25, "retransmits": 2500, "jitter": 111.71, "erro": False}}},
    {"rodada": 3, "data_hora": "2025-12-12 15:16:49", "servidor": "184.72.203.204", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 6.89}, "rede": {"ping_ms": 106.023, "ttl": 47, "download": {"mbps": 80.29, "retransmits": 1362, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.26, "retransmits": 2258, "jitter": 113.369, "erro": False}}},
    {"rodada": 4, "data_hora": "2025-12-12 15:18:18", "servidor": "184.72.203.204", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.77}, "rede": {"ping_ms": 106.005, "ttl": 47, "download": {"mbps": 92.13, "retransmits": 1598, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.32, "retransmits": 2428, "jitter": 111.702, "erro": False}}},
    {"rodada": 5, "data_hora": "2025-12-12 15:19:46", "servidor": "184.72.203.204", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.71}, "rede": {"ping_ms": 105.545, "ttl": 47, "download": {"mbps": 73.36, "retransmits": 762, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.22, "retransmits": 2865, "jitter": 111.617, "erro": False}}},
    {"rodada": 6, "data_hora": "2025-12-12 15:21:15", "servidor": "184.72.203.204", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.73}, "rede": {"ping_ms": 105.999, "ttl": 47, "download": {"mbps": 85.98, "retransmits": 1449, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.25, "retransmits": 2143, "jitter": 112.018, "erro": False}}},
    {"rodada": 7, "data_hora": "2025-12-12 15:22:43", "servidor": "184.72.203.204", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 6.46}, "rede": {"ping_ms": 105.586, "ttl": 47, "download": {"mbps": 82.59, "retransmits": 910, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.29, "retransmits": 2550, "jitter": 112.636, "erro": False}}},
    {"rodada": 8, "data_hora": "2025-12-12 15:24:12", "servidor": "184.72.203.204", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.44}, "rede": {"ping_ms": 105.809, "ttl": 47, "download": {"mbps": 81.4, "retransmits": 790, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.22, "retransmits": 2814, "jitter": 111.436, "erro": False}}},
    {"rodada": 9, "data_hora": "2025-12-12 15:25:40", "servidor": "184.72.203.204", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.55}, "rede": {"ping_ms": 105.669, "ttl": 47, "download": {"mbps": 92.76, "retransmits": 793, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.36, "retransmits": 1989, "jitter": 112.709, "erro": False}}},
    {"rodada": 10, "data_hora": "2025-12-12 15:27:09", "servidor": "184.72.203.204", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 7.02}, "rede": {"ping_ms": 105.704, "ttl": 47, "download": {"mbps": 92.13, "retransmits": 1344, "jitter": 0.0, "erro": False}, "upload": {"mbps": 27.02, "retransmits": 2601, "jitter": 110.84, "erro": False}}}
]

# Dados da RNP 
dados_rnp = [
    {"rodada": 1, "data_hora": "2025-12-12 14:26:59", "servidor": "3.93.68.15", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 2.61}, "rede": {"ping_ms": 110.939, "ttl": 56, "download": {"mbps": 32.19, "retransmits": 1097, "jitter": 0.0, "erro": False}, "upload": {"mbps": 92.68, "retransmits": 0, "jitter": 132.474, "erro": False}}},
    {"rodada": 2, "data_hora": "2025-12-12 14:28:27", "servidor": "3.93.68.15", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 74.58}, "rede": {"ping_ms": 111.904, "ttl": 55, "download": {"mbps": 39.95, "retransmits": 388, "jitter": 0.0, "erro": False}, "upload": {"mbps": 92.73, "retransmits": 0, "jitter": 124.596, "erro": False}}},
    {"rodada": 3, "data_hora": "2025-12-12 14:29:56", "servidor": "3.93.68.15", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.6}, "rede": {"ping_ms": 111.775, "ttl": 55, "download": {"mbps": 34.15, "retransmits": 453, "jitter": 0.0, "erro": False}, "upload": {"mbps": 92.74, "retransmits": 0, "jitter": 122.756, "erro": False}}},
    {"rodada": 4, "data_hora": "2025-12-12 14:31:25", "servidor": "3.93.68.15", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.63}, "rede": {"ping_ms": 112.512, "ttl": 55, "download": {"mbps": 33.59, "retransmits": 362, "jitter": 0.0, "erro": False}, "upload": {"mbps": 92.7, "retransmits": 0, "jitter": 130.121, "erro": False}}},
    {"rodada": 5, "data_hora": "2025-12-12 14:32:54", "servidor": "3.93.68.15", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.59}, "rede": {"ping_ms": 111.599, "ttl": 55, "download": {"mbps": 33.76, "retransmits": 341, "jitter": 0.0, "erro": False}, "upload": {"mbps": 92.73, "retransmits": 0, "jitter": 130.226, "erro": False}}},
    {"rodada": 6, "data_hora": "2025-12-12 14:34:23", "servidor": "3.93.68.15", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 72.33}, "rede": {"ping_ms": 111.42, "ttl": 56, "download": {"mbps": 39.04, "retransmits": 337, "jitter": 0.0, "erro": False}, "upload": {"mbps": 92.74, "retransmits": 0, "jitter": 129.453, "erro": False}}},
    {"rodada": 7, "data_hora": "2025-12-12 14:35:51", "servidor": "3.93.68.15", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.61}, "rede": {"ping_ms": 111.843, "ttl": 55, "download": {"mbps": 32.33, "retransmits": 359, "jitter": 0.0, "erro": False}, "upload": {"mbps": 92.76, "retransmits": 0, "jitter": 125.51, "erro": False}}},
    {"rodada": 8, "data_hora": "2025-12-12 14:37:20", "servidor": "3.93.68.15", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.66}, "rede": {"ping_ms": 111.431, "ttl": 55, "download": {"mbps": 42.57, "retransmits": 439, "jitter": 0.0, "erro": False}, "upload": {"mbps": 92.73, "retransmits": 0, "jitter": 132.684, "erro": False}}},
    {"rodada": 9, "data_hora": "2025-12-12 14:38:49", "servidor": "3.93.68.15", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 72.68}, "rede": {"ping_ms": 111.88, "ttl": 55, "download": {"mbps": 38.76, "retransmits": 394, "jitter": 0.0, "erro": False}, "upload": {"mbps": 92.76, "retransmits": 0, "jitter": 131.467, "erro": False}}},
    {"rodada": 10, "data_hora": "2025-12-12 14:40:18", "servidor": "3.93.68.15", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.52}, "rede": {"ping_ms": 111.475, "ttl": 56, "download": {"mbps": 39.81, "retransmits": 340, "jitter": 0.0, "erro": False}, "upload": {"mbps": 92.67, "retransmits": 0, "jitter": 130.72, "erro": False}}}
]

# ==============================================================================
# 2. PROCESSAMENTO
# ==============================================================================
df_local = pd.json_normalize(dados_local)
df_local['Provedor'] = 'Local'

df_rnp = pd.json_normalize(dados_rnp)
df_rnp['Provedor'] = 'RNP'

df_final = pd.concat([df_local, df_rnp], ignore_index=True)

# ==============================================================================
# 3. GERAÇÃO DOS GRÁFICOS
# ==============================================================================
sns.set_style("whitegrid")
cores = {"Local": "#1f77b4", "RNP": "#ff7f0e"}

fig, axs = plt.subplots(3, 2, figsize=(16, 15))
fig.suptitle('Comparativo de Desempenho Escola Municipal Severina Ernestina Abigail: Local vs RNP', fontsize=20, weight='bold')

# 1. Download
sns.lineplot(data=df_final, x='rodada', y='rede.download.mbps', hue='Provedor',
             marker='o', palette=cores, ax=axs[0, 0], linewidth=2.5)
axs[0, 0].set_title('Velocidade de Download (Mbps)', fontsize=14)
axs[0, 0].set_ylabel('Mbps')
# Ajustar limite Y dinamicamente ou fixar com margem
max_y = df_final['rede.download.mbps'].max()
axs[0, 0].set_ylim(0, max_y * 1.1)

# 2. Upload
sns.lineplot(data=df_final, x='rodada', y='rede.upload.mbps', hue='Provedor',
             marker='o', palette=cores, ax=axs[0, 1], linewidth=2.5)
axs[0, 1].set_title('Velocidade de Upload (Mbps)', fontsize=14)
axs[0, 1].set_ylabel('Mbps')
axs[0, 1].set_ylim(0, 110)

# 3. Latência
sns.lineplot(data=df_final, x='rodada', y='rede.ping_ms', hue='Provedor',
             marker='s', palette=cores, ax=axs[1, 0], linewidth=2)
axs[1, 0].set_title('Latência / Ping (ms)', fontsize=14)
axs[1, 0].set_ylabel('Tempo (ms)')

# 4. Jitter Upload
sns.barplot(data=df_final, x='rodada', y='rede.upload.jitter', hue='Provedor',
            palette=cores, ax=axs[1, 1], alpha=0.9)
axs[1, 1].set_title('Jitter de Upload (ms) - Estabilidade', fontsize=14)
axs[1, 1].set_ylabel('Jitter (ms)')

# 5. Retransmissões
sns.barplot(data=df_final, x='rodada', y='rede.download.retransmits', hue='Provedor',
            palette=cores, ax=axs[2, 0], alpha=0.9)
axs[2, 0].set_title('Retransmissões no Download (Menor é melhor)', fontsize=14)
axs[2, 0].set_ylabel('Qtd. Pacotes Retransmitidos')

# 6. DNS
sns.lineplot(data=df_final, x='rodada', y='ambiente.tempo_dns_ms', hue='Provedor',
             marker='^', palette=cores, ax=axs[2, 1], linewidth=2)
axs[2, 1].set_title('Tempo de Resposta DNS (ms)', fontsize=14)
axs[2, 1].set_ylabel('Tempo (ms)')

for ax in axs.flat:
    ax.set_xlabel('Rodada de Teste')
    ax.legend(title='Provedor')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# ==============================================================================
# 4. RESUMO
# ==============================================================================
resumo = df_final.groupby('Provedor')[
    ['rede.download.mbps', 'rede.upload.mbps', 'rede.ping_ms',
     'rede.upload.jitter', 'rede.download.retransmits']
].mean().reset_index()

print("--- RESUMO DAS MÉDIAS ---")
print(resumo.to_string(index=False))
