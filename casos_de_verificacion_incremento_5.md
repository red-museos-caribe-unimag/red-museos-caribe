# Casos de verificación – Incremento 5: Menú, verificación ampliada y cierre

Requisitos: 14 (el menú) y los casos nuevos de la verificación ampliada.

Opción 7 y los avisos para opciones no válidas. Los casos C23, C24, C26, R11, R12, S12, S13, S14 e I14 son los que pusieron en evidencia los tres comportamientos que se corrigieron: enteros con guion bajo, cierre del programa en el año 9999 y días a simular enormes.

Se ejecutan con `python verificar_casos.py --incremento 5` desde la carpeta del proyecto (o todos con `python verificar_casos.py`). Este documento se genera con `python verificar_casos.py --casos`. Son 14 casos.

**Cómo leer la columna "Se teclea".** Cada tramo separado por ` → ` es una opción del menú: el primer dato es la opción y los siguientes son lo que se teclea en esa opción. `↵` es una entrada vacía. Después de cada opción el programa pide Enter, y al final se elige 7. Los casos que dependen de la fecha de hoy calculan su salida esperada con la fecha del día en que se ejecutan.

| Caso | Qué prueba | Se teclea | La salida debe contener | La salida no debe contener |
|---|---|---|---|---|
| C23 | Aforo con guion bajo (1_000) | 1 / X / 1_000 / 2026 / 11 / 1 | `El aforo diario debe ser un número entero` | `creado` |
| C24 | Aforo con dígito de otro alfabeto | 1 / X / ٣ / 2026 / 11 / 1 | `El aforo diario debe ser un número entero` | `creado` |
| C26 | Año con guion bajo (2_026) | 1 / X / 150 / 2_026 / 11 / 1 | `La fecha no es válida` |  |
| R11 | Visitantes con guion bajo | 1 / Museo del Café / 5000 / 2026 / 12 / 30 → 2 / Museo del Café / 1_000 / 10 | `Los visitantes deben ser un número entero` · `Día registrado` |  |
| R12 | Último día del calendario: el segundo día no se puede registrar | 1 / Fin / 100 / 9999 / 12 / 31 → 2 / Fin / 5 → 2 / Fin | `Visitantes del 9999-12-31:` · `Día registrado` · `El registro no puede pasar del 31 de diciembre de 9999` |  |
| S12 | Días con guion bajo | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / 1_000 | `El número de días debe ser un número entero` |  |
| S13 | Pasar del último día del calendario no agrega nada; después sí cabe | 1 / Fin / 100 / 9999 / 12 / 30 → 3 / Fin / 3 / 0 / 100 → 4 / Fin → 3 / Fin / 2 / 0 / 100 | `El registro no puede pasar del 31 de diciembre de 9999` · `El museo no tiene días registrados` · `Días simulados: 2, del 9999-12-30 al 9999-12-31` |  |
| S14 | Cantidad de días enorme | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / 1000000000 / 0 / 100 | `El registro no puede pasar del 31 de diciembre de 9999` |  |
| I14 | Último día del calendario registrado: el informe no se cierra | 1 / Fin / 100 / 9999 / 12 / 31 → 2 / Fin / 5 → 4 / Fin | `Último día registrado: 9999-12-31` · `El registro está al día` |  |
| U01 | Opción fuera de rango | 8 | `La opción no es válida` |  |
| U02 | Opción de texto | dos | `La opción no es válida` |  |
| U03 | Opción vacía | ↵ | `La opción no es válida` |  |
| U04 | Opción 0 | 0 | `La opción no es válida` |  |
| U05 | Salir termina sin errores | (solo salir) | `Red de Museos del Caribe` |  |
