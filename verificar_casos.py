"""Ejecuta los casos de verificación sobre user_interface.py y compara la salida.

Uso (desde la carpeta del proyecto):  python verificar_casos.py
Escribe el resultado en resultados_verificacion.md.
Cada caso es una lista de "bloques": un bloque es lo que se teclea en una opción
del menú. Después de cada bloque el programa pide Enter, y al final se teclea 7.
"""
import re
import subprocess
import sys
from datetime import date, datetime, timedelta

HOY = date.today()
AYER = HOY - timedelta(days=1)
NO_HAY = "No hay un museo con ese nombre"
AFORO_ENTERO = "El aforo diario debe ser un número entero"
AFORO_MIN = "El aforo diario debe ser de al menos un visitante"
FECHA = "La fecha no es válida"
FIN = "El registro no puede pasar del 31 de diciembre de 9999"
VIS_ENTERO = "Los visitantes deben ser un número entero"
CARGA_CON_MUSEOS = "La carga solo se hace con el programa sin museos"
SIN_ARCHIVO = "El archivo no existe"

casos = []


def caso(id_, que_prueba, bloques, debe=(), no_debe=(), revisar=None):
    casos.append((id_, que_prueba, bloques, list(debe), list(no_debe), revisar))


def crear(nombre, aforo, anio, mes, dia):
    return ["1", nombre, str(aforo), str(anio), str(mes), str(dia)]


def registrar(nombre, *valores):
    return [["2", nombre, str(v)] for v in valores]


def informe(nombre):
    return ["4", nombre]


def cargar(ruta_museos, ruta_visitantes=None):
    bloque = ["6", ruta_museos]
    if ruta_visitantes is not None:
        bloque.append(ruta_visitantes)
    return bloque


def pendientes(siguiente):
    # Lo que debe decir el informe sobre los días sin registrar, según la fecha de hoy.
    faltan = (HOY - siguiente).days
    if faltan <= 0:
        return "El registro está al día"
    return f"Días por registrar: {faltan}, del {siguiente} al {AYER}"


CARGA_COMPLETA = cargar("datos/museos_completos.csv", "datos/visitantes_completos.csv")
CAFE = "Museo del Café"

# ---------- Req. 1: crear un museo ----------
caso("C01", "Caso válido", [crear(CAFE, 150, 2026, 11, 1)], [f"Museo {CAFE} creado, sin días registrados"])
caso("C02", "Aforo 0", [crear("X", 0, 2026, 11, 1)], [AFORO_MIN])
caso("C03", "Aforo negativo", [crear("X", -5, 2026, 11, 1)], [AFORO_MIN])
caso("C04", "Aforo mínimo válido", [crear("X", 1, 2026, 11, 1)], ["Museo X creado"])
caso("C05", "Aforo no numérico", [crear("X", "ciento cincuenta", 2026, 11, 1)], [AFORO_ENTERO])
caso("C06", "Aforo decimal", [crear("X", "15.5", 2026, 11, 1)], [AFORO_ENTERO])
caso("C07", "Nombre vacío", [crear("", 150, 2026, 11, 1)], ["El nombre no puede estar vacío"])
caso("C08", "Nombre de espacios", [crear("   ", 150, 2026, 11, 1)], ["El nombre no puede estar vacío"])
caso("C09", "Fecha inexistente (31 de noviembre)", [crear("X", 150, 2026, 11, 31)], [FECHA])
caso("C10", "Mes no numérico", [crear("X", 150, 2026, "noviembre", 1)], [FECHA])
caso("C11", "29 de febrero, año no bisiesto", [crear("X", 150, 2026, 2, 29)], [FECHA])
caso("C12", "29 de febrero, año bisiesto", [crear("X", 150, 2028, 2, 29)], ["Museo X creado"])
caso("C13", "Año gigante, sin cerrar el programa", [crear("X", 150, 99999999999, 1, 1)], [FECHA])
caso("C14", "Solo se avisa la primera condición que falla (aforo antes que fecha)",
     [crear("X", 0, 2026, 11, 31)], [AFORO_MIN], [FECHA])
caso("C15", "Nombre repetido", [crear(CAFE, 150, 2026, 11, 1), crear(CAFE, 150, 2026, 11, 1)],
     ["Ya existe un museo con ese nombre"])
caso("C16", "Nombre repetido con espacios alrededor",
     [crear(CAFE, 150, 2026, 11, 1), crear("  " + CAFE + "  ", 150, 2026, 11, 1)],
     ["Ya existe un museo con ese nombre"])
caso("C17", "El nombre se revisa antes que el aforo",
     [crear(CAFE, 150, 2026, 11, 1), crear("", 0, 2026, 11, 1)],
     ["El nombre no puede estar vacío"], [AFORO_MIN])
caso("C18", "Mes 13", [crear("X", 150, 2026, 13, 1)], [FECHA])
caso("C19", "Día 0", [crear("X", 150, 2026, 11, 0)], [FECHA])
caso("C20", "Año 0", [crear("X", 150, 0, 1, 1)], [FECHA])
caso("C21", "Año negativo", [crear("X", 150, -5, 1, 1)], [FECHA])
caso("C22", "Último día del calendario", [crear("X", 150, 9999, 12, 31)], ["Museo X creado"])
caso("C23", "Aforo con guion bajo (1_000)", [crear("X", "1_000", 2026, 11, 1)], [AFORO_ENTERO], ["creado"])
caso("C24", "Aforo con dígito de otro alfabeto", [crear("X", "٣", 2026, 11, 1)], [AFORO_ENTERO], ["creado"])
caso("C25", "Aforo con espacios alrededor", [crear("X", " 150 ", 2026, 11, 1)], ["Museo X creado"])
caso("C26", "Año con guion bajo (2_026)", [crear("X", 150, "2_026", 11, 1)], [FECHA])

# ---------- Req. 2: registrar el día siguiente ----------
BASE_R = crear(CAFE, 150, 2026, 12, 30)
caso("R01", "Muestra la fecha del primer día", [BASE_R, ["2", CAFE, "60"]],
     ["Visitantes del 2026-12-30:", "Día registrado"])
caso("R02", "Dato no numérico: avisa y vuelve a leer el mismo día", [BASE_R, ["2", CAFE, "x", "60"]],
     [VIS_ENTERO, "Día registrado"])
caso("R03", "Por encima del aforo", [BASE_R, ["2", CAFE, "151", "60"]],
     ["Los visitantes van de 0 a 150", "Día registrado"])
caso("R04", "Por debajo de 0", [BASE_R, ["2", CAFE, "-1", "60"]],
     ["Los visitantes van de 0 a 150", "Día registrado"])
caso("R05", "Frontera inferior (0)", [BASE_R, ["2", CAFE, "0"]], ["Día registrado"], ["van de"])
caso("R06", "Frontera superior (el aforo)", [BASE_R, ["2", CAFE, "150"]], ["Día registrado"], ["van de"])
caso("R07", "Cambio de año en la fecha del día siguiente",
     [BASE_R] + registrar(CAFE, 1, 2, 3) + [["2", CAFE, "4"]], ["Visitantes del 2027-01-02:"])
caso("R08", "Mayúsculas distintas", [BASE_R, ["2", "museo del café"]], [NO_HAY], ["Visitantes del"])
caso("R09", "Museo inexistente", [BASE_R, ["2", "Museo del Banano"]], [NO_HAY])
caso("R10", "Se ignoran los espacios del nombre", [BASE_R, ["2", "  " + CAFE + "  ", "5"]],
     ["Visitantes del 2026-12-30:", "Día registrado"])
caso("R11", "Visitantes con guion bajo", [crear(CAFE, 5000, 2026, 12, 30), ["2", CAFE, "1_000", "10"]],
     [VIS_ENTERO, "Día registrado"])
caso("R12", "Último día del calendario: el segundo día no se puede registrar",
     [crear("Fin", 100, 9999, 12, 31), ["2", "Fin", "5"], ["2", "Fin"]],
     ["Visitantes del 9999-12-31:", "Día registrado", FIN])

# ---------- Req. 3: simular días ----------
BASE_S = crear(CAFE, 150, 2026, 11, 1)


def revisar_s01(salida):
    total = int(re.search(r"Visitantes totales: (\d+)", salida).group(1))
    return 225 <= total <= 450


caso("S01", "Caso válido: 3 días entre 75 y 150", [BASE_S, ["3", CAFE, "3", "75", "150"], informe(CAFE)],
     ["Días simulados: 3, del 2026-11-01 al 2026-11-03", "Días registrados: 3"], revisar=revisar_s01)
caso("S02", "Días no numéricos: no lee mínimo ni máximo", [BASE_S, ["3", CAFE, "tres"]],
     ["El número de días debe ser un número entero"], ["Visitantes mínimos:"])
caso("S03", "Cero días", [BASE_S, ["3", CAFE, "0"]], ["Se debe simular al menos un día"], ["Visitantes mínimos:"])
caso("S04", "Días negativos", [BASE_S, ["3", CAFE, "-2"]], ["Se debe simular al menos un día"])
caso("S05", "Mínimo no numérico: no lee el máximo", [BASE_S, ["3", CAFE, "2", "x"]],
     [VIS_ENTERO], ["Visitantes máximos:"])
caso("S06", "Mínimo fuera de rango: no lee el máximo", [BASE_S, ["3", CAFE, "2", "-1"]],
     ["Los visitantes van de 0 a 150"], ["Visitantes máximos:"])
caso("S07", "Mínimo mayor que máximo: no agrega días", [BASE_S, ["3", CAFE, "2", "112", "75"], informe(CAFE)],
     ["El mínimo no puede ser mayor que el máximo", "El museo no tiene días registrados"])
caso("S08", "Máximo fuera de rango: no agrega días", [BASE_S, ["3", CAFE, "2", "0", "151"], informe(CAFE)],
     ["Los visitantes van de 0 a 150", "El museo no tiene días registrados"])
caso("S09", "Mínimo igual al máximo", [BASE_S, ["3", CAFE, "2", "10", "10"], informe(CAFE)],
     ["Días simulados: 2, del 2026-11-01 al 2026-11-02", "Visitantes totales: 20"])
caso("S10", "30 días: la última fecha decide si el registro está al día",
     [BASE_S, ["3", CAFE, "30", "0", "150"], informe(CAFE)],
     ["Días simulados: 30, del 2026-11-01 al 2026-11-30", pendientes(date(2026, 12, 1))])
caso("S11", "Museo inexistente: no lee días", [BASE_S, ["3", "Museo del Banano"]], [NO_HAY], ["Número de días"])
caso("S12", "Días con guion bajo", [BASE_S, ["3", CAFE, "1_000"]],
     ["El número de días debe ser un número entero"])
caso("S13", "Pasar del último día del calendario no agrega nada; después sí cabe",
     [crear("Fin", 100, 9999, 12, 30), ["3", "Fin", "3", "0", "100"], informe("Fin"), ["3", "Fin", "2", "0", "100"]],
     [FIN, "El museo no tiene días registrados", "Días simulados: 2, del 9999-12-30 al 9999-12-31"])
caso("S14", "Cantidad de días enorme", [BASE_S, ["3", CAFE, "1000000000", "0", "100"]], [FIN])

# ---------- Req. 4 a 9: el informe ----------
INF_MAR = ["Museo: Museo del Mar", "Aforo diario: 500", "Días registrados: 5", "Visitantes totales: 1420",
           "Promedio de visitantes por día: 284.0", "Porcentaje de asistencia: 56.8 %",
           "Desviación estándar de los visitantes: 145.68", "Día de más visitantes: 2026-11-04",
           "Día de menos visitantes: 2026-11-03", "  Baja: 2", "  Media: 0", "  Alta: 2", "  Plena: 1",
           "Racha más larga en asistencia baja: 2 días, desde el 2026-11-02",
           "Último día registrado: 2026-11-05", pendientes(date(2026, 11, 6))]
INF_CASA = ["Visitantes totales: 440", "Promedio de visitantes por día: 110.0", "Porcentaje de asistencia: 55.0 %",
            "Desviación estándar de los visitantes: 49.5", "Día de más visitantes: 2026-11-04",
            "Día de menos visitantes: 2026-11-01", "  Baja: 1", "  Media: 1", "  Alta: 1", "  Plena: 1",
            "Racha más larga en asistencia baja: 1 día, el 2026-11-01"]


def con_valores(aforo, valores, nombre="M"):
    return [crear(nombre, aforo, 2026, 11, 1)] + registrar(nombre, *valores) + [informe(nombre)]


caso("I01", "Museo del Mar: ejemplo del enunciado (req. 4 a 9 y 11 de días sin registrar)",
     [CARGA_COMPLETA, informe("Museo del Mar")], INF_MAR)
caso("I02", "Casa de la Música: ejemplo del enunciado, racha de un día",
     [CARGA_COMPLETA, informe("Casa de la Música")], INF_CASA)
caso("I03", "Galería del Puerto sin días", [CARGA_COMPLETA, informe("Galería del Puerto")],
     ["Aforo diario: 100", "El museo no tiene días registrados"], ["Días registrados:"])
caso("I04", "Un solo día, sin racha", [CARGA_COMPLETA, informe(CAFE)],
     ["Promedio de visitantes por día: 60.0", "Porcentaje de asistencia: 40.0 %",
      "Desviación estándar de los visitantes: 0.0", "Día de más visitantes: 2026-11-01",
      "Día de menos visitantes: 2026-11-01", "El museo no tuvo ningún día en asistencia baja"])
caso("I05", "Empates de más y menos visitantes: el primero", con_valores(500, [250, 500, 500, 100, 100]),
     ["Día de más visitantes: 2026-11-02", "Día de menos visitantes: 2026-11-04"])
caso("I06", "La racha más larga, no la primera", con_valores(500, [120, 90, 350, 140, 60, 100, 420]),
     ["Racha más larga en asistencia baja: 3 días, desde el 2026-11-04"])
caso("I07", "Empate de rachas: la que empezó primero", con_valores(500, [120, 90, 350, 140, 60]),
     ["Racha más larga en asistencia baja: 2 días, desde el 2026-11-01"])
caso("I08", "Racha de un día al principio", con_valores(500, [100, 350]),
     ["Racha más larga en asistencia baja: 1 día, el 2026-11-01"], ["desde el"])
caso("I09", "Fronteras de nivel (30, 60 y 85 %)", con_valores(500, [149, 150, 299, 300, 424, 425]),
     ["  Baja: 1", "  Media: 2", "  Alta: 2", "  Plena: 1"])
caso("I10", "Días con 0 visitantes", con_valores(100, [0, 0]),
     ["Porcentaje de asistencia: 0.0 %", "Día de más visitantes: 2026-11-01",
      "Racha más larga en asistencia baja: 2 días, desde el 2026-11-01"])
caso("I11", "Días sin registrar con un museo atrasado",
     [crear("A", 100, HOY.year, HOY.month, HOY.day)] if False else
     [crear("A", 100, (HOY - timedelta(days=3)).year, (HOY - timedelta(days=3)).month, (HOY - timedelta(days=3)).day),
      ["2", "A", "10"], informe("A")], [pendientes(HOY - timedelta(days=2))])
caso("I12", "Registro al día: último día registrado ayer",
     [crear("A", 100, AYER.year, AYER.month, AYER.day), ["2", "A", "10"], informe("A")],
     ["El registro está al día"], ["Días por registrar"])
caso("I13", "Registro al día: primer día en el futuro",
     [crear("A", 100, (HOY + timedelta(days=5)).year, (HOY + timedelta(days=5)).month, (HOY + timedelta(days=5)).day),
      ["2", "A", "10"], informe("A")], ["El registro está al día"], ["Días por registrar"])
caso("I14", "Último día del calendario registrado: el informe no se cierra",
     [crear("Fin", 100, 9999, 12, 31), ["2", "Fin", "5"], informe("Fin")],
     ["Último día registrado: 9999-12-31", "El registro está al día"])

# ---------- Req. 10: varios museos ----------
caso("M01", "Cada museo con sus datos", [CARGA_COMPLETA, informe("Museo del Mar"), informe("Casa de la Música")],
     INF_MAR + INF_CASA)
caso("M02", "Museo inexistente en el informe", [CARGA_COMPLETA, informe("Museo del Banano")], [NO_HAY])
caso("M03", "Se distinguen mayúsculas", [CARGA_COMPLETA, informe("museo del mar")], [NO_HAY])
caso("M04", "Se distinguen tildes", [CARGA_COMPLETA, informe("Casa de la Musica")], [NO_HAY])

# ---------- Req. 11: más alto y más bajo ----------
caso("P01", "Ejemplo del enunciado; la Galería sin días no entra", [CARGA_COMPLETA, ["5"]],
     ["más alto: Museo del Mar, con 56.8 %", "más bajo: Museo del Café, con 40.0 %"])
caso("P02", "Sin museos", [["5"]], ["Ningún museo tiene días registrados"])
caso("P03", "Museos sin días", [crear("A", 100, 2026, 11, 1), ["5"]], ["Ningún museo tiene días registrados"])
caso("P04", "Empate con 0.0 %: el primero", [crear("A", 100, 2026, 11, 1), crear("B", 100, 2026, 11, 1)]
     + registrar("A", 0) + registrar("B", 0) + [["5"]],
     ["más alto: A, con 0.0 %", "más bajo: A, con 0.0 %"])
caso("P05", "Un solo museo con días", [crear("A", 100, 2026, 11, 1)] + registrar("A", 50) + [["5"]],
     ["más alto: A, con 50.0 %", "más bajo: A, con 50.0 %"])

# ---------- Req. 12 y 13: archivos ----------
caso("A01", "Ejemplo del enunciado: museos y visitantes con líneas descartadas",
     [cargar("datos/museos.csv", "datos/visitantes.csv"), informe("Museo del Mar"), informe("Casa de la Música")],
     ["Línea 4 descartada. " + AFORO_MIN, "Línea 5 descartada. La línea no tiene cinco campos",
      "Línea 6 descartada. " + AFORO_ENTERO, "Línea 7 descartada. Ya existe un museo con ese nombre",
      "Línea 8 descartada. " + FECHA, "Museos cargados: 2",
      "Línea 10 descartada. Los visitantes van de 0 a 200", "Línea 12 descartada. " + NO_HAY,
      "Línea 13 descartada. Los visitantes van de 0 a 500", "Línea 14 descartada. " + VIS_ENTERO,
      "Línea 15 descartada. La línea no tiene dos campos", "Días cargados: 9"] + INF_MAR[:13] + INF_CASA)
caso("A03", "Archivo de museos inexistente: no pide la ruta de visitantes",
     [cargar("datos/no_existe.csv")], [SIN_ARCHIVO], ["Ruta del archivo de visitantes"])
caso("A04", "Archivo de visitantes inexistente: los museos se quedan sin días",
     [cargar("datos/museos.csv", "datos/no_existe.csv"), informe("Museo del Mar")],
     ["Museos cargados: 2", SIN_ARCHIVO, "El museo no tiene días registrados"])
caso("A05", "Cargar con un museo creado: no pide rutas", [crear("A", 100, 2026, 11, 1), ["6"]],
     [CARGA_CON_MUSEOS], ["Ruta del archivo de museos"])
caso("A06", "Segunda carga: no duplica los días",
     [CARGA_COMPLETA, ["6"], informe("Museo del Mar")], [CARGA_CON_MUSEOS, "Días registrados: 5"])
caso("A07", "Carga sin líneas descartadas", [CARGA_COMPLETA], ["Museos cargados: 4", "Días cargados: 10"],
     ["descartada"])
caso("A08", "Archivos guardados desde Excel (BOM, \\r\\n, espacios, líneas vacías)",
     [cargar("datos/museos_excel.csv", "datos/visitantes_excel.csv"), informe("Museo del Mar")],
     ["Línea 5 descartada. El nombre no puede estar vacío", "Línea 6 descartada. La línea no tiene cinco campos",
      "Museos cargados: 1", "Línea 3 descartada. La línea no tiene dos campos", "Línea 4 descartada. " + NO_HAY,
      "Línea 5 descartada. " + VIS_ENTERO, "Días cargados: 1", "Visitantes totales: 96"],
     ["Línea 2 descartada", "Línea 3 descartada. El", "Línea 4 descartada. La"])
caso("A09", "Archivo en Latin-1", [cargar("datos/museos_latin1.csv")],
     ["El archivo no está guardado en UTF-8"], ["Museos cargados"])
caso("A10", "Archivo con solo el encabezado", [cargar("datos/solo_encabezado.csv", "datos/solo_encabezado.csv")],
     ["Museos cargados: 0", "Días cargados: 0"])
caso("A11", "Archivo vacío", [cargar("datos/vacio.csv", "datos/vacio.csv")],
     ["Museos cargados: 0", "Días cargados: 0"])
caso("A12", "Rutas entre comillas y con espacios",
     [cargar('"datos/museos_completos.csv"', "  datos/visitantes_completos.csv  ")],
     ["Museos cargados: 4", "Días cargados: 10"])
caso("A13", "La ruta es una carpeta", [cargar("datos")], [SIN_ARCHIVO])
caso("A14", "Después de cargar, el registro sigue desde el teclado", [CARGA_COMPLETA, ["2", CAFE, "20"]],
     ["Visitantes del 2026-11-02:", "Día registrado"])
caso("A15", "Los museos cargados cuentan para los nombres repetidos",
     [CARGA_COMPLETA, crear("Museo del Mar", 10, 2026, 11, 1)], ["Ya existe un museo con ese nombre"])
caso("A16", "Líneas vacías en el archivo de visitantes: se saltan y el número de línea no se corre",
     [cargar("datos/museos_completos.csv", "datos/visitantes_vacias.csv")],
     ["Línea 6 descartada. Los visitantes van de 0 a 200", "Días cargados: 3"],
     ["Línea 3", "Línea 4", "Línea 7"])

# ---------- Req. 14: el menú ----------
caso("U01", "Opción fuera de rango", [["8"]], ["La opción no es válida"])
caso("U02", "Opción de texto", [["dos"]], ["La opción no es válida"])
caso("U03", "Opción vacía", [[""]], ["La opción no es válida"])
caso("U04", "Opción 0", [["0"]], ["La opción no es válida"])
caso("U05", "Salir termina sin errores", [], ["Red de Museos del Caribe"])


# ---------- Los incrementos: qué casos le corresponden a cada uno ----------
def serie(letra, desde, hasta):
    return [f"{letra}{n:02d}" for n in range(desde, hasta + 1)]


INCREMENTOS = {
    1: ("Crear, registrar y simular",
        "1 (crear un museo), 2 (registrar los visitantes del día siguiente) y 3 (simular días)",
        "Menú con las opciones 1, 2, 3 y 7. Los casos de este incremento no necesitan el informe: se comprueban con los mensajes del programa. "
        "Los casos de simulación que solo se ven en el informe (S01, S07 a S10) se ejecutan en el Incremento 2.",
        serie("C", 1, 22) + ["C25"] + serie("R", 1, 10) + serie("S", 2, 6) + ["S11"]),
    2: ("El informe de un museo",
        "4 (el informe), 5 (desviación estándar), 6 (días de más y de menos visitantes), 7 (niveles), 8 (racha) y 9 (días sin registrar)",
        "Opción 4. Incluye los casos de simulación que se aplazaron del Incremento 1, porque necesitan el informe para ver los días agregados. "
        "I01 a I04 se comprueban en el Incremento 4, que es cuando existe la carga de archivos; aquí se pueden comprobar creando el museo y registrando sus días a mano.",
        serie("I", 5, 13) + ["S01"] + serie("S", 7, 10)),
    3: ("Varios museos y comparación",
        "10 (varios museos en el mismo programa) y 11 (porcentaje de asistencia más alto y más bajo)",
        "Opción 5. M01 y P01 usan los archivos de datos y se ejecutan en el Incremento 4.",
        serie("M", 2, 4) + serie("P", 2, 5)),
    4: ("Carga desde archivos",
        "12 (cargar los museos desde un archivo) y 13 (cargar los visitantes desde un archivo)",
        "Opción 6. Incluye los casos que usan la carga completa para armar los museos: I01 a I04, M01 y P01.",
        ["A01"] + serie("A", 3, 16) + serie("I", 1, 4) + ["M01", "P01"]),
    5: ("Menú, verificación ampliada y cierre",
        "14 (el menú) y los casos nuevos de la verificación ampliada",
        "Opción 7 y los avisos para opciones no válidas. Los casos C23, C24, C26, R11, R12, S12, S13, S14 e I14 son los que pusieron en evidencia "
        "los tres comportamientos que se corrigieron: enteros con guion bajo, cierre del programa en el año 9999 y días a simular enormes.",
        serie("U", 1, 5) + ["C23", "C24", "C26", "R11", "R12", "S12", "S13", "S14", "I14"]),
}
INCREMENTO_DE = {}
for numero, datos in INCREMENTOS.items():
    for id_caso in datos[3]:
        assert id_caso not in INCREMENTO_DE, id_caso
        INCREMENTO_DE[id_caso] = numero
assert sorted(INCREMENTO_DE) == sorted(c[0] for c in casos), "hay casos sin incremento"


def describir_entradas(bloques):
    partes = []
    for bloque in bloques:
        partes.append(" / ".join(texto if texto != "" else "↵" for texto in bloque))
    return " → ".join(partes) if partes else "(solo salir)"


if "--casos" in sys.argv:
    # Genera un documento de casos por incremento, con los mismos casos que ejecuta el verificador.
    for numero, (titulo, requisitos, nota, ids_del_incremento) in INCREMENTOS.items():
        propios = [c for c in casos if INCREMENTO_DE[c[0]] == numero]
        with open(f"casos_de_verificacion_incremento_{numero}.md", "w", encoding="utf-8") as archivo:
            archivo.write(f"# Casos de verificación – Incremento {numero}: {titulo}\n\n")
            archivo.write(f"Requisitos: {requisitos}.\n\n{nota}\n\n")
            archivo.write(f"Se ejecutan con `python verificar_casos.py --incremento {numero}` desde la carpeta del proyecto ")
            archivo.write(f"(o todos con `python verificar_casos.py`). Este documento se genera con `python verificar_casos.py --casos`. ")
            archivo.write(f"Son {len(propios)} casos.\n\n")
            archivo.write("**Cómo leer la columna \"Se teclea\".** Cada tramo separado por ` → ` es una opción del menú: ")
            archivo.write("el primer dato es la opción y los siguientes son lo que se teclea en esa opción. ")
            archivo.write("`↵` es una entrada vacía. Después de cada opción el programa pide Enter, y al final se elige 7. ")
            archivo.write("Los casos que dependen de la fecha de hoy calculan su salida esperada con la fecha del día en que se ejecutan.\n\n")
            archivo.write("| Caso | Qué prueba | Se teclea | La salida debe contener | La salida no debe contener |\n|---|---|---|---|---|\n")
            for id_, que_prueba, bloques, debe, no_debe, revisar in propios:
                entradas = describir_entradas(bloques).replace("|", "\\|")
                esperado = " · ".join(f"`{t}`" for t in debe).replace("|", "\\|")
                if revisar is not None:
                    esperado += " · (la suma de visitantes está entre 225 y 450)"
                prohibido = " · ".join(f"`{t}`" for t in no_debe)
                archivo.write(f"| {id_} | {que_prueba} | {entradas} | {esperado} | {prohibido} |\n")
    print(f"{len(INCREMENTOS)} documentos de casos generados, con {len(casos)} casos en total")
    sys.exit(0)


def ejecutar(bloques):
    entradas = []
    for bloque in bloques:
        entradas.extend(bloque)
        entradas.append("")
    entradas.append("7")
    return subprocess.run([sys.executable, "user_interface.py"], input="\n".join(entradas) + "\n",
                          capture_output=True, text=True, encoding="utf-8",
                          env={"TERM": "dumb", "PATH": "/usr/bin:/bin", "PYTHONIOENCODING": "utf-8"})


incremento = None
if "--incremento" in sys.argv:
    incremento = int(sys.argv[sys.argv.index("--incremento") + 1])
    casos = [c for c in casos if INCREMENTO_DE[c[0]] == incremento]
filas = []
fallas = 0
for id_, que_prueba, bloques, debe, no_debe, revisar in casos:
    resultado = ejecutar(bloques)
    salida = resultado.stdout
    problemas = []
    if "Traceback" in resultado.stderr or resultado.returncode != 0:
        problemas.append("el programa se cerró con un error")
    for texto in debe:
        if texto not in salida:
            problemas.append(f"falta «{texto}»")
    for texto in no_debe:
        if texto in salida:
            problemas.append(f"no debía aparecer «{texto}»")
    if revisar is not None and not revisar(salida):
        problemas.append("la revisión adicional falló")
    estado = "OK" if not problemas else "FALLA"
    if problemas:
        fallas += 1
        print(f"{id_} FALLA: " + "; ".join(problemas))
    filas.append((id_, que_prueba, estado))

ahora = datetime.now().strftime("%Y-%m-%d %H:%M")
nombre_resultados = "resultados_verificacion.md" if incremento is None else f"resultados_verificacion_incremento_{incremento}.md"
with open(nombre_resultados, "w", encoding="utf-8") as archivo:
    sufijo = "" if incremento is None else f" – Incremento {incremento}"
    archivo.write(f"# Resultados de la verificación{sufijo}\n\nEjecutado el {ahora} (fecha de hoy para los casos que dependen de ella: {HOY}).\n")
    archivo.write("Ejecutado por: [nombre del integrante]\n\n| Caso | Qué prueba | Resultado obtenido |\n|---|---|---|\n")
    for id_, que_prueba, estado in filas:
        archivo.write(f"| {id_} | {que_prueba} | {estado} |\n")
    archivo.write(f"\nTotal: {len(filas)} casos, {len(filas) - fallas} OK, {fallas} con falla.\n")
print(f"{len(filas)} casos: {len(filas) - fallas} OK, {fallas} con falla. Detalle en {nombre_resultados}")
