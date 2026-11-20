from typing import Protocol


class ProveedorLLM(Protocol):
    def completar(self, prompt: str) -> str: ...
