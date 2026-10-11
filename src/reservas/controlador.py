# src/reservas/controlador.py
from dataclasses import dataclass
from uuid import UUID
from .entidades import Paciente
from .servicios import ServicioReservas

@dataclass
class CitaDTO:
    id: str
    estado: str

class ControladorReservas:
    def __init__(self, servicio: ServicioReservas) -> None:
        self._servicio: ServicioReservas = servicio

    def reservar_cita(self, paciente: Paciente, horario_id: UUID) -> CitaDTO:
        cita = self._servicio.reservar_cita(paciente, horario_id)
        return CitaDTO(id=str(cita.id), estado=cita.estado.value)
