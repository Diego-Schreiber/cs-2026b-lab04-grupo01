import pytest
import time

def test_fitness_presupuesto_latencia_p95_reserva(entorno_benchmark, paciente_valido):
    tiempos = []
    for _ in range(100):
        t0 = time.perf_counter()
        entorno_benchmark.servicio.reservar_cita(paciente_valido, "H1", canal="whatsapp")
        tiempos.append((time.perf_counter() - t0) * 1000)
    
    tiempos.sort()
    p95 = tiempos[int(len(tiempos) * 0.95)]
    assert p95 < 250.0, f"Violación de Fitness Function: p95 = {p95:.2f} ms (Límite: 250ms)"

def test_fitness_zero_notificaciones_perdidas(entorno_resiliente, paciente_valido):
    entorno_resiliente.wa_api.simular_caida = True
    cita = entorno_resiliente.servicio.reservar_cita(paciente_valido, "H1", canal="whatsapp")
    assert cita.canal_notificacion in ["sms", "correo"], "Conmutación fallida"
    assert entorno_resiliente.obtener_notificaciones_enviadas_count() == 1
