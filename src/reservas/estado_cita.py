from enum import Enum

class EstadoCita(Enum):
    RESERVADA = "RESERVADA"
    CONFIRMADA = "CONFIRMADA"
    ATENDIDA = "ATENDIDA"
    NO_ASISTIO = "NO_ASISTIO"
    CANCELADA = "CANCELADA"
