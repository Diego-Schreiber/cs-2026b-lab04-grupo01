from abc import ABC, abstractmethod
from pathlib import Path


class ProveedorLLM(ABC):
    @abstractmethod
    def completar(self, prompt: str) -> str:
        """Envía el prompt al modelo y devuelve la respuesta textual cruda."""


class ProveedorGrabado(ProveedorLLM):
    """Adaptador determinista que lee salidas pregrabadas para pruebas y CI."""

    def __init__(self, ruta_grabacion: str | Path):
        self._ruta = Path(ruta_grabacion)

    def completar(self, prompt: str) -> str:
        return self._ruta.read_text(encoding="utf-8").strip()
