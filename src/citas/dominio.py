from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

class EstadoCita(Enum):
    RESERVADA = "RESERVADA"
    CONFIRMADA = "CONFIRMADA"
    ATENDIDA = "ATENDIDA"
    NO_ASISTIO = "NO_ASISTIO"
    CANCELADA = "CANCELADA"

@dataclass
class Paciente:
    id: UUID
    dni: str
    nombre_completo: str
    celular: str

@dataclass
class HorarioAtencion:
    id: UUID
    fecha_hora_inicio: datetime
    fecha_hora_fin: datetime
    cupos_disponibles: int

    def reservar_cupo(self) -> None:
        if self.cupos_disponibles <= 0:
            raise ValueError("No hay cupos disponibles")
        self.cupos_disponibles -= 1

    def liberar_cupo(self) -> None:
        self.cupos_disponibles += 1

@dataclass
class Cita:
    paciente_id: UUID
    horario_id: UUID
    fecha_hora: datetime
    id: UUID = field(default_factory=uuid4)
    estado: EstadoCita = EstadoCita.RESERVADA

    def confirmar(self) -> None:
        self.estado = EstadoCita.CONFIRMADA

    def atender(self) -> None:
        self.estado = EstadoCita.ATENDIDA

    def marcar_no_asistio(self) -> None:
        self.estado = EstadoCita.NO_ASISTIO

    def cancelar(self, motivo: str) -> None:
        self.estado = EstadoCita.CANCELADA

class RepositorioCitas(ABC):
    @abstractmethod
    def buscar_por_id(self, id: UUID) -> Cita:
        pass

    @abstractmethod
    def guardar(self, cita: Cita) -> None:
        pass

    @abstractmethod
    def existe_cita_paciente(self, paciente_id: UUID, fecha_hora: datetime) -> bool:
        pass

class NotificadorSMS(ABC):
    @abstractmethod
    def enviar_recordatorio_cita(self, cita: Cita) -> None:
        pass
