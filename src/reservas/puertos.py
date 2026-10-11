# src/reservas/puertos.py
from abc import ABC, abstractmethod
from datetime import date
from uuid import UUID
from .entidades import Cita, Horario

class RepositorioAgenda(ABC):
    @abstractmethod
    def bloquear_horario(self, horario_id: UUID) -> Horario: ...

    @abstractmethod
    def buscar_horarios_alternativos(self, medico_id: UUID, fecha: date) -> list[Horario]: ...

    @abstractmethod
    def guardar(self, cita: Cita) -> None: ...

class PuertoNotificacion(ABC):
    @abstractmethod
    def enviar_recordatorio(self, cita: Cita) -> bool: ...
