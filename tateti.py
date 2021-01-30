# Ta Te Ti en Python con una AI básica
import random

tablero = [' ' for x in range(10)]


def ingresarLetra(letra, pos):
    # Llena la posición con 'O' o con 'X'
    tablero[pos] = letra


def hayLugar(pos):
    # Si la posición está vacía, retorna True (pos vacía = ' ')
    return tablero[pos] == ' '


def mostrarTablero(tablero):
    # Imprime en consola el tablero con las letras colocadas
    # El tablero se verá así:

    #  X | O | X
    # -----------
    #  O | X | O
    # -----------
    #  X | O | X

    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('-----------')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('-----------')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])


def esGanador(ta, le):
    # Analiza todas las combinaciones de 3 posiciones en el tablero para verificar si el jugador ganó el juego
    return ((ta[1] == le and ta[2] == le and ta[3] == le) or  # Primera fila
            (ta[4] == le and ta[5] == le and ta[6] == le) or         # Segunda Fila
            (ta[7] == le and ta[8] == le and ta[9] == le) or         # Tercera Fila
            # Primera Columna
            (ta[1] == le and ta[4] == le and ta[7] == le) or
            # Segunda Columna
            (ta[2] == le and ta[5] == le and ta[8] == le) or
            # Tercera Columna
            (ta[3] == le and ta[6] == le and ta[9] == le) or
            # Diagonal Izq-Der
            (ta[1] == le and ta[5] == le and ta[9] == le) or
            (ta[3] == le and ta[5] == le and ta[7] == le))           # Diagonal Der-Izq


def turnoJugador():
    # Ingresa un loop para validar el input del usuario. Recibe la posición que ingresa el usuario
    # tras validarla, revisa que la posición esté libre y en caso de que sea así, coloca la letra
    # en la posición y sale del loop
    corriendo = True
    while corriendo:
        pos = input("Ingrese la posición donde colocar una 'X' (1-9): ")
        try:
            pos = int(pos)
            if pos > 0 and pos < 10:
                if hayLugar(pos):
                    ingresarLetra('X', pos)
                    corriendo = False
                else:
                    print("Elija una posición libre.\n")
            else:
                print("Ingrese una posición válida entre 1 y 9.\n")
        except:
            print("Por favor, ingrese caracteres numéricos.\n")


def turnoComputadora():
    # Algoritmo de la computadora
    posLibres = [x for x, letter in enumerate(
        tablero) if letter == ' ' and x != 0]  # Posiciones posibles
    pos = 0  # Posición default (si no hay otras posiciones posibles)

    # De esta forma, se revisa si hay alguna posición donde las 'O' o las 'X' ganen. Si las 'O' ganan, retorna esa posición y la computadora gana.
    # Si las 'X' ganan, retorna esa posición para prevenir la victoria del jugador
    for let in ['O', 'X']:
        for i in posLibres:
            # Con esto creo un nuevo tablero con su propio espacio en memoria en lugar de hacer referencia al original
            tableroCopia = tablero[:]
            tableroCopia[i] = let
            if esGanador(tableroCopia, let):
                pos = i
                return pos

    # Si no hay movimientos ganadores o que prevengan la victoria del contrincante, se procede a tratar de tomar alguna esquina
    esquinasLibres = []
    for i in posLibres:
        if i in [1, 3, 7, 9]:
            esquinasLibres.append(i)

    if len(esquinasLibres) > 0:
        pos = elegirRandom(esquinasLibres)
        return pos

    # Si las esquinas están ocupadas, se procede a tomar el centro
    if 5 in posLibres:
        pos = 5
        return pos

    # Si el centro está ocupado, se toma algún borde
    bordesLibres = []
    for i in posLibres:
        if i in [1, 3, 7, 9]:
            bordesLibres.append(i)

    if len(bordesLibres) > 0:
        pos = elegirRandom(bordesLibres)
        return pos

    # En este punto, si no se encontraron posiciones posibles, la función retornará 0, lo que indicará que el tablero se encuentra lleno y termina el juego en empate
    return pos


def elegirRandom(listaPosiciones):
    # Retorna un número aleatorio de una lista de nümeros
    ln = len(listaPosiciones)
    r = random.randrange(0, ln)
    return listaPosiciones[r]


def tableroEstaLleno(tablero):
    if tablero.count(' ') > 1:
        return False
    else:
        return True


def main():
    print("\nBienvenid@ a Ta Te Ti!\n")

    mostrarTablero(tablero)

    while not(tableroEstaLleno(tablero)):

        if(tableroEstaLleno(tablero)):
            print("Empate!\n")
            mostrarTablero(tablero)

        if not esGanador(tablero, 'O'):
            turnoJugador()
        else:
            print("La computadora ganó esta partida!")
            break

        if not esGanador(tablero, 'X'):
            pos = turnoComputadora()
            if pos == 0:
                print("Empate!\n")
                mostrarTablero(tablero)
                break
            else:
                ingresarLetra('O', pos)
                print(f"La computadora colocó una 'O' en la posición {pos}")
        else:
            print("Has ganado la partida!")
            break

        mostrarTablero(tablero)


main()
