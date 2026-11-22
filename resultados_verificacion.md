# Resultados de la verificación

Ejecutado el 2026-11-22 21:47 UTC (fecha de referencia para casos dependientes del día: 2026-11-22).
Procedencia: ejecución automatizada local conservada en el entorno de comprobación. No atribuida a un integrante del equipo.

| Caso | Qué prueba | Resultado obtenido |
|---|---|---|
| C01 | Caso válido | OK |
| C02 | Aforo 0 | OK |
| C03 | Aforo negativo | OK |
| C04 | Aforo mínimo válido | OK |
| C05 | Aforo no numérico | OK |
| C06 | Aforo decimal | OK |
| C07 | Nombre vacío | OK |
| C08 | Nombre de espacios | OK |
| C09 | Fecha inexistente (31 de noviembre) | OK |
| C10 | Mes no numérico | OK |
| C11 | 29 de febrero, año no bisiesto | OK |
| C12 | 29 de febrero, año bisiesto | OK |
| C13 | Año gigante, sin cerrar el programa | OK |
| C14 | Solo se avisa la primera condición que falla (aforo antes que fecha) | OK |
| C15 | Nombre repetido | OK |
| C16 | Nombre repetido con espacios alrededor | OK |
| C17 | El nombre se revisa antes que el aforo | OK |
| C18 | Mes 13 | OK |
| C19 | Día 0 | OK |
| C20 | Año 0 | OK |
| C21 | Año negativo | OK |
| C22 | Último día del calendario | OK |
| C23 | Aforo con guion bajo (1_000) | OK |
| C24 | Aforo con dígito de otro alfabeto | OK |
| C25 | Aforo con espacios alrededor | OK |
| C26 | Año con guion bajo (2_026) | OK |
| R01 | Muestra la fecha del primer día | OK |
| R02 | Dato no numérico: avisa y vuelve a leer el mismo día | OK |
| R03 | Por encima del aforo | OK |
| R04 | Por debajo de 0 | OK |
| R05 | Frontera inferior (0) | OK |
| R06 | Frontera superior (el aforo) | OK |
| R07 | Cambio de año en la fecha del día siguiente | OK |
| R08 | Mayúsculas distintas | OK |
| R09 | Museo inexistente | OK |
| R10 | Se ignoran los espacios del nombre | OK |
| R11 | Visitantes con guion bajo | OK |
| R12 | Último día del calendario: el segundo día no se puede registrar | OK |
| S01 | Caso válido: 3 días entre 75 y 150 | OK |
| S02 | Días no numéricos: no lee mínimo ni máximo | OK |
| S03 | Cero días | OK |
| S04 | Días negativos | OK |
| S05 | Mínimo no numérico: no lee el máximo | OK |
| S06 | Mínimo fuera de rango: no lee el máximo | OK |
| S07 | Mínimo mayor que máximo: no agrega días | OK |
| S08 | Máximo fuera de rango: no agrega días | OK |
| S09 | Mínimo igual al máximo | OK |
| S10 | 30 días: la última fecha decide si el registro está al día | OK |
| S11 | Museo inexistente: no lee días | OK |
| S12 | Días con guion bajo | OK |
| S13 | Pasar del último día del calendario no agrega nada; después sí cabe | OK |
| S14 | Cantidad de días enorme | OK |
| I01 | Museo del Mar: ejemplo del enunciado (req. 4 a 9 y 11 de días sin registrar) | OK |
| I02 | Casa de la Música: ejemplo del enunciado, racha de un día | OK |
| I03 | Galería del Puerto sin días | OK |
| I04 | Un solo día, sin racha | OK |
| I05 | Empates de más y menos visitantes: el primero | OK |
| I06 | La racha más larga, no la primera | OK |
| I07 | Empate de rachas: la que empezó primero | OK |
| I08 | Racha de un día al principio | OK |
| I09 | Fronteras de nivel (30, 60 y 85 %) | OK |
| I10 | Días con 0 visitantes | OK |
| I11 | Días sin registrar con un museo atrasado | OK |
| I12 | Registro al día: último día registrado ayer | OK |
| I13 | Registro al día: primer día en el futuro | OK |
| I14 | Último día del calendario registrado: el informe no se cierra | OK |
| M01 | Cada museo con sus datos | OK |
| M02 | Museo inexistente en el informe | OK |
| M03 | Se distinguen mayúsculas | OK |
| M04 | Se distinguen tildes | OK |
| P01 | Ejemplo del enunciado; la Galería sin días no entra | OK |
| P02 | Sin museos | OK |
| P03 | Museos sin días | OK |
| P04 | Empate con 0.0 %: el primero | OK |
| P05 | Un solo museo con días | OK |
| A01 | Ejemplo del enunciado: museos y visitantes con líneas descartadas | OK |
| A03 | Archivo de museos inexistente: no pide la ruta de visitantes | OK |
| A04 | Archivo de visitantes inexistente: los museos se quedan sin días | OK |
| A05 | Cargar con un museo creado: no pide rutas | OK |
| A06 | Segunda carga: no duplica los días | OK |
| A07 | Carga sin líneas descartadas | OK |
| A08 | Archivos guardados desde Excel (BOM, \r\n, espacios, líneas vacías) | OK |
| A09 | Archivo en Latin-1 | OK |
| A10 | Archivo con solo el encabezado | OK |
| A11 | Archivo vacío | OK |
| A12 | Rutas entre comillas y con espacios | OK |
| A13 | La ruta es una carpeta | OK |
| A14 | Después de cargar, el registro sigue desde el teclado | OK |
| A15 | Los museos cargados cuentan para los nombres repetidos | OK |
| A16 | Líneas vacías en el archivo de visitantes: se saltan y el número de línea no se corre | OK |
| U01 | Opción fuera de rango | OK |
| U02 | Opción de texto | OK |
| U03 | Opción vacía | OK |
| U04 | Opción 0 | OK |
| U05 | Salir termina sin errores | OK |

Total: 95 casos, 95 OK, 0 con falla.
