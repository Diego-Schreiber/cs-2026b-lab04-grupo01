# Historia de Usuario - HU-01: Reserva de Citas Médicas

**Como** paciente de CitaSalud Arequipa,  
**Quiero** reservar una cita médica seleccionando especialidad, médico y horario,  
**Para** asegurar mi atención médica previa verificación de cupo y evitar doble asignación de horarios.

## Criterios de Aceptación

1. **Dado** un paciente autenticado y un horario de atención con cupos disponibles (`cuposDisponibles > 0`), **cuando** el paciente solicita la reserva de una cita, **entonces** el sistema decrementa en 1 los cupos del horario, crea la cita en estado `RESERVADA` y genera una confirmación.
2. **Dado** un paciente que ya posee una cita programada en la misma fecha/hora o un horario sin cupos (`cuposDisponibles == 0`), **cuando** intenta realizar la reserva, **entonces** el sistema rechaza la solicitud, no modifica la disponibilidad de cupos y retorna un mensaje de error explícito de disponibilidad o solapamiento.
