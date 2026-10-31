import matplotlib.pyplot as plt
import numpy as np

# Datos de la simulación
metricas = ['Latencia p95 (ms)', 'Throughput (tps)', 'Tasa Errores (%)', 'Overbooking (casos)']
antes = [1450, 85, 32.4, 3]
despues = [180, 490, 0.0, 0]
umbrales = [250, 400, 0.0, 0]

x = np.arange(len(metricas))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

rects1 = ax.bar(x - width, antes, width, label='Antes (Monolítico Sincrónico)', color='#D9534F')
rects2 = ax.bar(x, despues, width, label='Después (Queue + Lock)', color='#5CB85C')
rects3 = ax.bar(x + width, umbrales, width, label='Umbral QA-01', color='#0275D8', linestyle='--', fill=False, linewidth=2)

ax.set_ylabel('Valores de Métricas')
ax.set_title('Evaluación de Carga QA-01: Pico Matutino (500 req/s)')
ax.set_xticks(x)
ax.set_xticklabels(metricas)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

ax.bar_label(rects1, padding=3, fmt='%.1f')
ax.bar_label(rects2, padding=3, fmt='%.1f')
ax.bar_label(rects3, padding=3, fmt='%.1f')

fig.tight_layout()
plt.savefig('grafico_pico_qa01.png', dpi=300)
print("Gráfico generado exitosamente: grafico_pico_qa01.png")
