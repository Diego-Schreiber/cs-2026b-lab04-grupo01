import matplotlib.pyplot as plt

peticiones = list(range(1, 61))
latencias = []
canales = []

for i in peticiones:
    if i < 20:
        latencias.append(45)  # WhatsApp Normal
        canales.append('WhatsApp')
    elif 20 <= i <= 23:
        latencias.append(5000)  # Inyección de timeouts
        canales.append('WhatsApp (Fallo)')
    else:
        latencias.append(120)  # Circuito Abierto -> Fallback SMS
        canales.append('SMS (Fallback)')

plt.figure(figsize=(10, 5))
plt.axvspan(19.5, 23.5, color='red', alpha=0.2, label='Inyección de Fallos WhatsApp')
plt.plot(peticiones[:19], latencias[:19], 'g-o', label='Canal WhatsApp (Normal)')
plt.plot(peticiones[19:23], latencias[19:23], 'r-x', label='Timeouts WhatsApp (Fallo)')
plt.plot(peticiones[23:], latencias[23:], 'b-s', label='Fallback SMS (Circuito Abierto < 120ms)')

plt.axhline(y=2000, color='orange', linestyle='--', label='Umbral Máximo QA-03 (2000 ms)')
plt.title('Resiliencia QA-03: Conmutación de Canal con Circuit Breaker')
plt.xlabel('Número de Petición')
plt.ylabel('Tiempo de Respuesta / Conmutación (ms)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.savefig('grafico_circuit_breaker.png', dpi=300)
print("Gráfico generado exitosamente: grafico_circuit_breaker.png")
