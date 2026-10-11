## Diseño UML (Lab 05)
 
Historia crítica: reservar una cita verificando cupo y evitando doble
asignación (RF-02). Diseño coherente con el [ADR-001](adr/001-estilo-arquitectonico.md). 
### Máquina de estados de Cita

```mermaid
stateDiagram-v2
    [*] --> Reservada : crear() [horario disponible]
    Reservada --> Confirmada : confirmar() [paciente responde el recordatorio]
    Reservada --> Cancelada : cancelar() [anticipación mínima cumplida]
    Reservada --> Atendida : marcarAtendida() [paciente se presenta]
    Reservada --> NoAsistio : marcarNoAsistio() [hora vencida sin atención]
    Confirmada --> Cancelada : cancelar() [anticipación mínima cumplida]
    Confirmada --> Atendida : marcarAtendida() [paciente se presenta]
    Confirmada --> NoAsistio : marcarNoAsistio() [hora vencida sin atención]
    Atendida --> [*]
    NoAsistio --> [*]
    Cancelada --> [*]
 
### Diagramas
- [Historia de usuario](historia.md)
- Clases: [código](uml/clases.puml) · [imagen](img/clases.png)
- Secuencia: [código](uml/secuencia.puml) · [imagen](img/secuencia.png)
- Estados: [código](uml/estados.mmd) · [imagen](img/estados.png)
- Actividades: [código](uml/actividades.puml) · [imagen](img/actividades.png)
- Paquetes: [código](uml/paquetes.puml) · [imagen](img/paquetes.png)
- [ADR-004: puertos en el dominio](adr/004-puertos-en-dominio.md)
- [Round-trip con IA](round-trip.md) · [Consistencia](consistencia.md)
