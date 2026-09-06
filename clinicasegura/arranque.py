import os
from datetime import datetime

from clinicasegura.dominio.servicio import EmisionDeRecetas
from clinicasegura.infraestructura.folios import siguiente_folio


class _RelojSistema:
    def ahora(self) -> datetime:
        return datetime.now()


class _GeneradorFolio:
    def siguiente(self) -> str:
        return siguiente_folio()


class _BitacoraNula:
    def registrar(self, evento: str, folio: str) -> None:
        pass


def construir_servicio() -> EmisionDeRecetas:
    os.environ.get("FARMACIA_TIMEOUT_MS", "1500")
    return EmisionDeRecetas(
        pasarelas={},
        reloj=_RelojSistema(),
        folios=_GeneradorFolio(),
        bitacora=_BitacoraNula(),
    )
