from decimal import Decimal, InvalidOperation

from pydantic import BaseModel, ConfigDict, field_validator

from clinicasegura.dominio.errores import RecetaInvalida
from clinicasegura.dominio.modelos import Cedula, Receta, validar_cedula


class SolicitudReceta(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    cedula: str
    medicamento: str
    dias: int
    dosis_mg: str

    @field_validator("cedula")
    @classmethod
    def _cedula(cls, valor: str) -> str:
        if not validar_cedula(valor):
            raise RecetaInvalida("la cedula tiene formato 0-0000-0000")
        return valor

    @field_validator("dias")
    @classmethod
    def _dias(cls, valor: int) -> int:
        if valor <= 0:
            raise RecetaInvalida("los dias deben ser mayores que cero")
        if valor > 90:
            raise RecetaInvalida("la vigencia maxima son 90 dias")
        return valor

    @field_validator("dosis_mg")
    @classmethod
    def _dosis(cls, valor: str) -> str:
        try:
            dosis = Decimal(valor)
        except InvalidOperation as e:
            raise RecetaInvalida("la dosis debe ser positiva") from e
        if dosis <= 0:
            raise RecetaInvalida("la dosis debe ser positiva")
        return valor


def a_receta(solicitud: SolicitudReceta) -> Receta:
    return Receta(
        cedula=Cedula(solicitud.cedula),
        medicamento=solicitud.medicamento,
        dias=solicitud.dias,
        dosis_mg=Decimal(solicitud.dosis_mg),
    )
