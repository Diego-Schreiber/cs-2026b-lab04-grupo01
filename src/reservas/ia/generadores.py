# src/reservas/ia/generadores.py
import json
from pathlib import Path
import jsonschema
from src.reservas.ia.proveedor import ProveedorLLM

class SalidaLLMInvalidaError(Exception):
    """Se lanza cuando la salida del LLM viola el JSON Schema o las reglas de seguridad."""

class GeneradorCriteriosLLM:
    def __init__(self, proveedor: ProveedorLLM, version: str = "v3"):
        self._proveedor = proveedor
        base = Path(__file__).resolve().parents[3] / "prompts"
        self._plantilla = (base / f"criterios_{version}.txt").read_text(encoding="utf-8")
        self._esquema = json.loads((base / "esquema.json").read_text(encoding="utf-8"))

    def generar(self, id_historia: str, historia_usuario: str) -> dict:
        prompt = (
            self._plantilla
            .replace("{{id_historia}}", id_historia)
            .replace("{{historia}}", f"<historia_usuario>{historia_usuario}</historia_usuario>")
        )
        respuesta_cruda = self._proveedor.completar(prompt)
        try:
            datos = json.loads(respuesta_cruda)
            jsonschema.validate(instance=datos, schema=self._esquema)
        except (json.JSONDecodeError, jsonschema.ValidationError) as exc:
            raise SalidaLLMInvalidaError(f"Contrato incumplido para {id_historia}: {exc}") from exc
        return datos
