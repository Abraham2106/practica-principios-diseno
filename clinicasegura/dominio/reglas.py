from decimal import Decimal


def calcular_recargo( dias_restantes: int, tarifa_diaria: Decimal, recargo_por_riesgo: bool) -> Decimal:
    monto = tarifa_diaria * dias_restantes
    if recargo_por_riesgo:
        monto *= 2
    return monto
