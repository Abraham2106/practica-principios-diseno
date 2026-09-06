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
El "grep" da 7 lineas pero son 4 dataclasses en `modelos.py`. Las importantes del proveedor son `full_name`, `risk_level` y `attributes`. Creo que al terminar esta etapa van a quedar 0 marcas fuera de el adaptador. 
**Observación:**

```
# grep no existe en PowerShell; equivalente en Windows:
# Get-ChildItem -Recurse -Path clinicasegura -Filter *.py | Select-String -Pattern 'data|attributes|full_name|risk_lvl'

grep -rn 'data\|attributes\|full_name\|risk_lvl' clinicasegura/
grep : The term 'grep' is not recognized as the name of a cmdlet, function, script file, or operable program.
At line:1 char:1
+ grep -rn 'data\|attributes\|full_name\|risk_lvl' clinicasegura/
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (grep:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

Get-ChildItem -Recurse -Path clinicasegura -Filter *.py | Select-String -Pattern 'data|attributes|full_name|risk_lvl'

clinicasegura\legado.py:125:                    data=json.dumps(cuerpo).encode("utf-8"),
clinicasegura\legado.py:150:            paciente["data"]["attributes"]["full_name"],
clinicasegura\legado.py:151:            paciente["data"]["attributes"]["risk_lvl"],
clinicasegura\dominio\modelos.py:1:from dataclasses import dataclass
clinicasegura\dominio\modelos.py:6:@dataclass(frozen=True)
clinicasegura\dominio\modelos.py:11:@dataclass(frozen=True)
clinicasegura\dominio\modelos.py:20:@dataclass(frozen=True)

pytest -m etapa3 -q
======================================================================= short test summary info =======================================================================
FAILED pruebas/test_etapa3_abstraccion_reuso.py::test_el_dominio_declara_sus_puertos_como_protocolos - Failed: Falta el módulo «clinicasegura.dominio.puertos».
FAILED pruebas/test_etapa3_abstraccion_reuso.py::test_los_puertos_hablan_el_idioma_del_dominio_y_no_el_del_proveedor - FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\solan\\Downloads\\Practica asincrona - Principios de diseno (estudiantes)\\practica-principios-...
FAILED pruebas/test_etapa3_abstraccion_reuso.py::test_no_se_reinventa_lo_que_la_biblioteca_estandar_ya_resuelve - Failed: Falta el módulo «clinicasegura.aplicacion.borde».
FAILED pruebas/test_etapa3_abstraccion_reuso.py::test_el_folio_y_el_dinero_usan_los_tipos_correctos - AssertionError: Nadie genera folios. Use uuid o secrets desde infraestructura (y random solo si lo inyecta, nunca incrustado en el dominio).

python herramientas/marcador.py 3

  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Abraham Solano Parrales   carné 2024132538
  ────────────────────────────────────────────────────────────
  Etapa 3  Abstracción y reuso                          ███████        verde
  ────────────────────────────────────────────────────────────
  7 pruebas en verde · 0 por resolver
  corrida #5 registrada
  SELLO: 27220fbcb8782e91
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.
```

**Explicación:**
fallaron 4 pruebas porque faltaban puertos.py, borde.py y folios con uuid. Cree los 4 Protocol en puertos.py (Pasarela, Reloj, GeneradorFolio, Bitacora), borde.py vacio para que importe, validar_cedula con re en modelos.py y folios.py con uuid en infraestructura. Pasaron las 7 pruebas. full_name y attributes solo siguen en legado.py que ya nadie importa.

**Sello:**
`27220fbcb8782e91`

## Etapa 4 — Flexibilidad, obsolescencia y portabilidad

**Predicción:**
Va a fallar porque hay `if's` en el codigo aun. Como dice la desc, que si hay if's porque mi servicio aun no tiene registro / tiene NotImplementedError / menciona farmauno en un if. 
**Observación:**

```
pytest -m etapa4 -q
=============================================================================== short test summary info ===============================================================================
FAILED pruebas/test_etapa4_flexibilidad.py::test_se_agrega_una_cadena_nueva_sin_tocar_el_servicio - Failed: Falta el módulo «clinicasegura.infraestructura.registro».
FAILED pruebas/test_etapa4_flexibilidad.py::test_una_cadena_desconocida_lanza_un_error_de_dominio - TypeError: EmisionDeRecetas() takes no arguments
FAILED pruebas/test_etapa4_flexibilidad.py::test_la_configuracion_entra_por_el_entorno - Failed: Falta el módulo «clinicasegura.arranque».
FAILED pruebas/test_etapa4_flexibilidad.py::test_existe_la_tabla_de_obsolescencia_de_dependencias - AssertionError: Filas incompletas en DEPENDENCIAS.md: pytest, pydantic,
4 failed, 3 passed, 77 deselected in 0.43s

python herramientas/marcador.py 4

  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Abraham Solano Parrales   carné 2024132538
  ────────────────────────────────────────────────────────────
  Etapa 4  Flexibilidad · obsolescencia · portabilidad  ███████        verde
  ────────────────────────────────────────────────────────────
  7 pruebas en verde · 0 por resolver
  corrida #6 registrada
  SELLO: 64f81da5c505ccb9
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.
```

**Explicación:**
Al principio fallaron 4 porque faltaban registro.py, arranque.py, el constructor de EmisionDeRecetas y DEPENDENCIAS.md vacio. Cree construir_registro en infraestructura, servicio con pasarelas/reloj/folios/bitacora sin ifs por cadena, arranque con getenv y la tabla de dependencias. Pasaron las 7 incluyendo FarmaViva sin tocar servicio.py otra vez.

**Sello:**
`64f81da5c505ccb9`

## Etapa 5 — Testabilidad

**Predicción:**
Predigo que el legado se va a demorar un buen rato o pegarle a la red porque emitir abre sqlite y hace post con while True. Tambien que el folio sale random y http puede salir -1 si la farmacia no responde. Para probar solo el recargo tuve que meterle a todo eso, no a una linea.

**Observación:**

```
>>> from clinicasegura.legado import ServicioRecetas
>>> s = ServicioRecetas()
>>> s.emitir({"cedula": "1-1234-5678", "dias": 30, "dosis_mg": 500}, "farmauno")
{'folio': '541857', 'vence': '2026-10-05T22:14:23.764429', 'recargo': 7500, 'http': -1, 'cadena': 'farmauno'}

python herramientas/marcador.py 5

  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Abraham Solano Parrales   carné 2024132538
  ────────────────────────────────────────────────────────────
  Etapa 5  Testabilidad                                 ███████        verde
  ────────────────────────────────────────────────────────────
  7 pruebas en verde · 0 por resolver
  corrida #8 registrada
  SELLO: 9b970a6270fe479a
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.
```

**Explicación:**
Paso lo que predije: http -1 porque la farmacia no respondio bien, folio random (541857) y recargo 7500 mezclado con red y sqlite. En el rediseno el servicio ya recibe pasarelas reloj folios y bitacora por constructor y la vigencia sale del reloj inyectado. Escribi 4 pruebas en mis_pruebas/ (reloj fijo, cadena caida, cedula mala, folio sin random) con ayuda de IA para el esqueleto pero las corri yo.

**Sello:**
`9b970a6270fe479a`

## Etapa 6 — Diseño defensivo

**Predicción:**
Predigo que la primera corrida revienta con AssertionError en dias=0 porque el legado usa assert sobre datos del formulario. La segunda con python -O no corre ese assert, sigue adelante, abre sqlite, pega al post de farmauno y se queda colgado o tarda un buen rato por el while True del _post.

**Observación:**

```
python -c "from clinicasegura.legado import ServicioRecetas as S; S().emitir({'cedula':'x','dias':0,'dosis_mg':1}, 'farmauno')"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "C:\Users\solan\Downloads\Practica asincrona - Principios de diseno (estudiantes)\practica-principios-diseno\clinicasegura\legado.py", line 62, in emitir
    assert datos["dias"] > 0, "los dias deben ser positivos"
AssertionError: los dias deben ser positivos

python -O -c "from clinicasegura.legado import ServicioRecetas as S; S().emitir({'cedula':'x','dias':0,'dosis_mg':1}, 'farmauno')"
(se queda colgado: sin assert pasa la validacion, intenta HTTP en bucle while True)

pytest -m etapa6 -q
...........
11 passed

python herramientas/marcador.py 6

  MARCADOR DE LA PRÁCTICA · Principios de diseño
  Abraham Solano Parrales   carné 2024132538
  ────────────────────────────────────────────────────────────
  Etapa 6  Diseño defensivo                             ███████████   verde
  ────────────────────────────────────────────────────────────
  11 pruebas en verde · 0 por resolver
  corrida #9 registrada
  SELLO: 73dcea8735afcdb8
  Cópielo en la entrada de BITACORA.md de la etapa que acaba de cerrar.
```

**Explicación:**
Paso lo que predije, la primera revienta con AssertionError en dias=0 y la segunda con -O no corre ese assert, sigue y se cuelga un rato en el post. En el rediseno el borde parsea afuera con SolicitudReceta (pydantic, extra forbid, frozen) y a_receta devuelve Receta del dominio; si algo viene mal lanza RecetaInvalida, no assert. En servicio si la pasarela tira TimeoutError registro en bitacora y lanzo FarmaciaNoDisponible con cadena y folio para no fallar en silencio.

**Sello:**
`73dcea8735afcdb8`

## Cierre — Los principios en conflicto

Nombre dos principios que se estorbaron entre sí en SU rediseño, y con qué
criterio resolvió el conflicto. Cite el archivo donde se ve la decisión.

**Conflicto 1:**

**Conflicto 2:**
