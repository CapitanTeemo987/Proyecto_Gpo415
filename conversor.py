historial_conversiones = []
"""
Función para mostrar el historial de conversiones
 - Si hay conversiones, las muestra
 - Si no hay, informa al usuario
"""
def mostrar_historia():
    if historial_conversiones: 
        """"
        Comprueba que hay datos guardados en el historial, 
        si no hay datos regresa "No hay conversiones registradas"
        """
        print("\n__Historial de conversiones__")
        for i in historial_conversiones: 
            print(f"\n{i}")
    else:
        print("\nNo hay conversiones registradas") 

conversiones_longitud = [
    [1, 0.621371, 100000, 1000],  #Km (Km, Milla, Cm, Metros)
    [1.60934, 1, 160934, 1609.34],  #Milla (Km, Milla, Cm, Metros)
    [0.00001, 0.0000062137, 1, 0.01],  #Cm (Km, Milla, Cm, Metros)
    [0.001, 0.000621371, 100, 1]  #Metros (Km, Milla, Cm, Metros)
]
"""
Matriz de conversiones de longitud (km, millas, cm, metros)
Fila representa la unidad de origen, columna la unidad destino
"""

def convertir_longitud(cantidad, fila, columna): 
    return cantidad * conversiones_longitud[fila][columna]
"""
Función para realizar conversiones de longitud
 - Recibe la cantidad y las posiciones en la matriz de conversión
 - Regresa la cantidad convertida
"""

def menu_longitud():
    """
    Funcion que muestra un menú para 
    seleccionar las conversiones de longitud
    """
    while True: 
        """
        #El cilo while True se ejecutará siempre hasta que 
        # el usuaro dijite 6. El ciclo se acaba con el "break"
        """
        print(
            """
Menu de Longitud

[1] Km a Milla
[2] Milla a km
[3] Cm a Metros
[4] Metros a Cm
[5] Km a Cm
[6] Menu principal
"""
)
        """
        Input de la opción del menú 
        """
        respuesta2 = int(input("Escribe la opcion deseada: "))
        if respuesta2 == 1: #Condicional para ejecutar los km a millas
            km = float(input("Escribe los km: ")) #Asignamos una variable para el input
            resultado1 = convertir_longitud(km, 0, 1) #Llamamos a la funcion para realizar la conversión
            historial_conversiones.append(f"{km} km son {resultado1} millas") #Agregamos al historial
            print(f"El total en millas es: {resultado1}") #Monstramos el resultado al usuario

        #Condicional para ejecutar las millas a km
        elif respuesta2 == 2:
            mi = float(input("Escriba las millas: ")) #Asignamos una variable para el input
            resultado2 = convertir_longitud(mi, 1, 0) #Llamamos a la funcion para realizar la conversión
            historial_conversiones.append(f"{mi} mi son {resultado2} km") #Agregamos al historial
            print(f"El total en km es: {resultado2}") #Monstramos el resultado al usuario

        #Condicional para ejecutar los cm a metros
        elif respuesta2 == 3:
            Cm = float(input("Escribe los Cm: ")) #Asignamos una variable para el input
            resultado3 = convertir_longitud(Cm, 2, 3) #Llamamos a la funcion para realizar la conversión
            historial_conversiones.append(f"{Cm} Cm son {resultado3} Metros") #Agregamos al historial
            print(f"El total de Cm a Metros es: {resultado3}") #Monstramos el resultado al usuario

        #Condicional para ejecutar los metros a cm
        elif respuesta2 == 4:
            Metros = float(input("Escribe la cantidad de Metros: ")) #Asignamos una variable para el input
            resultado4 = convertir_longitud(Metros, 3, 2) #Llamamos a la funcion para realizar la conversión
            historial_conversiones.append(f"{Metros} Metros son {resultado4} Cm") #Agregamos al historial
            print(f"El total en Metros es: {resultado4}") #Monstramos el resultado al usuario

        #Condicional para ejecutar los km a cm
        elif respuesta2 == 5:
            km = float(input("Escribe los Km: ")) #Asignamos una variable para el input
            resultado5 = convertir_longitud(km, 0, 2) #Llamamos a la funcion para realizar la conversión
            historial_conversiones.append(f"{km} Km son {resultado5} Cm") #Agregamos al historial
            print(f"{km} Km son {resultado5} Cm") #Monstramos el resultado al usuario
        
        #Opción para salir al menú principal
        elif respuesta2 == 6:
            print("\nRegresando al menu principal...")
            break #Uso del break para finalizar el ciclo while True

        #Verifica si el imput es un número del 1 al 6
        else:
            print("\nselecciona una opción del 1-6")


#Funciones para convertir unidades de tiempo
def Seg_a_Min(Seg):
    """
    Creamos la funcion que recibe "Seg" y 
    realiza la operación asignada
    """
    operacion5 = Seg * 0.0166667
    return operacion5

def Min_a_Seg(Min):
    """
    Creamos la funcion que recibe "Min" y 
    realiza la operación asignada
    """    
    operacion6 = Min * 60
    return operacion6

def Mic_a_Mil(Mic):
    """
    Creamos la funcion que recibe "Mic" y 
    realiza la operación asignada
    """
    operacion7 = Mic * 0.001
    return operacion7

def Mil_a_Mic(Mil):
    """
    Creamos la funcion que recibe "Mil" y 
    realiza la operación asignada
    """    
    operacion8 = Mil * 1000
    return operacion8


#Menú para seleccionar las conversiones de tiempo
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
        
        #Input de la opción del menú 
        respuesta3 = int(input("Escribe la opcion deseada: "))

        #Condicional para ejecutar los Segundos a Minutos
        if respuesta3 == 1:
            Seg = float(input("Escribe los Seg: "))
            resultado1 = Seg_a_Min(Seg)
            historial_conversiones.append(f"{Seg} Seg son {resultado1} Min")
            print(f"El total en Minutos es: {resultado1}")

        #Condicional para ejecutar los Minutos a Segundos
        elif respuesta3 == 2:
            Min = float(input("Escribe la cantidad de Min: "))
            resultado2 = Min_a_Seg(Min)
            historial_conversiones.append(f"{Min} Min son {resultado2} Seg")
            print(f"La cantidad en Segundos es: {resultado2}")

        #Condicional para ejecutar los Microsegundos a Milisegundos
        elif respuesta3 == 3:
            Mic = float(input("Ingresa la cantidad de Microsegundos: "))
            resultado3 = Mic_a_Mil(Mic)
            historial_conversiones.append(f"{Mic} Microsegundos son {resultado3} Milisegundos")
            print(f"El resultado en Milisegudnos es: {resultado3}")

        #Condicional para ejecutar los Milisegundos a Microsegundos
        elif respuesta3 == 4:
            Mil = float(input("Escribe la cantidad de Milisegudnos: "))
            resultado4 = Mil_a_Mic(Mil)
            historial_conversiones.append(f"{Mil} Milisegundos son {resultado4} Microsegundos")
            print(f"El resultado en Microsegundos es: {resultado4}")

        #Regresa al menú principal
        elif respuesta3 == 5:
            print("\nRegresando al menu principal...")
            break #Uso del break para finalizar el ciclo while True

        #Verifica si el imput es un número del 1 al 5
        else:
            print("\nEscribe una opción del 1-5")


#Funciones para convertir unidades de área
def Cm2_a_Metro2(Cm2):
    """
    Creamos la funcion que recibe "Cm2" y 
    realiza la operación asignada
    """
    operacion = Cm2 * 10**-4
    return operacion

def Metro2_a_Cm2(Metro2):
    """
    Creamos la funcion que recibe "Metro2" y 
    realiza la operación asignada
    """
    operacion2 = Metro2 * 10000
    return operacion2

def Km2_a_Ha(Km2):
    """
    Creamos la funcion que recibe "Km2" y 
    realiza la operación asignada
    """
    operacion3 = Km2 * 100
    return operacion3

def Ha_a_Km2(Ha):
    """
    Creamos la funcion que recibe "Ha" y 
    realiza la operación asignada
    """
    operacion4 = Ha * 0.01
    return  operacion4

#Menú para seleccionar las conversiones de área
def menu_area():
    while True:
        print("""
Menu Area

[1] Cm^2 a Metro^2
[2] Metro^2 a Cm^2
[3] Km^2 a Hectarea
[4] hectarea a Km^2
[5] Menu Principal
        """)

        #Input de la opción del menú 
        respuesta4 = int(input("Escribe la opcion deseada: "))

        #Condicional para ejecutar los Cm^2 a Metros^2
        if respuesta4 == 1:
            Cm2 = float(input("Escribe los Cm^2: "))
            resultado1 = Cm2_a_Metro2(Cm2)
            historial_conversiones.append(f"{Cm2} Cm^2 son {resultado1} Metros^2")
            print(f"El total es de: {resultado1:.4f} Metros")

        #Condicional para ejecutar los Metros^2 a Cm^2
        elif respuesta4 == 2:
            Metro2 = float(input("Escribe los Metros^2: "))
            resultado2 = Metro2_a_Cm2(Metro2)
            historial_conversiones.append(f"{Metro2} Metros^2 son {resultado2} Cm^2")
            print(f"El total es de: {resultado2} Cm^2")

        #Condicional para ejecutar los Km^2 a Hectarea
        elif respuesta4 == 3:
            Km2 = float(input("Escribe los Km2: "))
            resultado3 = Km2_a_Ha(Km2)
            historial_conversiones.append(f"{Km2} km2 son {resultado3} Ha")
            print(f"El total es de: {resultado3} Ha")

        #Condicional para ejecutar las hectareas a Km^2        
        elif respuesta4 == 4:
            Ha = float(input("Escribe las Hectareas: "))
            resultado4 = Ha_a_Km2(Ha)
            historial_conversiones.append(f"{Ha} Hectareas son {resultado4} Km2")
            print(f"El total es de: {resultado4} Km2")

        #Regresar al menú principal
        elif respuesta4 == 5:
            print("\nRegresando al menu principal...")
            break #Uso del break para finalizar el ciclo while True
        
        #Verifica si el imput es un número del 1 al 5
        else:
            print("\nEscribe una opcion del 1-5")


#Ejecuta el menú principal con el ciclo while True 
while True:
    print("""
    Menu principal

    [1] Longitud
    [2] Tiempo
    [3] Area
    [4] Historial
    [5] Salir
    """)

    #Input para elegir el tipo de conversión que se desea hacer 
    respuesta = int(input("Escribe la opción deseada: "))

    if respuesta == 1:
        """
        Condicional para entrar al menú de longitud 
        """
        menu_longitud()

    elif respuesta == 2:
        """
        Condicional para entrar al menú de tiempo 
        """
        menu_tiempo()

    elif respuesta == 3:
        """
        Condicional para entrar al menú de área 
        """
        menu_area()

    elif respuesta == 4:
        """
        Condicional para mostrar el historial
        """
        mostrar_historia()
    
    elif respuesta == 5:
        """
        Evalua la opción para salir del bucle con un "break" 
        ya que el while True siempre se repite hasta que 
        el usuario quiera salir
        """
        print("Saliendo del programa...")
        break

    else:
        """
        Si la opción no es un numero del 1-5, 
        te regresa al menu principal y te
        vuelve a mostrar las opciones
        """
        print("Escribe una opcion del 1-5")
    