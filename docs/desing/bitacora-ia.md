# Bitácora de Interacciones con Inteligencia Artificial

1. **Fecha**: 06/10/2026 | **Herramienta**: ChatGPT / Gemini  
   * **Prompt**: "Genera un diagrama de clases en PlantUML para la reserva de citas en un centro de salud..."  
   * **Propuesta IA**: Incluía una clase `Factura` y relaciones directas con pasarelas de pago con tarjeta.  
   * **Verificación**: El MVP no requiere cobro por tarjeta en la reserva inicial.  
   * **Decisión**: Rechazada y simplificada la clase `Factura`.

2. **Fecha**: 06/10/2026 | **Herramienta**: ChatGPT / Gemini  
   * **Prompt**: "Crea el diagrama de secuencia en PlantUML para el flujo de reserva con alt y loop..."  
   * **Propuesta IA**: Propuso enviar el SMS de notificación como un mensaje síncrono bloqueante.  
   * **Verificación**: El envío síncrono ralentiza la respuesta HTTP al cliente de la App Móvil.  
   * **Decisión**: Modificado a mensaje asíncrono `->>`.

3. **Fecha**: 07/10/2026 | **Herramienta**: ChatGPT / Gemini  
   * **Prompt**: "Convierte el diagrama PlantUML de clases a esqueleto Python 3.10 usando dataclasses..."  
   * **Propuesta IA**: Creó clases de Python funcionales respetando la enumeración `EstadoCita`.  
   * **Verificación**: Revisión con la regla C5 (nombres consistentes en snake_case).  
   * **Decisión**: Aceptada la propuesta.

4. **Fecha**: 07/10/2026 | **Herramienta**: ChatGPT / Gemini  
   * **Prompt**: "Audita estos diagramas buscando inconsistencias según reglas C1 a C5..."  
   * **Propuesta IA**: Reportó un error falso positivo indicando que faltaba un método en el controlador.  
   * **Verificación**: Análisis directo del diagrama de secuencia mostró invocación correcta hacia la entidad.  
   * **Decisión**: Reportado como falso positivo en `consistencia.md`.

5. **Fecha**: 07/10/2026 | **Herramienta**: ChatGPT / Gemini  
   * **Prompt**: "Genera máquina de estados Mermaid para la entidad Cita..."  
   * **Propuesta IA**: Incluyó estados `PENDIENTE_PAGO` y `REEMBOLSADA`.  
   * **Verificación**: Incompatibles con la enumeración definida en el modelo de dominio.  
   * **Decisión**: Removidos para mantener coherencia con `EstadoCita`.
