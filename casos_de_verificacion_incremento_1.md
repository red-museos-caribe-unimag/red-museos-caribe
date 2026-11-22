# Casos de verificación – Incremento 1: Crear, registrar y simular

Requisitos: 1 (crear un museo), 2 (registrar los visitantes del día siguiente) y 3 (simular días).

Menú con las opciones 1, 2, 3 y 7. Los casos de este incremento no necesitan el informe: se comprueban con los mensajes del programa. Los casos de simulación que solo se ven en el informe (S01, S07 a S10) se ejecutan en el Incremento 2.

Se ejecutan con `python verificar_casos.py --incremento 1` desde la carpeta del proyecto (o todos con `python verificar_casos.py`). Este documento se genera con `python verificar_casos.py --casos`. Son 39 casos.

**Cómo leer la columna "Se teclea".** Cada tramo separado por ` → ` es una opción del menú: el primer dato es la opción y los siguientes son lo que se teclea en esa opción. `↵` es una entrada vacía. Después de cada opción el programa pide Enter, y al final se elige 7. Los casos que dependen de la fecha de hoy calculan su salida esperada con la fecha del día en que se ejecutan.

| Caso | Qué prueba | Se teclea | La salida debe contener | La salida no debe contener |
|---|---|---|---|---|
| C01 | Caso válido | 1 / Museo del Café / 150 / 2026 / 11 / 1 | `Museo Museo del Café creado, sin días registrados` |  |
| C02 | Aforo 0 | 1 / X / 0 / 2026 / 11 / 1 | `El aforo diario debe ser de al menos un visitante` |  |
| C03 | Aforo negativo | 1 / X / -5 / 2026 / 11 / 1 | `El aforo diario debe ser de al menos un visitante` |  |
| C04 | Aforo mínimo válido | 1 / X / 1 / 2026 / 11 / 1 | `Museo X creado` |  |
| C05 | Aforo no numérico | 1 / X / ciento cincuenta / 2026 / 11 / 1 | `El aforo diario debe ser un número entero` |  |
| C06 | Aforo decimal | 1 / X / 15.5 / 2026 / 11 / 1 | `El aforo diario debe ser un número entero` |  |
| C07 | Nombre vacío | 1 / ↵ / 150 / 2026 / 11 / 1 | `El nombre no puede estar vacío` |  |
| C08 | Nombre de espacios | 1 /     / 150 / 2026 / 11 / 1 | `El nombre no puede estar vacío` |  |
| C09 | Fecha inexistente (31 de noviembre) | 1 / X / 150 / 2026 / 11 / 31 | `La fecha no es válida` |  |
| C10 | Mes no numérico | 1 / X / 150 / 2026 / noviembre / 1 | `La fecha no es válida` |  |
| C11 | 29 de febrero, año no bisiesto | 1 / X / 150 / 2026 / 2 / 29 | `La fecha no es válida` |  |
| C12 | 29 de febrero, año bisiesto | 1 / X / 150 / 2028 / 2 / 29 | `Museo X creado` |  |
| C13 | Año gigante, sin cerrar el programa | 1 / X / 150 / 99999999999 / 1 / 1 | `La fecha no es válida` |  |
| C14 | Solo se avisa la primera condición que falla (aforo antes que fecha) | 1 / X / 0 / 2026 / 11 / 31 | `El aforo diario debe ser de al menos un visitante` | `La fecha no es válida` |
| C15 | Nombre repetido | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 1 / Museo del Café / 150 / 2026 / 11 / 1 | `Ya existe un museo con ese nombre` |  |
| C16 | Nombre repetido con espacios alrededor | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 1 /   Museo del Café   / 150 / 2026 / 11 / 1 | `Ya existe un museo con ese nombre` |  |
| C17 | El nombre se revisa antes que el aforo | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 1 / ↵ / 0 / 2026 / 11 / 1 | `El nombre no puede estar vacío` | `El aforo diario debe ser de al menos un visitante` |
| C18 | Mes 13 | 1 / X / 150 / 2026 / 13 / 1 | `La fecha no es válida` |  |
| C19 | Día 0 | 1 / X / 150 / 2026 / 11 / 0 | `La fecha no es válida` |  |
| C20 | Año 0 | 1 / X / 150 / 0 / 1 / 1 | `La fecha no es válida` |  |
| C21 | Año negativo | 1 / X / 150 / -5 / 1 / 1 | `La fecha no es válida` |  |
| C22 | Último día del calendario | 1 / X / 150 / 9999 / 12 / 31 | `Museo X creado` |  |
| C25 | Aforo con espacios alrededor | 1 / X /  150  / 2026 / 11 / 1 | `Museo X creado` |  |
| R01 | Muestra la fecha del primer día | 1 / Museo del Café / 150 / 2026 / 12 / 30 → 2 / Museo del Café / 60 | `Visitantes del 2026-12-30:` · `Día registrado` |  |
| R02 | Dato no numérico: avisa y vuelve a leer el mismo día | 1 / Museo del Café / 150 / 2026 / 12 / 30 → 2 / Museo del Café / x / 60 | `Los visitantes deben ser un número entero` · `Día registrado` |  |
| R03 | Por encima del aforo | 1 / Museo del Café / 150 / 2026 / 12 / 30 → 2 / Museo del Café / 151 / 60 | `Los visitantes van de 0 a 150` · `Día registrado` |  |
| R04 | Por debajo de 0 | 1 / Museo del Café / 150 / 2026 / 12 / 30 → 2 / Museo del Café / -1 / 60 | `Los visitantes van de 0 a 150` · `Día registrado` |  |
| R05 | Frontera inferior (0) | 1 / Museo del Café / 150 / 2026 / 12 / 30 → 2 / Museo del Café / 0 | `Día registrado` | `van de` |
| R06 | Frontera superior (el aforo) | 1 / Museo del Café / 150 / 2026 / 12 / 30 → 2 / Museo del Café / 150 | `Día registrado` | `van de` |
| R07 | Cambio de año en la fecha del día siguiente | 1 / Museo del Café / 150 / 2026 / 12 / 30 → 2 / Museo del Café / 1 → 2 / Museo del Café / 2 → 2 / Museo del Café / 3 → 2 / Museo del Café / 4 | `Visitantes del 2027-01-02:` |  |
| R08 | Mayúsculas distintas | 1 / Museo del Café / 150 / 2026 / 12 / 30 → 2 / museo del café | `No hay un museo con ese nombre` | `Visitantes del` |
| R09 | Museo inexistente | 1 / Museo del Café / 150 / 2026 / 12 / 30 → 2 / Museo del Banano | `No hay un museo con ese nombre` |  |
| R10 | Se ignoran los espacios del nombre | 1 / Museo del Café / 150 / 2026 / 12 / 30 → 2 /   Museo del Café   / 5 | `Visitantes del 2026-12-30:` · `Día registrado` |  |
| S02 | Días no numéricos: no lee mínimo ni máximo | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / tres | `El número de días debe ser un número entero` | `Visitantes mínimos:` |
| S03 | Cero días | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / 0 | `Se debe simular al menos un día` | `Visitantes mínimos:` |
| S04 | Días negativos | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / -2 | `Se debe simular al menos un día` |  |
| S05 | Mínimo no numérico: no lee el máximo | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / 2 / x | `Los visitantes deben ser un número entero` | `Visitantes máximos:` |
| S06 | Mínimo fuera de rango: no lee el máximo | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Café / 2 / -1 | `Los visitantes van de 0 a 150` | `Visitantes máximos:` |
| S11 | Museo inexistente: no lee días | 1 / Museo del Café / 150 / 2026 / 11 / 1 → 3 / Museo del Banano | `No hay un museo con ese nombre` | `Número de días` |
