import random

def Crear_Tablero(Tamano):
    return [["~" for _ in range(Tamano)]for _ in range(Tamano)]

def Mostrar_Tableros (Tablero_Disparos_Jugador, Tablero_Disparos_Oponente):
    print("Tu tablero de disparos: ")
    for Fila in Tablero_Disparos_Jugador:
        print(" ".join(Fila))

    print("Tablero de disparos del oponente: ")
    for Fila in Tablero_Disparos_Oponente:
        print(" ".join(Fila))

def Colocar_Barcos(Tablero, Barcos, Jugador):
    for Barco in Barcos:
        Colocado=False
        while not Colocado:
            if Jugador == "Jugador":
                print(f"Colocando {Barco['Nombre']} de Tamano {Barco['Tamano']}")
                Fila=int(input("Ingresa la Fila: "))
                Columna=int(input("Ingrese la Colmuna: "))
                Orientación=input("Ingresar orientación (h para horizontal, v para vertical): ").lower()
            else:
                Fila= random.randint(0, len(Tablero)-1)
                Columna= random.randint(0,len(Tablero)-1)
                Orientación= random.choice(['h','v'])
            if Validar_Colocación(Tablero, Fila, Columna, Barco['Tamano'], Orientación):
                Colocar_Barco(Tablero, Fila, Columna, Barco['Tamano'], Orientación)
                Colocado=True 
            elif Jugador=="Jugador":
                print("Colocación inválida. Inténtelo de nuevo")

def Validar_Colocación(Tablero, Fila, Columna, Tamano, Orientación):
    if Orientación == 'h':
        if Columna+Tamano > len(Tablero):
            return False 
        for i in range (Tamano):
            if Tablero [Fila][Columna+i]!= "~":
                return False
    else:
        if Fila + Tamano > len (Tablero):
            return False
        for i in range (Tamano):
            if Tablero[Fila+i][Columna]!= "~":
               return False    
    return True

def Colocar_Barco(Tablero, Fila, Columna, Tamano, Orientación):
    if Orientación == 'h':
        for i in range(Tamano):
            Tablero[Fila][Columna + i] = "B"
    else:
        for i in range(Tamano):
            Tablero[Fila + i][Columna] = "B"

def Realizar_Disparo(Tablero_Oculto, Tablero_Disparos, Fila, Columna):
    if Tablero_Oculto[Fila][Columna] == "B":
        Tablero_Disparos[Fila][Columna] = "X"
        Tablero_Oculto[Fila][Columna] = "H"  # Marcar como hundido
        return "Impacto"
    elif Tablero_Disparos[Fila][Columna] == "~":
        Tablero_Disparos[Fila][Columna] = "O"
        return "Agua"
    return "Ya disparaste aquí"

def Verificar_Victoria(Tablero_Oculto):
    for Fila in Tablero_Oculto:
        if "B" in Fila:  # Si hay algún barco no hundido
            return False
    return True

def Jugador_Contra_Computadora():
    Tamano=5
    Tablero_Jugador = Crear_Tablero(Tamano)
    Tablero_Computadora =Crear_Tablero(Tamano)
    Tablero_Disparos_Jugador =Crear_Tablero(Tamano)
    Tablero_Disparos_Computadora =Crear_Tablero(Tamano)

    Barcos=[
         {"Nombre": "Portaaviones", "Tamano": 3},
         {"Nombre": "Submarino", "Tamano": 2}
   ]

    print("Coloca tus barcos")
    Colocar_Barcos(Tablero_Jugador, Barcos, "Jugador")
    Colocar_Barcos(Tablero_Computadora, Barcos, "Computadora")

    Turno_Jugador=True

    while True:
        if Turno_Jugador:
            print("Tu turno")
            Mostrar_Tableros(Tablero_Disparos_Jugador, Tablero_Disparos_Computadora)
            Fila=int(input("Ingresa fila de disparo: "))
            Columna=int(input("Ingresa columna de disparo: "))
            Resultado= Realizar_Disparo(Tablero_Computadora, Tablero_Disparos_Jugador, Fila, Columna)
            print(Resultado)
            if Verificar_Victoria (Tablero_Computadora):
                print("¡Ganaste!")
                return "Jugador"
    
        else:
            print("Turno de la computadora")
            Fila=random.randint(0, Tamano-1)
            Columna= random.randint(0, Tamano-1)
            Resultado=Realizar_Disparo(Tablero_Jugador, Tablero_Disparos_Computadora, Fila, Columna)
            print (f"La computadora disparó en ({Fila},{Columna}): {Resultado}")
            if Verificar_Victoria(Tablero_Jugador):
                print("La computadora ganó.")
                return "Computadora"

        Turno_Jugador=not Turno_Jugador

def Jugar_Dos_Jugadores():
    Tamano= 5
    Tablero_Jugador1=Crear_Tablero(Tamano)
    Tablero_Jugador2=Crear_Tablero(Tamano)
    Tablero_Disparos_Jugador1= Crear_Tablero(Tamano)
    Tablero_Disparos_Jugador2= Crear_Tablero(Tamano)

    Barcos=[
         {"Nombre": "Portaaviones", "Tamano": 3},
         {"Nombre": "Submarino", "Tamano": 2}
    ]

    print("Jugador 1 coloca sus barcos")
    Colocar_Barcos(Tablero_Jugador1, Barcos, "Jugador")
    print("Jugador 2 coloca sus barcos")
    Colocar_Barcos(Tablero_Jugador2, Barcos, "Jugador")

    Turno_Jugador1=True

    while True:
        if Turno_Jugador1:
            print("Turno del jugador 1")
            Mostrar_Tableros(Tablero_Disparos_Jugador1, Tablero_Disparos_Jugador2)
            Fila=int(input("Ingresa la fila de disparos: "))
            Columna= int(input("Ingresa la columna de disparo: "))
            Resultado= Realizar_Disparo(Tablero_Jugador2, Tablero_Disparos_Jugador1, Fila, Columna)
            print(Resultado)
            if Verificar_Victoria(Tablero_Jugador2):
                print("¡Jugador 1 ganó!")
                return "Jugador 1"
        else:
            print("Turno del Jugador 2")
            Mostrar_Tableros(Tablero_Disparos_Jugador2, Tablero_Disparos_Jugador1)
            Fila=int(input("Ingresa la fila de disparo: "))
            Columna=int(input("Ingresa la columna de disparo: "))
            Resultado=Realizar_Disparo(Tablero_Jugador1, Tablero_Disparos_Jugador2, Fila, Columna)
            print(Resultado)
            if Verificar_Victoria(Tablero_Jugador1):
                print("¡Jugador 2 ganó!")
                return "Jugador 2"
        Turno_Jugador1= not Turno_Jugador1

def Mostrar_Menú():
    print("Bienvenido a Batalla Naval: Caribe")
    print("1. Jugar")
    print("2. Dos Jugadores")
    print("3. Salir")

def Iniciar_Juego():
    while True:
        Mostrar_Menú()
        Modo=input("Elige una opción: ")

        if Modo == "1":
            Ganador=Jugador_Contra_Computadora()

        elif Modo == "2":
            Ganador=Jugar_Dos_Jugadores()
        
        elif Modo == "3":
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        else:
            print("La opción elegida no es váalida,por favor elija una opción válida entre 1 y 3")
            continue
        print(f"El ganador es: {Ganador}")

        Jugar_De_Nuevo=input("¿Quiere jugar de nuevo? (s/n): ").lower()
        if Jugar_De_Nuevo!="s": 
            print("Gracias por jugar.\nHasta la próxima.")
            break

Iniciar_Juego()










                     









