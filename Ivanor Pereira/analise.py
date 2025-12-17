import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np



# Dados do Provedor Local
dados_local = [
    {"rodada": 1, "data_hora": "2025-12-11 10:48:49", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 6.1}, "rede": {"ping_ms": 110.158, "ttl": 46, "download": {"mbps": 96.08, "retransmits": 7856, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.1, "retransmits": 962, "jitter": 115.481, "erro": False}}},
    {"rodada": 2, "data_hora": "2025-12-11 10:50:18", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.45}, "rede": {"ping_ms": 109.52, "ttl": 46, "download": {"mbps": 96.18, "retransmits": 4916, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.29, "retransmits": 1477, "jitter": 115.501, "erro": False}}},
    {"rodada": 3, "data_hora": "2025-12-11 10:51:46", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 3.4}, "rede": {"ping_ms": 109.818, "ttl": 46, "download": {"mbps": 96.54, "retransmits": 5454, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.26, "retransmits": 2339, "jitter": 115.514, "erro": False}}},
    {"rodada": 4, "data_hora": "2025-12-11 10:53:15", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.84}, "rede": {"ping_ms": 110.18, "ttl": 46, "download": {"mbps": 95.21, "retransmits": 5452, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.13, "retransmits": 961, "jitter": 114.355, "erro": False}}},
    {"rodada": 5, "data_hora": "2025-12-11 10:54:44", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.75}, "rede": {"ping_ms": 110.014, "ttl": 46, "download": {"mbps": 95.73, "retransmits": 6325, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.2, "retransmits": 1863, "jitter": 115.081, "erro": False}}},
    {"rodada": 6, "data_hora": "2025-12-11 10:56:12", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 3.82}, "rede": {"ping_ms": 109.899, "ttl": 46, "download": {"mbps": 94.37, "retransmits": 7158, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.2, "retransmits": 1665, "jitter": 115.6, "erro": False}}},
    {"rodada": 7, "data_hora": "2025-12-11 10:57:41", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.47}, "rede": {"ping_ms": 110.021, "ttl": 46, "download": {"mbps": 88.57, "retransmits": 8002, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.1, "retransmits": 973, "jitter": 117.04, "erro": False}}},
    {"rodada": 8, "data_hora": "2025-12-11 10:59:10", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.58}, "rede": {"ping_ms": 110.402, "ttl": 46, "download": {"mbps": 94.48, "retransmits": 7705, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.14, "retransmits": 2252, "jitter": 115.612, "erro": False}}},
    {"rodada": 9, "data_hora": "2025-12-11 11:00:38", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 3.02}, "rede": {"ping_ms": 110.268, "ttl": 46, "download": {"mbps": 94.79, "retransmits": 5409, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.15, "retransmits": 2136, "jitter": 127.865, "erro": False}}},
    {"rodada": 10, "data_hora": "2025-12-11 11:02:07", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.53}, "rede": {"ping_ms": 110.013, "ttl": 46, "download": {"mbps": 93.42, "retransmits": 6266, "jitter": 0.0, "erro": False}, "upload": {"mbps": 29.04, "retransmits": 992, "jitter": 115.324, "erro": False}}}
]

# Dados da RNP
dados_rnp = [
    {"rodada": 1, "data_hora": "2025-12-11 11:07:26", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 4.82}, "rede": {"ping_ms": 111.545, "ttl": 55, "download": {"mbps": 91.89, "retransmits": 1627, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.79, "retransmits": 376, "jitter": 416.702, "erro": False}}},
    {"rodada": 2, "data_hora": "2025-12-11 11:08:55", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.55}, "rede": {"ping_ms": 111.626, "ttl": 56, "download": {"mbps": 92.38, "retransmits": 1934, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.74, "retransmits": 368, "jitter": 416.08, "erro": False}}},
    {"rodada": 3, "data_hora": "2025-12-11 11:10:25", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.53}, "rede": {"ping_ms": 111.318, "ttl": 55, "download": {"mbps": 85.35, "retransmits": 1898, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.7, "retransmits": 388, "jitter": 416.229, "erro": False}}},
    {"rodada": 4, "data_hora": "2025-12-11 11:11:54", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 73.48}, "rede": {"ping_ms": 111.506, "ttl": 56, "download": {"mbps": 92.52, "retransmits": 1906, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.77, "retransmits": 404, "jitter": 416.066, "erro": False}}},
    {"rodada": 5, "data_hora": "2025-12-11 11:13:23", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.86}, "rede": {"ping_ms": 111.581, "ttl": 55, "download": {"mbps": 93.88, "retransmits": 1371, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.73, "retransmits": 377, "jitter": 416.24, "erro": False}}},
    {"rodada": 6, "data_hora": "2025-12-11 11:14:53", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.56}, "rede": {"ping_ms": 111.469, "ttl": 56, "download": {"mbps": 91.64, "retransmits": 1886, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.75, "retransmits": 401, "jitter": 416.721, "erro": False}}},
    {"rodada": 7, "data_hora": "2025-12-11 11:16:22", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 74.14}, "rede": {"ping_ms": 111.721, "ttl": 56, "download": {"mbps": 88.18, "retransmits": 2449, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.8, "retransmits": 362, "jitter": 415.929, "erro": False}}},
    {"rodada": 8, "data_hora": "2025-12-11 11:17:51", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.47}, "rede": {"ping_ms": 111.34, "ttl": 56, "download": {"mbps": 88.74, "retransmits": 2120, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.74, "retransmits": 390, "jitter": 416.028, "erro": False}}},
    {"rodada": 9, "data_hora": "2025-12-11 11:19:20", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.67}, "rede": {"ping_ms": 112.239, "ttl": 56, "download": {"mbps": 93.36, "retransmits": 6241, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.84, "retransmits": 391, "jitter": 415.875, "erro": False}}},
    {"rodada": 10, "data_hora": "2025-12-11 11:20:50", "servidor": "98.84.132.182", "ambiente": {"wifi_sinal_dbm": None, "wifi_link_negociado": None, "tempo_dns_ms": 0.56}, "rede": {"ping_ms": 111.754, "ttl": 56, "download": {"mbps": 89.86, "retransmits": 1444, "jitter": 0.0, "erro": False}, "upload": {"mbps": 94.79, "retransmits": 425, "jitter": 416.407, "erro": False}}}
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
fig.suptitle('Comparativo de Desempenho Escola Municipal Ivanor Pereira: Local vs RNP', fontsize=20, weight='bold')

# 1. Download
sns.lineplot(data=df_final, x='rodada', y='rede.download.mbps', hue='Provedor',
             marker='o', palette=cores, ax=axs[0, 0], linewidth=2.5)
axs[0, 0].set_title('Velocidade de Download (Mbps)', fontsize=14)
axs[0, 0].set_ylabel('Mbps')
axs[0, 0].set_ylim(0, 110)

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
axs[2, 0].set_title('Retransmissões no Download', fontsize=14)
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

print("--- RESUMO DAS MÉDIAS (NOVA ESCOLA) ---")
print(resumo.to_string(index=False))
