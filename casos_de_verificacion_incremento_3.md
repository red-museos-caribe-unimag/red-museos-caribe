# Casos de verificación – Incremento 3: Varios museos y comparación

Requisitos: 10 (varios museos en el mismo programa) y 11 (porcentaje de asistencia más alto y más bajo).

Opción 5. M01 y P01 usan los archivos de datos y se ejecutan en el Incremento 4.

Se ejecutan con `python verificar_casos.py --incremento 3` desde la carpeta del proyecto (o todos con `python verificar_casos.py`). Este documento se genera con `python verificar_casos.py --casos`. Son 7 casos.

**Cómo leer la columna "Se teclea".** Cada tramo separado por ` → ` es una opción del menú: el primer dato es la opción y los siguientes son lo que se teclea en esa opción. `↵` es una entrada vacía. Después de cada opción el programa pide Enter, y al final se elige 7. Los casos que dependen de la fecha de hoy calculan su salida esperada con la fecha del día en que se ejecutan.

| Caso | Qué prueba | Se teclea | La salida debe contener | La salida no debe contener |
|---|---|---|---|---|
| M02 | Museo inexistente en el informe | 6 / datos/museos_completos.csv / datos/visitantes_completos.csv → 4 / Museo del Banano | `No hay un museo con ese nombre` |  |
| M03 | Se distinguen mayúsculas | 6 / datos/museos_completos.csv / datos/visitantes_completos.csv → 4 / museo del mar | `No hay un museo con ese nombre` |  |
| M04 | Se distinguen tildes | 6 / datos/museos_completos.csv / datos/visitantes_completos.csv → 4 / Casa de la Musica | `No hay un museo con ese nombre` |  |
| P02 | Sin museos | 5 | `Ningún museo tiene días registrados` |  |
| P03 | Museos sin días | 1 / A / 100 / 2026 / 11 / 1 → 5 | `Ningún museo tiene días registrados` |  |
| P04 | Empate con 0.0 %: el primero | 1 / A / 100 / 2026 / 11 / 1 → 1 / B / 100 / 2026 / 11 / 1 → 2 / A / 0 → 2 / B / 0 → 5 | `más alto: A, con 0.0 %` · `más bajo: A, con 0.0 %` |  |
| P05 | Un solo museo con días | 1 / A / 100 / 2026 / 11 / 1 → 2 / A / 50 → 5 | `más alto: A, con 50.0 %` · `más bajo: A, con 50.0 %` |  |
