# Dependencias externas

Una fila por dependencia externa que el proyecto usa hoy, incluidas las de
la practica. Complete las cuatro columnas: sin ruta de salida, la
dependencia es un compromiso indefinido.

| Dependencia | Versión acotada | Licencia | Riesgo | Ruta de salida |
|-------------|-----------------|----------|--------|----------------|
| pytest | >=8.0 | MIT | bajo, solo lo uso para correr tests | subir version si el curso pide otra minima |
| pydantic | >=2.6 | MIT | medio, capaz cambia la API en v3 | esperar a v3 estable y migrar el borde cuando toque |
| urllib | viene con python 3.12 | PSF | bajo, es stdlib | si urllib no alcanza cambiar a httpx |
