import re
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

_PATRON_CEDULA = re.compile(r"^\d-\d{4}-\d{4}$")


def validar_cedula(valor: str) -> bool:
    return _PATRON_CEDULA.fullmatch(valor) is not None


@dataclass(frozen=True)
class Cedula:
    valor: str


@dataclass(frozen=True)
class Receta:
    cedula: Cedula
    medicamento: str
    dias: int
    dosis_mg: Decimal
    riesgo_alto: bool = False


@dataclass(frozen=True)
class Despacho:
    folio: str
    cadena: str
    vence: datetime
