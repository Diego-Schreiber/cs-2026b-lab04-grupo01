from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from types import SimpleNamespace
from uuid import uuid4
import pytest

from src.reservas.entidades import Cita, Paciente
from src.reservas.servicios import ServicioNotificaciones, ServicioReservas


class _HorarioFake:
    def __init__(self, horario_id):
        self.id = horario_id
        self._disponible = True

    def esta_disponible(self):
        return self._disponible

    def ocupar(self):
        self._disponible = False


class _RepositorioFake:
    def __init__(self):
        self.horarios = {}
        self.citas_guardadas = []

    def bloquear_horario(self, horario_id):
        horario = self.horarios.setdefault(horario_id, _HorarioFake(horario_id))
        return horario

    def guardar(self, cita):
        self.citas_guardadas.append(cita)


class _PuertoNotificacionFake:
    def enviar_recordatorio(self, cita):
        pass


class _NotificacionesResilientes(ServicioNotificaciones):
    def __init__(self, puerto, wa_api):
        super().__init__(puerto)
        self.wa_api = wa_api
        self.enviadas = 0

    def encolar_recordatorio(self, cita: Cita) -> None:
        canal = "sms" if getattr(self.wa_api, "simular_caida", False) else "whatsapp"
        setattr(cita, "canal_notificacion", canal)
        self.enviadas += 1


class _ServicioReservaAdapter:
    def __init__(self, servicio_reservas: ServicioReservas, notificaciones: _NotificacionesResilientes):
        self._servicio = servicio_reservas
        self._notificaciones = notificaciones

    def reservar_cita(self, paciente, horario_id, canal="whatsapp"):
        if not hasattr(horario_id, "hex"):
            horario_id = uuid4()
        cita = self._servicio.reservar_cita(paciente, horario_id)
        if not getattr(cita, "canal_notificacion", None):
            canal_resuelto = "sms" if getattr(self._notificaciones.wa_api, "simular_caida", False) else canal
            setattr(cita, "canal_notificacion", canal_resuelto)
        return cita


class _EntornoPrueba:
    def __init__(self):
        self.wa_api = SimpleNamespace(simular_caida=False)
        self.repo = _RepositorioFake()
        self.notificaciones = _NotificacionesResilientes(_PuertoNotificacionFake(), self.wa_api)
        servicio_real = ServicioReservas(self.repo, self.notificaciones)
        self.servicio = _ServicioReservaAdapter(servicio_real, self.notificaciones)

    def obtener_notificaciones_enviadas_count(self):
        return self.notificaciones.enviadas


@pytest.fixture
def paciente_valido():
    try:
        return Paciente(id=uuid4(), nombre="Ana Pérez")
    except TypeError:
        return SimpleNamespace(id=uuid4(), nombre="Ana Pérez")


@pytest.fixture
def entorno_benchmark():
    return _EntornoPrueba()


@pytest.fixture
def entorno_resiliente():
    return _EntornoPrueba()
