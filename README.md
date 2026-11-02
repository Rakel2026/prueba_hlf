# prueba_hlf

1er proyecto: Hundir la flota (1026_ Vitoria-Gasteiz)

# 🚢 Hundir la Flota (Battleship) en Python

¡Juega contra un rival controlado por la máquina y destruye su flota antes de que acabe con la tuya!

---

## 📋 Características del Juego

* **Tablero de 10x10**: Espacio de juego cuadriculado gestionado mediante matrices de NumPy.

* **Flota Dinámica**: Colocación automática de barcos de diferentes esloras (2, 3 y 4 casillas) con orientaciones aleatorias (vertical y horizontal).

* **Mecánica de Turnos**: 

  * Si aciertas el disparo, **repites turno**.

  * Si fallas ("Agua"), el turno pasa al rival.

* **Inteligencia del Rival**: El rival realiza disparos aleatorios automáticos sobre tu tablero.


## 📂 Estructura del Proyecto

El proyecto está modularizado en tres archivos principales:

1. `main.py`: Archivo principal que inicializa los tableros y gestiona el flujo de la partida.

2. `funciones.py`: Contiene toda la lógica del juego (creación de tableros, generación de barcos de eslora 2, 3 y 4, colocación, disparos, gestión de turnos y decisión del ganador).

3. `variables.py`: Almacena las variables globales y la configuración de las esloras de la flota.


