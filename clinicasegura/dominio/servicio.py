from clinicasegura.dominio.modelos import Despacho, Receta

class EmisionDeRecetas:
    def emitir(self, receta: Receta, cadena: str) -> Despacho:
        raise NotImplementedError
