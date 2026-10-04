# Drivers Arquitectónicos - CitaSalud Arequipa

Este documento recopila los drivers arquitectónicos (requisitos funcionales, atributos de calidad, restricciones y escenarios de calidad) que guiarán el diseño del sistema **CitaSalud Arequipa**[cite: 6].

---

## 1. Requisitos Funcionales Clave (RF)
| ID | Actor | Descripción |
| :--- | :--- | :--- |
| **RF-01** | Paciente | Buscar disponibilidad de médicos por especialidad, clínica, fecha y horario. |
| **RF-02** | Paciente | Seleccionar un horario y reservar una cita médica en tiempo real, evitando sobreventas. |
| **RF-03** | Paciente | Consultar sus citas programadas y realizar la cancelación o reprogramación con anticipación. |
| **RF-04** | Personal de Admisión | Visualizar, filtrar y gestionar la lista de pacientes agendados para el día en la clínica correspondiente. |
| **RF-05** | Sistema | Enviar recordatorios automáticos de citas vía notificación (WhatsApp/Correo) 24 horas antes. |

---

## 2. Atributos de Calidad (Priorizados)
1. **Disponibilidad y Rendimiento (Crítico):** El sistema debe soportar un pico masivo de tráfico y concurrencia de pacientes entre las **7:00 a. m. y 7:15 a. m.** (apertura de agenda diaria).
2. **Consistencia de Datos (Integridad):** Garantizar cero duplicidad de reservas o cruce de horarios para un mismo médico bajo concurrencia alta.
3. **Seguridad y Privacidad:** Protección de datos sensibles e historia clínica de los pacientes bajo la normativa local (Ley 29733).
4. **Mantenibilidad y Modificabilidad:** Facilidad para escalar componentes y cambiar reglas de negocio (ej. tarifas o convenios de seguros) sin afectar el núcleo de agendamiento.

---

## 3. Restricciones Arquitectónicas (R)
* **R-01 (Plazo):** El Producto Mínimo Viable (MVP) debe estar listo y desplegado en producción en un plazo máximo de **1 mes**.
* **R-02 (Tecnología):** El desarrollo debe emplear estrictamente el stack tecnológico dominado por los integrantes del equipo (ej. Node.js/Python para backend, React/Next.js para frontend, PostgreSQL).
* **R-03 (Presupuesto):** La infraestructura inicial en la nube no debe superar un costo de **USD 30 mensuales** (uso de capas gratuitas o servicios optimizados).
* **R-04 (Normativa):** Cumplimiento obligatorio de la **Ley N° 29733** (Ley de Protección de Datos Personales en el Perú).
* **R-05 (Integración):** Obligatoriedad de integrarse con pasarelas de pago locales y la API oficial de WhatsApp Business para los recordatorios.

---

## 4. Escenarios de Calidad

### Escenario 1: Concurrencia Masiva Matutina (Rendimiento / Disponibilidad)
* **Fuente:** 5,000 pacientes concurrentes intentando reservar cita simultáneamente.
* **Estímulo:** Solicitudes HTTP masivas de búsqueda y reserva a las 7:00 a. m.
* **Entorno:** Horario pico de apertura de agenda diaria en ambiente de producción.
* **Artefacto:** Módulo de gestión y reservas de citas.
* **Respuesta:** El sistema procesa las solicitudes de reserva distribuyendo la carga y manteniendo la estabilidad operativa.
* **Medida:** El tiempo de respuesta (p95) para confirmar una reserva es menor o igual a **3 segundos**, con una tasa de error HTTP menor al **1%**.

### Escenario 2: Integridad de Agenda ante Concurrencia (Consistencia)
* **Fuente:** Dos pacientes distintos intentando reservar exactamente el mismo último cupo disponible con el mismo médico al mismo milisegundo.
* **Estímulo:** Peticiones de escritura concurrentes sobre el mismo recurso de la base de datos.
* **Entorno:** Operación normal bajo alta demanda.
* **Artefacto:** Base de datos relacional y servicio transaccional de citas.
* **Respuesta:** El motor de base de datos aplica bloqueo transaccional (aislamiento estricto), permitiendo que solo una transacción proceda con éxito y rechazando limpiamente la segunda.
* **Medida:** Se registran **0 sobreventas** o citas duplicadas en la agenda del médico.

### Escenario 3: Recuperación ante Fallos de Red (Disponibilidad)
* **Fuente:** Caída temporal del proveedor de servicios de mensajería (WhatsApp API).
* **Estímulo:** El microservicio de notificaciones intenta enviar un recordatorio y recibe un timeout.
* **Entorno:** Operación en tiempo de ejecución.
* **Artefacto:** Cola de mensajes y componente de reintentos asíncronos.
* **Respuesta:** El sistema aísla el fallo mediante un patrón de reintentos (*Circuit Breaker*) y encola los mensajes pendientes sin afectar ni bloquear la funcionalidad principal de agendamiento web.
* **Medida:** El flujo de reserva del paciente no sufre retrasos ni bloqueos (**0% de impacto** en el hilo principal de reservas), y las notificaciones se reintentan de forma autónoma tras la recuperación del servicio.
