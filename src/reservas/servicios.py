# src/reservas/servicios.py
from uuid import UUID
from .entidades import Cita, Paciente
from .puertos import PuertoNotificacion, RepositorioAgenda

class ServicioNotificaciones:
    def __init__(self, puerto: PuertoNotificacion) -> None:
        self._puerto: PuertoNotificacion = puerto

    def encolar_recordatorio(self, cita: Cita) -> None:
        raise NotImplementedError("Registrar el mensaje en la cola (Redis)")

    def enviar_recordatorio(self, cita: Cita) -> None:
        self._puerto.enviar_recordatorio(cita)

    def enviar_por_correo(self, cita: Cita) -> None:
        raise NotImplementedError

class ServicioReservas:
    def __init__(
        self, repositorio: RepositorioAgenda, notificaciones: ServicioNotificaciones
    ) -> None:
        self._repositorio: RepositorioAgenda = repositorio
        self._notificaciones: ServicioNotificaciones = notificaciones

    def reservar_cita(self, paciente: Paciente, horario_id: UUID) -> Cita:
        horario = self._repositorio.bloquear_horario(horario_id)
        if not horario.esta_disponible():
            raise ValueError("Cupo no disponible")
        horario.ocupar()
        cita = Cita.crear(paciente, horario)
        self._repositorio.guardar(cita)
        self._notificaciones.encolar_recordatorio(cita)
        return cita
