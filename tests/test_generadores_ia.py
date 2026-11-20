import pytest
from src.reservas.ia.generadores import (
    GeneradorCriteriosLLM,
    GeneradorDatosSinteticosLLM,
    SalidaLLMInvalidaError,
)
from src.reservas.ia.proveedor import ProveedorGrabado, ProveedorLLM


class ProveedorCorruptoStub(ProveedorLLM):
    def __init__(self, salida_invalida: str):
        self._salida = salida_invalida

    def completar(self, prompt: str) -> str:
        return self._salida


def test_generador_criterios_acepta_respuesta_grabada_valida():
    proveedor = ProveedorGrabado("grabaciones/v3/HU-01.txt")
    generador = GeneradorCriteriosLLM(proveedor, version="v3")
    resultado = generador.generar("HU-01", "Como paciente quiero reservar una cita...")
    assert resultado["id_historia"] == "HU-01"
    assert resultado["es_invest_valida"] is True
    assert len(resultado["criterios_aceptacion"]) >= 3


def test_generador_criterios_rechaza_respuesta_fuera_de_contrato():
    stub = ProveedorCorruptoStub('{"id_historia": "HU-01", "criterios_aceptacion": "texto invalido"}')
    generador = GeneradorCriteriosLLM(stub, version="v3")
    with pytest.raises(SalidaLLMInvalidaError):
        generador.generar("HU-01", "Como paciente quiero reservar una cita...")


def test_generador_datos_acepta_lote_sintetico_valido():
    proveedor = ProveedorGrabado("grabaciones/v3/DATOS-01.txt")
    generador = GeneradorDatosSinteticosLLM(proveedor, version="v3")
    resultado = generador.generar("Genera 1 paciente ficticio y 1 cita RESERVADA.")
    assert resultado["pacientes"][0]["dni_ficticio"].startswith("999")
    assert resultado["pacientes"][0]["es_ficticio"] is True


def test_generador_datos_rechaza_dni_real_inyectado():
    payload_inseguro = (
        '{"pacientes":[{"id_paciente":"PAC-TEST-001","dni_ficticio":"72458912",'
        '"es_ficticio":true,"marca_seguridad":"DATO_SINTETICO_PRUEBA",'
        '"nombres":"Juan Perez","celular_ficticio":"900123456"}],'
        '"citas":[{"id_cita":"CIT-TEST-001","id_paciente":"PAC-TEST-001",'
        '"especialidad":"Medicina General","fecha_hora":"2026-11-20T09:00:00Z",'
        '"estado":"RESERVADA","es_ficticio":true}]}'
    )
    generador = GeneradorDatosSinteticosLLM(ProveedorCorruptoStub(payload_inseguro), version="v3")
    with pytest.raises(SalidaLLMInvalidaError):
        generador.generar("Genera 1 paciente.")
