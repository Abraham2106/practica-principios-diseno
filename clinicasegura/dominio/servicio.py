from datetime import timedelta

from clinicasegura.dominio.errores import CadenaNoSoportada, FarmaciaNoDisponible
from clinicasegura.dominio.modelos import Despacho, Receta

_VIGENCIA_DIAS = 30


class EmisionDeRecetas:
    def __init__(self, pasarelas, reloj, folios, bitacora):
        self._pasarelas = pasarelas
        self._reloj = reloj
        self._folios = folios
        self._bitacora = bitacora

    def emitir(self, receta: Receta, cadena: str) -> Despacho:
        pasarela = self._pasarelas.get(cadena)
        if pasarela is None:
            raise CadenaNoSoportada(cadena)
        folio = self._folios.siguiente()
        vence = self._reloj.ahora() + timedelta(days=_VIGENCIA_DIAS)
        try:
            despacho = pasarela.enviar(receta, folio, vence)
        except TimeoutError as e:
            self._bitacora.registrar("farmacia_no_disponible", folio)
            raise FarmaciaNoDisponible(f"{cadena} / {folio}") from e
        self._bitacora.registrar("emitida", folio)
        return despacho
