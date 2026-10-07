# Reporte de Auditoría de Consistencia (C1 - C5)

| Regla | Elemento Auditado | Hallazgo | Verificación / Decisión |
| :--- | :--- | :--- | :--- |
| **C1** | `ServicioCitas` -> `NotificadorSMS` | El mensaje `enviarRecordatorioCita` concuerda exactamente con el puerto en el diagrama de clases. | **Aceptado**: Coincidencia total. |
| **C2** | Transición `NO_ASISTIO` | La transición `marcarNoAsistio()` en la máquina de estados está soportada por el método `marcar_no_asistio()` en `Cita`. | **Aceptado**: Consistencia verificada. |
| **C1** | `ServicioCitas` -> `HorarioAtencion` | *Hallazgo de la IA:* "No existe el método `reservarCupo()` en la interfaz del controlador". | **Falso Positivo**: El mensaje se envía a la entidad `HorarioAtencion`, donde sí está definido el método `reservarCupo()`. Se rechaza el hallazgo. |
| **C4** | Dependencias de paquetes | No existen dependencias cíclicas; `citas` consume puertos de `notificaciones` de forma unidireccional. | **Aceptado**: Cumple regla C4. |
| **C5** | Nombres del dominio | Coincidencia de términos (`Paciente`, `Cita`, `HorarioAtencion`, `EstadoCita`) en diagramas y código. | **Aceptado**: Cumple regla C5. |
