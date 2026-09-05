# Bitácora de la práctica

Estudiante:
Carné:

> Cómo se llena cada entrada, en este orden y sin saltarse pasos:
>
> 1. **Predicción** — escríbala ANTES de correr nada. Qué cree que va a
>    pasar y por qué. Equivocarse aquí y entender después vale más que
>    acertar; no vuelva a corregirla.
> 2. **Observación** — corra el experimento de la etapa y pegue la salida.
> 3. **Explicación** — por qué pasó lo que pasó, en sus palabras, citando
>    **su** archivo y **su** línea (`servicio.py:24`).
> 4. **Sello** — corra `python herramientas/marcador.py` al cerrar la
>    etapa y pegue el sello que imprime.

## Etapa 0 — Diagnóstico

**Predicción:**
El test de la etapa 0 va a pasar sin problemas porque llene la tabla de diagnostico y el analisis es correcto sobre la codebase. 
**Observación:**

```
pytest -m etapa0
....                                                                                                                                                             [100%]
4 passed, 80 deselected in 0.15s
```

**Explicación:**
Todos los tests pasaron porque rellene de manera correcta la tabla de Diagnostico 
**Sello:**
`c34d278e3bd51d6a` 
## Etapa 1 — Dividir y conquistar, cohesión

**Predicción:**
Las responsabilidades que logre contar fueron 7: como valida, el calculo del recargo, write en la base de datos, generacion del folio, vigencia con now(),a la exportacion y la busqueda de pacientes. Serian como 6 archivos nuevos, los init de cada pieza (`dominio/app/infra`) y los `.py` de `modelos.py`, `reglas.py` y `errores.py`. 

**Observación:**

```
pytest -m etapa1 -q              
FFF....                                                                                                                                                                                                     [100%]
==================================================================================================== FAILURES ====================================================================================================
_________________________________________________________________________________________ test_existen_los_tres_paquetes _________________________________________________________________________________________
pruebas\apoyo.py:22: in importar
    return importlib.import_module(ruta)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   ModuleNotFoundError: No module named 'clinicasegura.dominio'

During handling of the above exception, another exception occurred:
pruebas\test_etapa1_division_cohesion.py:37: in test_existen_los_tres_paquetes
    importar(f"clinicasegura.{paquete}")
pruebas\apoyo.py:24: in importar
    pytest.fail(
E   Failed: Falta el módulo «clinicasegura.dominio».
E      Cree el archivo clinicasegura/dominio.py (y el __init__.py de su paquete).
E      Detalle: No module named 'clinicasegura.dominio'
_______________________________________________________________________________ test_el_dominio_define_sus_tipos_y_son_inmutables ________________________________________________________________________________
pruebas\apoyo.py:22: in importar
    return importlib.import_module(ruta)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   ModuleNotFoundError: No module named 'clinicasegura.dominio'

During handling of the above exception, another exception occurred:
pruebas\test_etapa1_division_cohesion.py:42: in test_el_dominio_define_sus_tipos_y_son_inmutables
    tipo = obtener("clinicasegura.dominio.modelos", nombre)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pruebas\apoyo.py:38: in obtener
    mod = importar(ruta)
          ^^^^^^^^^^^^^^
pruebas\apoyo.py:24: in importar
    pytest.fail(
E   Failed: Falta el módulo «clinicasegura.dominio.modelos».
E      Cree el archivo clinicasegura/dominio/modelos.py (y el __init__.py de su paquete).
E      Detalle: No module named 'clinicasegura.dominio'
___________________________________________________________________________________ test_el_dominio_define_sus_propios_errores ___________________________________________________________________________________
pruebas\apoyo.py:22: in importar
    return importlib.import_module(ruta)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..\..\..\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py:90: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E   ModuleNotFoundError: No module named 'clinicasegura.dominio'

During handling of the above exception, another exception occurred:
pruebas\test_etapa1_division_cohesion.py:54: in test_el_dominio_define_sus_propios_errores
    base = obtener("clinicasegura.dominio.errores", "ErrorDominio")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pruebas\apoyo.py:38: in obtener
    mod = importar(ruta)
          ^^^^^^^^^^^^^^
pruebas\apoyo.py:24: in importar
    pytest.fail(
E   Failed: Falta el módulo «clinicasegura.dominio.errores».
E      Cree el archivo clinicasegura/dominio/errores.py (y el __init__.py de su paquete).
E      Detalle: No module named 'clinicasegura.dominio'
============================================================================================ short test summary info =============================================================================================
FAILED pruebas/test_etapa1_division_cohesion.py::test_existen_los_tres_paquetes - Failed: Falta el módulo «clinicasegura.dominio».
FAILED pruebas/test_etapa1_division_cohesion.py::test_el_dominio_define_sus_tipos_y_son_inmutables - Failed: Falta el módulo «clinicasegura.dominio.modelos».
FAILED pruebas/test_etapa1_division_cohesion.py::test_el_dominio_define_sus_propios_errores - Failed: Falta el módulo «clinicasegura.dominio.errores».

python herramientas/marcador.py 1

  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Abraham Solano Parrales   carné 2024132538
  ────────────────────────────────────────────────────────────
  Etapa 1  Dividir y conquistar · cohesión              ███████        verde
  ────────────────────────────────────────────────────────────
  7 pruebas en verde · 0 por resolver
  corrida #3 registrada
  SELLO: 59c5807f2d83c4ff
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.
```

**Explicación:**
Al principio fallaron 3 pruebas porque no existia clinicasegura/dominio. Despues de crear los __init__.py en dominio, aplicacion e infraestructura, Cedula Receta y Despacho con frozen=True en modelos.py y ErrorDominio con sus hijas en errores.py pasaron las 7 pruebas en verde. El campo medicamento en Receta no sale del legado pero lo agregue porque en otros tests de etapas avanzadas (como test_etapa4 y test_etapa5) vi que construyen la receta con medicamentos.

**Sello:**
`59c5807f2d83c4ff`

## Etapa 2 — Reducir el acoplamiento

**Predicción:**
Si cambio la linea de la vigencia a 1, lo que cambia de comportamiento seria lo siguiente: se afecta el calculo de `vence` en emitir y todo lo que toque esa variable, mas alla de lo que se ve en el scope se veria afectado porque `CONFIG` es global hay mas lugares afectados. Son 4 en legado.py: la linea 66 donde se calcula vence, la 82 donde va al payload de farmauno, la 87 donde va expira en saludtotal, y la 112 donde vence vuelve en el return.

**Observación:**

```
# En PowerShell no sirve pegar Python directo; hay que entrar con: python

(.venv) PS> from clinicasegura.legado import CONFIG, ServicioRecetas
At line:1 char:1
+ from clinicasegura.legado import CONFIG, ServicioRecetas
+ ~~~~
The 'from' keyword is not supported in this version of the language.

>>> from clinicasegura.legado import CONFIG
>>> from datetime import datetime, timedelta
>>> CONFIG["vigencia_dias"] = 1
>>> vence = datetime.now() + timedelta(days=CONFIG["vigencia_dias"])
>>> print(CONFIG["vigencia_dias"])
1
>>> print(vence.isoformat())
2026-09-05T23:01:54.647379

pytest -m etapa2 -q
======================================================================= short test summary info =======================================================================
FAILED pruebas/test_etapa2_acoplamiento.py::test_la_regla_de_negocio_es_una_funcion_pura_de_firma_estrecha - Failed: Falta el módulo «clinicasegura.dominio.reglas».
FAILED pruebas/test_etapa2_acoplamiento.py::test_la_regla_de_negocio_no_tiene_efectos_ni_depende_del_entorno - Failed: Falta el módulo «clinicasegura.dominio.reglas».
FAILED pruebas/test_etapa2_acoplamiento.py::test_el_caso_de_uso_no_recibe_diccionarios_crudos - Failed: Falta el módulo «clinicasegura.dominio.servicio».

python herramientas/marcador.py 2

  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Abraham Solano Parrales   carné 2024132538
  ────────────────────────────────────────────────────────────
  Etapa 2  Acoplamiento                                 █████          verde
  ────────────────────────────────────────────────────────────
  5 pruebas en verde · 0 por resolver
  corrida #4 registrada
  SELLO: ba2ad594476b5705
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.
```

**Explicación:**
Solo hay 1 lectura directa de CONFIG["vigencia_dias"] en legado.py .py:66, pero el acoplamiento hace que 4 lineas cambien: 66 calcula vence, 82 lo manda a farmauno, 87 a saludtotal, 112 lo devuelve al llamador. fallaron 3 pruebas porque faltaban reglas.py y servicio.py. Despues cree calcular_recargo con 3 parametros en reglas.py y EmisionDeRecetas.emitir(receta: Receta, cadena: str) en servicio.py sin globals mutables, y pasaron las 5 pruebas en verde.

**Sello:**
`ba2ad594476b5705`

## Etapa 3 — Abstracción y reuso

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 4 — Flexibilidad, obsolescencia y portabilidad

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 5 — Testabilidad

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 6 — Diseño defensivo

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Cierre — Los principios en conflicto

Nombre dos principios que se estorbaron entre sí en SU rediseño, y con qué
criterio resolvió el conflicto. Cite el archivo donde se ve la decisión.

**Conflicto 1:**

**Conflicto 2:**
