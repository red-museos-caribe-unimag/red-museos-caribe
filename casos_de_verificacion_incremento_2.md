# Casos de verificación – Incremento 2: El informe de un museo

Requisitos: 4 (el informe), 5 (desviación estándar), 6 (días de más y de menos visitantes), 7 (niveles), 8 (racha) y 9 (días sin registrar).

Opción 4. Incluye los casos de simulación que se aplazaron del Incremento 1, porque necesitan el informe para ver los días agregados. I01 a I04 se comprueban en el Incremento 4, que es cuando existe la carga de archivos; aquí se pueden comprobar creando el museo y registrando sus días a mano.

Se ejecutan con `python verificar_casos.py --incremento 2` desde la carpeta del proyecto (o todos con `python verificar_casos.py`). Este documento se genera con `python verificar_casos.py --casos`. Son 14 casos.

**Cómo leer la columna "Se teclea".** Cada tramo separado por ` → ` es una opción del menú: el primer dato es la opción y los siguientes son lo que se teclea en esa opción. `↵` es una entrada vacía. Después de cada opción el programa pide Enter, y al final se elige 7. Los casos que dependen de la fecha de hoy calculan su salida esperada con la fecha del día en que se ejecutan.

| Caso | Qué prueba | Se teclea | La salida debe contener | La salida no debe contener |
|---|---|---|---|---|
| S01 | Caso válido: 3 días entre 75 y 150 | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / 3 / 75 / 150 → 4 / Museo del Café | `Días simulados: 3, del 2026-11-01 al 2026-11-03` · `Días registrados: 3` · (la suma de visitantes está entre 225 y 450) |  |
| S07 | Mínimo mayor que máximo: no agrega días | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / 2 / 112 / 75 → 4 / Museo del Café | `El mínimo no puede ser mayor que el máximo` · `El museo no tiene días registrados` |  |
| S08 | Máximo fuera de rango: no agrega días | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / 2 / 0 / 151 → 4 / Museo del Café | `Los visitantes van de 0 a 150` · `El museo no tiene días registrados` |  |
| S09 | Mínimo igual al máximo | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / 2 / 10 / 10 → 4 / Museo del Café | `Días simulados: 2, del 2026-11-01 al 2026-11-02` · `Visitantes totales: 20` |  |
| S10 | 30 días: la última fecha decide si el registro está al día | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / 30 / 0 / 150 → 4 / Museo del Café | `Días simulados: 30, del 2026-11-01 al 2026-11-30` · `El registro está al día` |  |
| I05 | Empates de más y menos visitantes: el primero | 1 / M / 500 / 2026 / 11 / 1 → 2 / M / 250 → 2 / M / 500 → 2 / M / 500 → 2 / M / 100 → 2 / M / 100 → 4 / M | `Día de más visitantes: 2026-11-02` · `Día de menos visitantes: 2026-11-04` |  |
| I06 | La racha más larga, no la primera | 1 / M / 500 / 2026 / 11 / 1 → 2 / M / 120 → 2 / M / 90 → 2 / M / 350 → 2 / M / 140 → 2 / M / 60 → 2 / M / 100 → 2 / M / 420 → 4 / M | `Racha más larga en asistencia baja: 3 días, desde el 2026-11-04` |  |
| I07 | Empate de rachas: la que empezó primero | 1 / M / 500 / 2026 / 11 / 1 → 2 / M / 120 → 2 / M / 90 → 2 / M / 350 → 2 / M / 140 → 2 / M / 60 → 4 / M | `Racha más larga en asistencia baja: 2 días, desde el 2026-11-01` |  |
| I08 | Racha de un día al principio | 1 / M / 500 / 2026 / 11 / 1 → 2 / M / 100 → 2 / M / 350 → 4 / M | `Racha más larga en asistencia baja: 1 día, el 2026-11-01` | `desde el` |
| I09 | Fronteras de nivel (30, 60 y 85 %) | 1 / M / 500 / 2026 / 11 / 1 → 2 / M / 149 → 2 / M / 150 → 2 / M / 299 → 2 / M / 300 → 2 / M / 424 → 2 / M / 425 → 4 / M | `  Baja: 1` · `  Media: 2` · `  Alta: 2` · `  Plena: 1` |  |
| I10 | Días con 0 visitantes | 1 / M / 100 / 2026 / 11 / 1 → 2 / M / 0 → 2 / M / 0 → 4 / M | `Porcentaje de asistencia: 0.0 %` · `Día de más visitantes: 2026-11-01` · `Racha más larga en asistencia baja: 2 días, desde el 2026-11-01` |  |
| I11 | Días sin registrar con un museo atrasado | 1 / A / 100 / 2026 / 11 / 18 → 2 / A / 10 → 4 / A | `Días por registrar: 2, del 2026-11-19 al 2026-11-20` |  |
| I12 | Registro al día: último día registrado ayer | 1 / A / 100 / 2026 / 11 / 20 → 2 / A / 10 → 4 / A | `El registro está al día` | `Días por registrar` |
| I13 | Registro al día: primer día en el futuro | 1 / A / 100 / 2026 / 11 / 26 → 2 / A / 10 → 4 / A | `El registro está al día` | `Días por registrar` |
