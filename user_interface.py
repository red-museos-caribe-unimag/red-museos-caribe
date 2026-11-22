from datetime import date, timedelta
from os import name as sistema, system

from business_logic import (ALTA, BAJA, MEDIA, MENSAJE_FIN_DEL_CALENDARIO, PLENA,
                            RedDeMuseos, convertir_dias_a_simular)

red = RedDeMuseos()
salir = False

while not salir:
    system("cls" if sistema == "nt" else "clear")
    print("=====================================")
    print("Red de Museos del Caribe")
    print("=====================================")
    print("1. Crear un museo")
    print("2. Registrar los visitantes del día siguiente")
    print("3. Simular días")
    print("4. Ver el informe de un museo")
    print("5. Ver el museo con el porcentaje de asistencia más alto y el más bajo")
    print("6. Cargar los museos y los visitantes desde archivos")
    print("7. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        print("\n--- Crear un museo ---")
        nombre = input("Nombre del museo: ")
        aforo = input("Aforo diario: ")
        anio = input("Año de inicio del registro: ")
        mes = input("Mes de inicio del registro: ")
        dia = input("Día de inicio del registro: ")
        try:
            museo = red.crear_museo(nombre, aforo, anio, mes, dia)
            print(f"Museo {museo.nombre} creado, sin días registrados")
        except ValueError as error:
            print(error)

    elif opcion == "2":
        print("\n--- Registrar los visitantes del día siguiente ---")
        museo = red.buscar_museo(input("Nombre del museo: "))
        if museo is None:
            print("No hay un museo con ese nombre")
        elif not museo.hay_fechas_para(1):
            print(MENSAJE_FIN_DEL_CALENDARIO)
        else:
            fecha = museo.calcular_fecha_siguiente()
            registrado = False
            while not registrado:
                try:
                    museo.registrar_dia(input(f"Visitantes del {fecha}: "))
                    registrado = True
                except ValueError as error:
                    print(error)
            print("Día registrado")

    elif opcion == "3":
        print("\n--- Simular días ---")
        museo = red.buscar_museo(input("Nombre del museo: "))
        if museo is None:
            print("No hay un museo con ese nombre")
        else:
            # Un solo try: ante el primer dato inválido se avisa y se vuelve al menú.
            try:
                dias = convertir_dias_a_simular(input("Número de días a simular: "))
                minimo = museo.convertir_visitantes(input("Visitantes mínimos: "))
                maximo = museo.convertir_visitantes(input("Visitantes máximos: "))
                primer_dia = museo.simular_dias(dias, minimo, maximo)
                print(f"Días simulados: {dias}, del {primer_dia} al {museo.calcular_fecha_ultimo_dia()}")
            except ValueError as error:
                print(error)

    elif opcion == "4":
        print("\n--- Informe de un museo ---")
        museo = red.buscar_museo(input("Nombre del museo: "))
        if museo is None:
            print("No hay un museo con ese nombre")
        else:
            print(f"\nMuseo: {museo.nombre}")
            print(f"Aforo diario: {museo.aforo_diario}")
            if museo.contar_dias() == 0:
                print("El museo no tiene días registrados")
            else:
                print(f"Días registrados: {museo.contar_dias()}")
                print(f"Visitantes totales: {museo.calcular_total()}")
                print(f"Promedio de visitantes por día: {round(museo.calcular_promedio(), 2)}")
                print(f"Porcentaje de asistencia: {round(museo.calcular_porcentaje(), 2)} %")
                print(f"Desviación estándar de los visitantes: {round(museo.calcular_desviacion(), 2)}")
                print(f"Día de más visitantes: {museo.buscar_fecha_del_mayor()}")
                print(f"Día de menos visitantes: {museo.buscar_fecha_del_menor()}")

                print("Días en cada nivel de asistencia:")
                print(f"  {BAJA}: {museo.contar_dias_en_nivel(BAJA)}")
                print(f"  {MEDIA}: {museo.contar_dias_en_nivel(MEDIA)}")
                print(f"  {ALTA}: {museo.contar_dias_en_nivel(ALTA)}")
                print(f"  {PLENA}: {museo.contar_dias_en_nivel(PLENA)}")

                racha = museo.buscar_racha_baja()
                if racha is None:
                    print("El museo no tuvo ningún día en asistencia baja")
                elif racha[0] == 1:
                    print(f"Racha más larga en asistencia baja: 1 día, el {racha[1]}")
                else:
                    print(f"Racha más larga en asistencia baja: {racha[0]} días, desde el {racha[1]}")

                # La fecha de hoy se toma aquí y se le pasa a la lógica.
                hoy = date.today()
                faltan = museo.contar_dias_sin_registrar(hoy)
                print(f"Último día registrado: {museo.calcular_fecha_ultimo_dia()}")
                if faltan == 0:
                    print("El registro está al día")
                else:
                    ayer = hoy - timedelta(days=1)
                    print(f"Días por registrar: {faltan}, del {museo.calcular_fecha_siguiente()} al {ayer}")

    elif opcion == "5":
        print("\n--- Porcentaje de asistencia más alto y más bajo ---")
        mas_alto = red.buscar_museo_mas_alto()
        mas_bajo = red.buscar_museo_mas_bajo()
        if mas_alto is None:
            print("Ningún museo tiene días registrados")
        else:
            print(f"Museo con el porcentaje de asistencia más alto: {mas_alto.nombre}, con {round(mas_alto.calcular_porcentaje(), 2)} %")
            print(f"Museo con el porcentaje de asistencia más bajo: {mas_bajo.nombre}, con {round(mas_bajo.calcular_porcentaje(), 2)} %")

    elif opcion == "6":
        print("\n--- Cargar los museos y los visitantes desde archivos ---")
        # Un solo try: si ya hay museos no se pide ninguna ruta, y si el
        # archivo de museos falla no se pide la de visitantes.
        try:
            red.validar_red_vacia()
            descartadas = red.cargar_museos(input("Ruta del archivo de museos: "))
            for mensaje in descartadas:
                print(mensaje)
            print(f"Museos cargados: {red.contar_museos()}")

            descartadas = red.cargar_visitantes(input("\nRuta del archivo de visitantes: "))
            for mensaje in descartadas:
                print(mensaje)
            print(f"Días cargados: {red.contar_dias_totales()}")
        except ValueError as error:
            print(error)

    elif opcion == "7":
        salir = True
    else:
        print("La opción no es válida")

    if not salir:
        input("\nPresione Enter para volver al menú...")
