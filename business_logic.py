from datetime import date, timedelta
from math import sqrt
from os.path import isfile
from random import randint

AFORO_MINIMO = 1
VISITANTES_MINIMOS = 0
LIMITE_MEDIA = 30
LIMITE_ALTA = 60
LIMITE_PLENA = 85
MENSAJE_FIN_DEL_CALENDARIO = "El registro no puede pasar del 31 de diciembre de 9999"
BAJA = "Baja"
MEDIA = "Media"
ALTA = "Alta"
PLENA = "Plena"


def convertir_a_entero(texto, mensaje):
    # int() acepta cosas que no son enteros para un usuario: 1_000 (con guion
    # bajo) y dígitos de otros alfabetos. Se rechazan antes de llamarlo.
    if "_" in texto or not texto.isascii():
        raise ValueError(mensaje)
    # int() da un error en inglés; lo cambiamos por el mensaje del problema.
    try:
        return int(texto)
    except ValueError:
        raise ValueError(mensaje)


def crear_fecha(texto_anio, texto_mes, texto_dia):
    mensaje = "La fecha no es válida"
    anio = convertir_a_entero(texto_anio, mensaje)
    mes = convertir_a_entero(texto_mes, mensaje)
    dia = convertir_a_entero(texto_dia, mensaje)
    # Con un año enorme, date() lanza OverflowError y no ValueError.
    # Por eso se captura también, para que el programa no se cierre.
    try:
        return date(anio, mes, dia)
    except (ValueError, OverflowError):
        raise ValueError(mensaje)


def convertir_dias_a_simular(texto):
    dias = convertir_a_entero(texto, "El número de días debe ser un número entero")
    if dias < 1:
        raise ValueError("Se debe simular al menos un día")
    return dias


def leer_lineas(ruta):
    # "Copiar como ruta de acceso" de Windows deja la ruta entre comillas.
    ruta = ruta.strip().strip('"')
    if not isfile(ruta):
        raise ValueError("El archivo no existe")
    # utf-8-sig también lee los archivos que guarda Excel (con BOM).
    try:
        archivo = open(ruta, encoding="utf-8-sig")
        texto = archivo.read()
        archivo.close()
    except UnicodeDecodeError:
        raise ValueError("El archivo no está guardado en UTF-8")
    return texto.splitlines()


class Museo:
    def __init__(self, nombre, aforo_diario, fecha_inicio):
        self.nombre = nombre
        self.aforo_diario = aforo_diario
        self.fecha_inicio = fecha_inicio
        self.visitantes_por_dia = []

    def contar_dias(self):
        return len(self.visitantes_por_dia)

    def calcular_fecha_del_dia(self, posicion):
        return self.fecha_inicio + timedelta(days=posicion)

    def calcular_fecha_siguiente(self):
        return self.calcular_fecha_del_dia(self.contar_dias())

    def calcular_fecha_ultimo_dia(self):
        return self.calcular_fecha_del_dia(self.contar_dias() - 1)

    def hay_fechas_para(self, cantidad):
        # El calendario de Python termina el 31-12-9999. Se revisa antes de
        # agregar días, porque sumar fechas más allá de ese día da OverflowError.
        try:
            self.calcular_fecha_del_dia(self.contar_dias() + cantidad - 1)
            return True
        except OverflowError:
            return False

    def validar_visitantes(self, visitantes):
        if visitantes < VISITANTES_MINIMOS or visitantes > self.aforo_diario:
            raise ValueError(f"Los visitantes van de {VISITANTES_MINIMOS} a {self.aforo_diario}")

    def convertir_visitantes(self, texto):
        visitantes = convertir_a_entero(texto, "Los visitantes deben ser un número entero")
        self.validar_visitantes(visitantes)
        return visitantes

    def registrar_dia(self, texto):
        visitantes = self.convertir_visitantes(texto)
        if not self.hay_fechas_para(1):
            raise ValueError(MENSAJE_FIN_DEL_CALENDARIO)
        self.visitantes_por_dia.append(visitantes)

    def simular_dias(self, dias, minimo, maximo):
        # Se revisa todo antes de agregar, para no dejar días a medias.
        if dias < 1:
            raise ValueError("Se debe simular al menos un día")
        self.validar_visitantes(minimo)
        self.validar_visitantes(maximo)
        if minimo > maximo:
            raise ValueError("El mínimo no puede ser mayor que el máximo")
        if not self.hay_fechas_para(dias):
            raise ValueError(MENSAJE_FIN_DEL_CALENDARIO)
        # Se guarda antes de agregar: es la fecha del primer día simulado.
        primer_dia = self.calcular_fecha_siguiente()
        for i in range(dias):
            self.visitantes_por_dia.append(randint(minimo, maximo))
        return primer_dia

    def calcular_total(self):
        total = 0
        for visitantes in self.visitantes_por_dia:
            total += visitantes
        return total

    def calcular_promedio(self):
        return self.calcular_total() / self.contar_dias()

    def calcular_porcentaje(self):
        return self.calcular_promedio() / self.aforo_diario * 100

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = 0
        for visitantes in self.visitantes_por_dia:
            suma += (visitantes - promedio) ** 2
        return sqrt(suma / self.contar_dias())

    def buscar_fecha_del_mayor(self):
        posicion_mayor = 0
        for i in range(1, self.contar_dias()):
            # Con > estricto, si hay empate se queda el primero.
            if self.visitantes_por_dia[i] > self.visitantes_por_dia[posicion_mayor]:
                posicion_mayor = i
        return self.calcular_fecha_del_dia(posicion_mayor)

    def buscar_fecha_del_menor(self):
        posicion_menor = 0
        for i in range(1, self.contar_dias()):
            if self.visitantes_por_dia[i] < self.visitantes_por_dia[posicion_menor]:
                posicion_menor = i
        return self.calcular_fecha_del_dia(posicion_menor)

    def clasificar_dia(self, visitantes):
        # Se comparan enteros (visitantes * 100 contra límite * aforo) y no
        # decimales, para que 150 de 500 (30 %) quede justo en Media.
        ocupado = visitantes * 100
        if ocupado < LIMITE_MEDIA * self.aforo_diario:
            return BAJA
        if ocupado < LIMITE_ALTA * self.aforo_diario:
            return MEDIA
        if ocupado < LIMITE_PLENA * self.aforo_diario:
            return ALTA
        return PLENA

    def contar_dias_en_nivel(self, nivel):
        cantidad = 0
        for visitantes in self.visitantes_por_dia:
            if self.clasificar_dia(visitantes) == nivel:
                cantidad += 1
        return cantidad

    def buscar_racha_baja(self):
        # Retorna (días de la racha más larga, posición donde empezó),
        # o None si ningún día fue de asistencia baja.
        mejor_largo = 0
        mejor_inicio = 0
        largo_actual = 0
        inicio_actual = 0
        for i in range(self.contar_dias()):
            if self.clasificar_dia(self.visitantes_por_dia[i]) == BAJA:
                if largo_actual == 0:
                    inicio_actual = i
                largo_actual += 1
                # Con > estricto, si hay empate se queda la que empezó primero.
                if largo_actual > mejor_largo:
                    mejor_largo = largo_actual
                    mejor_inicio = inicio_actual
            else:
                largo_actual = 0
        if mejor_largo == 0:
            return None
        return (mejor_largo, self.calcular_fecha_del_dia(mejor_inicio))

    def contar_dias_sin_registrar(self, hoy):
        if not self.hay_fechas_para(1):
            # El registro llegó al último día del calendario: no falta ninguno.
            return 0
        dias = (hoy - self.calcular_fecha_siguiente()).days
        if dias < 0:
            dias = 0
        return dias


class RedDeMuseos:
    def __init__(self):
        self.museos = []

    def contar_museos(self):
        return len(self.museos)

    def buscar_museo(self, nombre):
        nombre = nombre.strip()
        for museo in self.museos:
            if museo.nombre == nombre:
                return museo
        return None

    def crear_museo(self, nombre, texto_aforo, texto_anio, texto_mes, texto_dia):
        # Las condiciones se revisan en el orden que pide el enunciado.
        nombre = nombre.strip()
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")
        if self.buscar_museo(nombre) is not None:
            raise ValueError("Ya existe un museo con ese nombre")
        aforo = convertir_a_entero(texto_aforo, "El aforo diario debe ser un número entero")
        if aforo < AFORO_MINIMO:
            raise ValueError("El aforo diario debe ser de al menos un visitante")
        fecha = crear_fecha(texto_anio, texto_mes, texto_dia)
        museo = Museo(nombre, aforo, fecha)
        self.museos.append(museo)
        return museo

    def buscar_museo_mas_alto(self):
        # Solo cuentan los museos con días; con > estricto gana el primero.
        elegido = None
        for museo in self.museos:
            if museo.contar_dias() > 0:
                if elegido is None or museo.calcular_porcentaje() > elegido.calcular_porcentaje():
                    elegido = museo
        return elegido

    def buscar_museo_mas_bajo(self):
        elegido = None
        for museo in self.museos:
            if museo.contar_dias() > 0:
                if elegido is None or museo.calcular_porcentaje() < elegido.calcular_porcentaje():
                    elegido = museo
        return elegido

    def contar_dias_totales(self):
        total = 0
        for museo in self.museos:
            total += museo.contar_dias()
        return total

    def validar_red_vacia(self):
        if self.contar_museos() > 0:
            raise ValueError("La carga solo se hace con el programa sin museos")

    def cargar_museos(self, ruta):
        self.validar_red_vacia()
        lineas = leer_lineas(ruta)
        descartadas = []
        # La línea 0 es el encabezado; el número de línea es posición + 1.
        for i in range(1, len(lineas)):
            if lineas[i].strip() != "":
                campos = lineas[i].split(";")
                try:
                    if len(campos) != 5:
                        raise ValueError("La línea no tiene cinco campos")
                    self.crear_museo(campos[0], campos[1].strip(), campos[2].strip(),
                                     campos[3].strip(), campos[4].strip())
                except ValueError as error:
                    descartadas.append(f"Línea {i + 1} descartada. {error}")
        return descartadas

    def cargar_visitantes(self, ruta):
        lineas = leer_lineas(ruta)
        descartadas = []
        for i in range(1, len(lineas)):
            if lineas[i].strip() != "":
                campos = lineas[i].split(";")
                try:
                    if len(campos) != 2:
                        raise ValueError("La línea no tiene dos campos")
                    museo = self.buscar_museo(campos[0])
                    if museo is None:
                        raise ValueError("No hay un museo con ese nombre")
                    museo.registrar_dia(campos[1].strip())
                except ValueError as error:
                    descartadas.append(f"Línea {i + 1} descartada. {error}")
        return descartadas
