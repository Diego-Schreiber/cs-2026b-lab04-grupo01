# tests/test_generadores_ia.py
import pytest
from pathlib import Path
from src.reservas.ia.generadores import GeneradorCriteriosLLM, SalidaLLMInvalidaError

class ProveedorGrabadoStub:
    def __init__(self, respuesta_fija: str):
        self._respuesta = respuesta_fija
    def completar(self, prompt: str) -> str:
        return self._respuesta

def test_generador_acepta_respuesta_grabada_valida():
    grabacion = Path("grabaciones/v3/HU-01.txt").read_text(encoding="utf-8")
    generador = GeneradorCriteriosLLM(ProveedorGrabadoStub(grabacion), version="v3")
    resultado = generador.generar("HU-01", "Como paciente quiero reservar una cita...")
    assert resultado["id_historia"] == "HU-01"
    assert resultado["es_invest_valida"] is True
    assert len(resultado["criterios_aceptacion"]) >= 3

def test_generador_rechaza_respuesta_fuera_de_contrato():
    respuesta_corrupta = '{"id_historia": "HU-01", "criterios_aceptacion": "texto invalido"}'
    generador = GeneradorCriteriosLLM(ProveedorGrabadoStub(respuesta_corrupta), version="v3")
    with pytest.raises(SalidaLLMInvalidaError):
        generador.generar("HU-01", "Como paciente quiero reservar una cita...")
