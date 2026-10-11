# src/reservas/adaptador_whatsapp.py
from .entidades import Cita
from .puertos import PuertoNotificacion

class AdaptadorWhatsApp(PuertoNotificacion):
    def __init__(self, max_reintentos: int = 5) -> None:
        self._max_reintentos = max_reintentos

    def enviar_recordatorio(self, cita: Cita) -> bool:
        raise NotImplementedError("Llamar a la API de WhatsApp Business")
