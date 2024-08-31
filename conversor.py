def km_a_milla(km):
    operacion = km * 0.621371
    return operacion

def milla_a_km(mi):
    operacion2 = mi * 1.60934
    return operacion2

def Cm_a_Metros(Cm):
    operacion3 = Cm * 0.01
    return operacion3

def Metros_a_Cm(Metros):
    operacion4 = Metros * 100
    return operacion4

def menu_longitud():
    while True:
        print("""
Menu de Longitud

[1] Km a Milla
[2] Milla a km
[3] Cm a Metros
[4] Metros a Cm
[5] Menu principal
"""
)

        respuesta2 = int(input("Escribe la opcion deseada: "))

        if respuesta2 == 1:
            km = float(input("Escribe los km: "))
            resultado1 = km_a_milla(km)
            print(f"El total en millas es: {resultado1}")

        elif respuesta2 == 2:
            mi = float(input("Escriba las millas: "))
            resultado2 = milla_a_km(mi)
            print(f"El total en km es: {resultado2}")

        elif respuesta2 == 3:
            Cm = float(input("Escribe los Cm: "))
            resultado3 = Cm_a_Metros(Cm)
            print(f"El total de Cm a Metros es: {resultado3}")

        elif respuesta2 == 4:
            Metros = float(input("Escribe la cantidad de Metros: "))
            resultado4 = Metros_a_Cm(Metros)
            print(f"El total en Metros es: {resultado4}")

        elif respuesta2 == 5:
            print("Regresando al menu principal...")
            break

        else:
            print("selecciona una opción del 1-3")


def Seg_a_Min(Seg):
    operacion5 = Seg * 0.0166667
    return operacion5

def Min_a_Seg(Min):
    operacion6 = Min * 60
    return operacion6

def Mic_a_Mil(Mic):
    operacion7 = Mic * 0.001
    return operacion7

def Mil_a_Mic(Mil):
    operacion8 = Mil * 1000
    return operacion8

def menu_tiempo():
    while True:
        print("""
Menu de Tiempo
[1] Segundos a Minutos
[2] Minutos a Segundos
[3] Microsegundo a Milisegundo
[4] Milisegudno a Microsegundo
[5] Menu Principal
""")
        respuesta3 = int(input("Escribe la opcion deseada: "))

        if respuesta3 == 1:
            Seg = float(input("Escribe los Seg: "))
            resultado1 = Seg_a_Min(Seg)
            print(f"El total en Minutos es: {resultado1}")

        elif respuesta3 == 2:
            Min = float(input("Escribe la cantidad de Min: "))
            resultado2 = Min_a_Seg(Min)
            print(f"La cantidad en Segundos es: {resultado2}")

        elif respuesta3 == 3:
            Mic = float(input("Ingresa la cantidad de Microsegundos: "))
            resultado3 = Mic_a_Mil(Mic)
            print(f"El resultado en Milisegudnos es: {resultado3}")

        elif respuesta3 == 4:
            Mil = float(input("Escribe la cantidad de Milisegudnos: "))
            resultado4 = Mil_a_Mic(Mil)
            print(f"El resultado en Microsegundos es: {resultado4}")

        elif respuesta3 == 5:
            print("Regresando al menu principal...")
            break

        else:
            print("Escribe una opción del 1-5")

def Cm2_a_Metro2(Cm2):
    operacion = Cm2 * 10**-4
    return operacion

def Metro2_a_Cm2(Metro2):
    operacion2 = Metro2 * 10000
    return operacion2

def Km2_a_Ha(Km2):
    operacion3 = Km2 * 100
    return operacion3

def Ha_a_Km2(Ha):
    operacion4 = Ha * 0.01
    return  operacion4

def menu_area():
    while True:
        print("""
Menu Area

[1] Cm2 a Metro2
[2] Metro2 a Cm2
[3] Km2 a Hectarea
[4] hectarea a Km2
[5] Menu Principal
        """)

        respuesta4 = int(input("Escribe la opcion deseada: "))

        if respuesta4 == 1:
            Cm2 = float(input("Escribe los Cm2: "))
            resultado1 = Cm2_a_Metro2(Cm2)
            print(f"El total es de: {resultado1:.4f} Metros")

        elif respuesta4 == 2:
            Metro2 = float(input("Escribe los Metros2: "))
            resultado2 = Metro2_a_Cm2(Metro2)
            print(f"El total es de: {resultado2} Cm2")

        elif respuesta4 == 3:
            Km2 = float(input("Escribe los Km2: "))
            resultado3 = Km2_a_Ha(Km2)
            print(f"El total es de: {resultado3} Ha")

        elif respuesta4 == 4:
            Ha = float(input("Escribe las Hectareas: "))
            resultado4 = Ha_a_Km2(Ha)
            print(f"El total es de: {resultado4} Km2")

        elif respuesta4 == 5:
            print("Regresando al menu principal...")
            break

        else:
            print("Escribe una opcion del 1-5")

while True:
    print("""
    Menu principal

    [1] Longitud
    [2] Tiempo
    [3] Area
    [4] Salir
    """)

    respuesta = int(input("Escribe la opción deseada: "))

    if respuesta == 1:
        menu_longitud()

    if respuesta == 2:
        menu_tiempo()

    if respuesta == 3:
        menu_area()

    elif respuesta == 4:
        print("Saliendo del programa...")
        break
