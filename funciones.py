import numpy as np
import funciones as f
import variables as v

## FUNCIÓN DE CREAR TABLERO

def crear_tablero():
    tablero = np.full((10,10), " ")
    return tablero


## FUNCION QUE CREA BARCOS DE ESLORA 2 

def barco_eslora_2():

    primera_posicion = (np.random.randint(10), np.random.randint(10))

    direcciones_validas = []

    # Comprobar si puede colocarse en vertical
    if primera_posicion[0] < 9:
        direcciones_validas.append("V_abajo")
    if primera_posicion[0] > 0:
        direcciones_validas.append("V_arriba")

    # Comprobar si puede colocarse en horizontal
    if primera_posicion[1] < 9:
        direcciones_validas.append("H_derecha")
    if primera_posicion[1] > 0:
        direcciones_validas.append("H_izquierda")

    direccion = np.random.choice(direcciones_validas)

    if direccion == "V_abajo":
        segunda_posicion = (primera_posicion[0] + 1, primera_posicion[1])
    elif direccion == "V_arriba":
        segunda_posicion = (primera_posicion[0] - 1, primera_posicion[1])
    elif direccion == "H_derecha":
        segunda_posicion = (primera_posicion[0], primera_posicion[1] + 1)
    else:  
        segunda_posicion = (primera_posicion[0], primera_posicion[1] - 1)

    posiciones_barco = [primera_posicion, segunda_posicion]

    return (posiciones_barco)


## FUNCION QUE CREA BARCOS DE ESLORA 3

def barco_eslora_3():

    primera_posicion = (np.random.randint(10), np.random.randint(10))

    direcciones_validas = []

    # Comprobar si puede colocarse en vertical
    if primera_posicion[0] <= 7:
        direcciones_validas.append("V_abajo")
    if primera_posicion[0] >= 2:
        direcciones_validas.append("V_arriba")

    # Comprobar si puede colocarse en horizontal
    if primera_posicion[1] <= 7:
        direcciones_validas.append("H_derecha")
    if primera_posicion[1] >= 2:
        direcciones_validas.append("H_izquierda")

    direccion = np.random.choice(direcciones_validas)

    if direccion == "V_abajo":
        segunda_posicion = (primera_posicion[0] + 1, primera_posicion[1])
        tercera_posicion = (primera_posicion[0] + 2, primera_posicion[1])

    elif direccion == "V_arriba":
        segunda_posicion = (primera_posicion[0] - 1, primera_posicion[1])
        tercera_posicion = (primera_posicion[0] - 2, primera_posicion[1])

    elif direccion == "H_derecha":
        segunda_posicion = (primera_posicion[0], primera_posicion[1] + 1)
        tercera_posicion = (primera_posicion[0], primera_posicion[1] + 2)

    else: 
        segunda_posicion = (primera_posicion[0], primera_posicion[1] - 1)
        tercera_posicion = (primera_posicion[0], primera_posicion[1] - 2)

    posiciones_barco = [primera_posicion, segunda_posicion, tercera_posicion]

    return (posiciones_barco)


## FUNCION QUE CREA BARCOS DE ESLORA 4

def barco_eslora_4():

    primera_posicion = (np.random.randint(10), np.random.randint(10))

    direcciones_validas = []

    # Comprobar si puede colocarse en vertical
    if primera_posicion[0] <= 6:
        direcciones_validas.append("V_abajo")
    if primera_posicion[0] >= 3:
        direcciones_validas.append("V_arriba")

    # Comprobar si puede colocarse en horizontal
    if primera_posicion[1] <= 6:
        direcciones_validas.append("H_derecha")
    if primera_posicion[1] >= 3:
        direcciones_validas.append("H_izquierda")

    direccion = np.random.choice(direcciones_validas)

    if direccion == "V_abajo":
        segunda_posicion = (primera_posicion[0] + 1, primera_posicion[1])
        tercera_posicion = (primera_posicion[0] + 2, primera_posicion[1])
        cuarta_posicion = (primera_posicion[0] + 3, primera_posicion[1])

    elif direccion == "V_arriba":
        segunda_posicion = (primera_posicion[0] - 1, primera_posicion[1])
        tercera_posicion = (primera_posicion[0] - 2, primera_posicion[1])
        cuarta_posicion = (primera_posicion[0] - 3, primera_posicion[1])

    elif direccion == "H_derecha":
        segunda_posicion = (primera_posicion[0], primera_posicion[1] + 1)
        tercera_posicion = (primera_posicion[0], primera_posicion[1] + 2)
        cuarta_posicion = (primera_posicion[0], primera_posicion[1] + 3)

    else:
        segunda_posicion = (primera_posicion[0], primera_posicion[1] - 1)
        tercera_posicion = (primera_posicion[0], primera_posicion[1] - 2)
        cuarta_posicion = (primera_posicion[0], primera_posicion[1] - 3)

    posiciones_barco = [primera_posicion, segunda_posicion, tercera_posicion,cuarta_posicion]

    return (posiciones_barco)


## FUNCION QUE CREA Y COLOCA LOS BARCOS

def colocar_barcos(tablero):

    for esl in v.esloras_flota:
        while True:

            if esl == 2:
                barco = barco_eslora_2()
            elif esl == 3:
                barco = barco_eslora_3()
            elif esl == 4:
                barco = barco_eslora_4()
            else:
                print("La eslora no es correcta")
                
            if all(tablero[i][j] == " " for i, j in barco):
                for i, j in barco:
                    tablero[i][j] = "O"
                break
                     
    return(tablero)


## FUNCION PARA REALIZAR UN DISPARO

def disparar(disparos_jugador, barcos_rival, filas_disparo:int, columnas_disparo:int,):
    acierto = True
    try:
        print(filas_disparo, columnas_disparo)
        if barcos_rival[filas_disparo][columnas_disparo] == " ":
            disparos_jugador[filas_disparo][columnas_disparo] = "A"
            print ("AGUA!!! PIERDES TURNO!!!")
            acierto = False
                    
        elif barcos_rival[filas_disparo][columnas_disparo] == "X":
            print ("Disparo ya hecho")
            disparar(disparos_jugador, barcos_rival, filas_disparo, columnas_disparo)
        else: # es decir, si es "O"
            disparos_jugador[filas_disparo][columnas_disparo] = "X"
            acierto = True


    except:
        "Disparo no válido"

    return (disparos_jugador, acierto)


## FUNCION QUE IMPRIME POR PANTALLA EL ESTADO ACTUAL DE LA PARTIDA DEL JUGADOR

def pintar(tablero_barcos, tablero_disparos):
    
    print("TABLERO BARCOS")
    print(tablero_barcos)
    print("--------------------------")
    print("TABLERO DISPAROS")
    print(tablero_disparos)
    
    
    
    ## FUNCION QUE MARCA EL TURNO DE JUEGO Y SI SE HA ACABADO LA PARTIDA Y HAY UN GANADOR

def turnos(barcos_rival, disparos_rival, barcos_jugador, disparos_jugador):
    turno_jugador = True
    ganador=""
    while True:
        if turno_jugador == True:
            print("Turno jugador")
            fila = int (input("Introduce un numero de 0 a 9 que indique la filas: "))
            columna = int (input("Introduce un numero de 0 a 9 que indique la columna: "))
            disparos_jugador, acierto = disparar(disparos_jugador, barcos_rival, fila, columna)
            if acierto == False:
                turno_jugador = False
            else:
                turno_jugador = True
            pintar(barcos_jugador, disparos_jugador)
        else:
            print("Turno rival")
            fila = int (np.random.randint(10))
            columna = int (np.random.randint(10))
            disparos_rival, acierto = disparar(disparos_rival, barcos_jugador, fila, columna)
            if acierto is False:
                turno_jugador = True
            else:
                turno_jugador = False
            pintar(barcos_rival, disparos_rival)

        if "O" not in barcos_rival:
            ganador = "Jugador"
            break
        if "O" not in barcos_jugador:
            ganador = "Rival"
            break

    return ganador
