# Diagnóstico del código de partida

Lea `clinicasegura/legado.py` entero antes de escribir una sola línea de
código nuevo. Llene una fila por principio. En la columna de evidencia
cite **archivo y línea** (por ejemplo `legado.py:38`); una fila sin
evidencia no cuenta.

Si cree que un principio **no** está violado, escriba la fila igual y
explique por qué en la columna de hallazgo.

| # | Principio | Hallazgo concreto | Evidencia (archivo:línea) | Qué cuesta si no se corrige |
|---|-----------|-------------------|---------------------------|------------------------------|
| 1 | Dividir y conquistar | La clase ServicioRecetas es una clase Dios que se encarga de realizar todo (valida, reporta, busca pacientes, peticiones, bases de datos y demas)|`legado.py`:44:50:57:137 |Si se tienen tantas responsabilidades dentro de una clase, cualquier cambio podria afectar a otras funciones y puede que estas no esten relacionadas directamente. |
| 2 | Aumentar la cohesión |La clase Dios ServicioRecetas tiene baja cohesion, sus metodos trabjan sobre varias responsabilidades a la vez, mezcla desde la logica del negocio con la persistencia y la exportacion |`legado.py:48-54`-`legado.py:119-135` |Si cada metodo hace cosas de distintos niveles (negocio, red, disco) es dificil saber donde va un cambio y termina uno tocando codigo que no tenia nada que ver con lo que queria arreglar. |
| 3 | Reducir el acoplamiento | Hay variables globales mutables (CONFIG, CACHE_PACIENTES, ULTIMO_ERROR, CONTADOR_EMITIDAS) que cualquier metodo lee o escribe sin que se vea en la firma, es acoplamiento comun | `legado.py:30-41`, `legado.py:72-76`, `legado.py:107` | Si alguien cambia CONFIG desde afuera cambia el comportamiento de todo el modulo y nadie se entera hasta que algo falla. |
| 4 | Mantener alta la abstracción | El metodo reporte() conoce la forma exacta del JSON del proveedor externo (data, attributes, full_name) en vez de trabajar con un tipo del dominio | `legado.py:146-152` | Si el proveedor cambia un campo del JSON hay que buscar en todo el codigo donde se uso esa estructura, impactaria a muchas partes del codigo y su funcionamiento. |
| 5 | Aumentar la reusabilidad | La regla del recargo esta metida adentro de emitir() junto con HTTP y la base de datos, no se puede reusar sola en otro contexto | `legado.py:72-76` | Cada vez que necesite la misma regla en otro lado hay que copiarla o volver a llamar a todo el servicio aunque solo quiera el monto. |
| 6 | Reusar lo existente | validar_cedula() recorre caracter por caracter a mano cuando eso ya lo resuelve una libreria, y el dinero usa float en vez de Decimal | `legado.py:154-167`, `legado.py:63` | Se reinventa la rueda y ademas es mas facil meter bugs en el "parser" que en una biblioteca. |
| 7 | Diseñar para la flexibilidad | Cada farmacia nueva obliga a abrir emitir() y meter otro elif, la variacion vive en un condicional en vez de en un adaptador aparte | `legado.py:79-95` | Agregar una cadena es editar codigo que ya funcionaba y arriesgarse a romper las otras, no cumple abierto/cerrado. |
| 8 | Anticipar la obsolescencia | Las URLs de las farmacias estan hardcodeadas en CONFIG sin failovers o plan de contenciom | `legado.py:30-33` | Cuando una API cambie de version o se apague no hay documentacion de que realizar. |
| 9 | Diseñar para la portabilidad | La base de datos usa ruta /tmp fija y exportar() tiene una ruta de Windows `C:\ClinicaSegura\...` | `legado.py:50`, `legado.py:169` | En otra maquina o SO el codigo falla o escribe donde no debe. |
| 10 | Diseñar para la testabilidad | emitir() llama datetime.now() y random.randint() adentro y abre sqlite en el constructor, imposible probar vigencia o folio sin red ni reloj real | `legado.py:50`, `legado.py:66`, `legado.py:69` | Las pruebas dependen del momento exacto y del azar, o peor tienen que pegarle a la red y a un archivo en disco. |
| 11 | Diseñar defensivamente | Usa assert sobre datos del formulario (se apaga con python -O), devuelve None cuando la cadena no existe, traga excepciones con except: pass y tiene while True sin limite | `legado.py:62-63`, `legado.py:95`, `legado.py:103-104`, `legado.py:121` | En produccion entran datos malos sin que se alerte de ellos. |
