"""
mis_pruebas · etapa 5

Aclaracion: use IA (Cursor) para armar el esqueleto de estas pruebas y
automatizar los casos que pide la practica (reloj fijo, cadena caida, borde,
folio sin random). Yo las revise, las corri en pytest y las entiendo para
defenderlas; no las pegue sin leerlas.
"""

from datetime import datetime, timedelta
from decimal import Decimal

import pytest

from clinicasegura.dominio.modelos import Cedula, Despacho, Receta, validar_cedula
from clinicasegura.dominio.servicio import EmisionDeRecetas


class RelojFijo:
    def __init__(self):
        self.cuando = datetime(2026, 3, 1, 9, 0, 0)

    def ahora(self):
        return self.cuando


class FoliosEnOrden:
    def __init__(self):
        self.n = 0

    def siguiente(self):
        self.n += 1
        return f"F-{self.n:05d}"


class FarmaciaEnMemoria:
    cadena = "farmauno"

    def enviar(self, receta, folio, vence):
        return Despacho(folio=folio, cadena=self.cadena, vence=vence)


class BitacoraLista:
    def __init__(self):
        self.eventos = []

    def registrar(self, evento, folio):
        self.eventos.append((evento, folio))


class PasarelaCaida:
    cadena = "farmauno"

    def enviar(self, receta, folio, vence):
        raise TimeoutError("la cadena no respondio")


def _receta():
    return Receta(
        cedula=Cedula("1-1234-5678"),
        medicamento="N02BE01",
        dias=30,
        dosis_mg=Decimal("500"),
    )


def test_vigencia_con_reloj_fijo():
    servicio = EmisionDeRecetas(
        pasarelas={"farmauno": FarmaciaEnMemoria()},
        reloj=RelojFijo(),
        folios=FoliosEnOrden(),
        bitacora=BitacoraLista(),
    )
    despacho = servicio.emitir(_receta(), "farmauno")
    esperado = datetime(2026, 3, 1, 9, 0, 0) + timedelta(days=30)
    assert despacho.vence == esperado


def test_cadena_caida():
    servicio = EmisionDeRecetas(
        pasarelas={"farmauno": PasarelaCaida()},
        reloj=RelojFijo(),
        folios=FoliosEnOrden(),
        bitacora=BitacoraLista(),
    )
    with pytest.raises(TimeoutError):
        servicio.emitir(_receta(), "farmauno")


def test_cedula_invalida_rechazada_en_el_borde():
    assert not validar_cedula("abc")


def test_folio_predecible_sin_random():
    servicio = EmisionDeRecetas(
        pasarelas={"farmauno": FarmaciaEnMemoria()},
        reloj=RelojFijo(),
        folios=FoliosEnOrden(),
        bitacora=BitacoraLista(),
    )
    assert servicio.emitir(_receta(), "farmauno").folio == "F-00001"
    assert servicio.emitir(_receta(), "farmauno").folio == "F-00002"
