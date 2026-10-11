# src/reservas/entidades.py
from __future__ import annotations
from datetime import datetime
from uuid import UUID, uuid4
from .estado_cita import EstadoCita

class Especialidad:
    def __init__(self, id: int, nombre: str) -> None:
        self._id = id
        self._nombre = nombre

class Paciente:
    def __init__(self, dni: str, nombres: str, celular: str, correo: str) -> None:
        self._id: UUID = uuid4()
        self._dni = dni
        self._nombres = nombres
        self._celular = celular
        self._correo = correo

class Horario:
    def __init__(self, fecha_hora: datetime, duracion_min: int) -> None:
        self._id: UUID = uuid4()
        self._fecha_hora = fecha_hora
        self._duracion_min = duracion_min
        self._ocupado = False

    def esta_disponible(self) -> bool:
        return not self._ocupado

    def ocupar(self) -> None:
        if self._ocupado:
            raise ValueError("Horario ocupado")
        self._ocupado = True

    def liberar(self) -> None:
        self._ocupado = False

class Medico:
    def __init__(self, nombre_completo: str, cmp: str, especialidad: Especialidad) -> None:
        self._id: UUID = uuid4()
        self._nombre_completo = nombre_completo
        self._cmp = cmp
        self._especialidad: Especialidad = especialidad
        self._horarios: list[Horario] = []

    def ofrecer(self, horario: Horario) -> None:
        self._horarios.append(horario)

class Cita:
    def __init__(self, paciente: Paciente, horario: Horario) -> None:
        self._id: UUID = uuid4()
        self._paciente: Paciente = paciente
        self._horario: Horario = horario
        self._estado: EstadoCita = EstadoCita.RESERVADA
        self._fecha_registro = datetime.now()

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def estado(self) -> EstadoCita:
        return self._estado

    @staticmethod
    def crear(paciente: Paciente, horario: Horario) -> "Cita":
        return Cita(paciente, horario)

    def confirmar(self) -> None:
        self._estado = EstadoCita.CONFIRMADA

    def cancelar(self) -> None:
        self._estado = EstadoCita.CANCELADA
        self._horario.liberar()

    def marcar_atendida(self) -> None:
        self._estado = EstadoCita.ATENDIDA

    def marcar_no_asistio(self) -> None:
        self._estado = EstadoCita.NO_ASISTIO
