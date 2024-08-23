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

        elif respuesta3 == 5:
            print("Regresando al menu principal...")
            break

        else:
            print("Escribe una opción del 1-5")

while True:
    print("""
    Menu principal

    [1] Longitud
    [2] Tiempo
    [3] Volumen
    [4] Salir
    """)

    respuesta = int(input("Escribe la opción deseada: "))

    if respuesta == 1:
        menu_longitud()

    if respuesta == 2:
        menu_tiempo()

    elif respuesta == 4:
        print("Saliendo del programa...")
        break
