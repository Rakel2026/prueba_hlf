import numpy as np
import funciones as f
import variables as v

## CREACIÓN DE TABLEROS

t_barcos_rival = f.crear_tablero()
t_disparos_rival = f.crear_tablero()
t_barcos_jugador = f.crear_tablero()
t_disparos_jugador = f.crear_tablero()


## PROCEDEMOS A CREAR Y COLOCAR LOS BARCOS EN LOS TABLEROS PERTINENTES

# PRIMERO EN EL TABLERO DEL JUGADOR

t_barcos_jugador = f.colocar_barcos(t_barcos_jugador)
print("El tablero de barcos del jugador es: ")
print(t_barcos_jugador)
print("El tablero de disparos del jugador es: ")
print(t_disparos_jugador)

# DESPUES EN EL TABLERO DEL RIVAL

t_barcos_rival = f.colocar_barcos(t_barcos_rival)
print("El tablero de barcos del rival es: ")
print(t_barcos_rival)

## EMPEZAMOS LA PARTIDA DECIDIENDO EL TURNO Y VAMOS JUGANDO.- TRAS HUNDIR LA FLOTA VEREMOS QUIEN ES EL/LA GANADOR/A

ganador = f.turnos(t_barcos_rival, t_disparos_rival, t_barcos_jugador, t_disparos_jugador)

print("EL GANADOR ES: ", ganador, " !!!!!")











    




