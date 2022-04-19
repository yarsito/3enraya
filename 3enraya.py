CELDAS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANCO = 'X', 'O', ' '


def main():
    print('Bienvenido a 3 en raya!')
    tableroJuego = obtenerTableroVacio()  # Create a TTT board dictionary.
    jugadorActual, jugadorSiguiente = X, O  # X goes first, O goes next.

    while True:  # Main game loop.
        # Display the board on the screen:
        print(obtenerStrTablero(tableroJuego))

        # Keep asking the player until they enter a number 1-9:
        movimiento = None
        while not esCeldaValida(tableroJuego, movimiento):
            print('')
            print('Cuál es el movimiento de {}? (1-9)'.format(jugadorActual))
            movimiento = input('> ')

        tableroJuego[movimiento] = jugadorActual

        # Comprueba si el juego ha terminado
        if esGanador(tableroJuego, jugadorActual):  # Comprueba si hay ganador
            print(obtenerStrTablero(tableroJuego))
            print('')
            print(jugadorActual + ' ha ganado la partida!')
            break
        elif tableroLleno(tableroJuego):  # Comprueba si hay empate
            print(obtenerStrTablero(tableroJuego))
            print('')
            print('Empate!')
            break

        # Cambio de turno entre jugadores:
        jugadorActual, jugadorSiguiente = jugadorSiguiente, jugadorActual

    print('Gracias por jugar!')


def obtenerTableroVacio():
    """Crea un tablero vacío para la partida de 3 en raya."""
    # Mapeado : 1|2|3
    #           -+-+-
    #           4|5|6
    #           -+-+-
    #           7|8|9
    tablero = {}
    for celda in CELDAS:
        tablero[celda] = BLANCO  # Todas las celdas del tablero se inicializan a BLANCO
    return tablero


def obtenerStrTablero(tablero):
    """Devuelve el tablero formateado como cadena de texto."""
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(tablero['1'], tablero['2'], tablero['3'],
                                tablero['4'], tablero['5'], tablero['6'],
                                tablero['7'], tablero['8'], tablero['9'])


def esCeldaValida(tablero, celda):
    """Devuelve True si la celda es válida y está en BLANCO."""
    return celda in CELDAS and tablero[celda] == BLANCO


def esGanador(tablero, jugador):
    """Devuelve True si el jugador es ganador."""
    # Se utilizan variables cortas para mejorar la legibilidad
    b, p = tablero, jugador
    # Busca el 3 en raya en las 3 filas, 3 columnas y las 2 diagonales
    return ((b['1'] == b['2'] == b['3'] == p) or  # Horizontal arriba
            (b['4'] == b['5'] == b['6'] == p) or  # Horizontal medio
            (b['7'] == b['8'] == b['9'] == p) or  # Horizontal abajo
            (b['1'] == b['4'] == b['7'] == p) or  # Vertical izquierda
            (b['2'] == b['5'] == b['8'] == p) or  # Vertical centro
            (b['3'] == b['6'] == b['9'] == p) or  # Vertical derecha
            (b['3'] == b['5'] == b['7'] == p) or  # Diagonal
            (b['1'] == b['5'] == b['9'] == p))  # Diagonal


def tableroLleno(tablero):
    """Devuelve True si todas las celdas están ocupadas."""
    for celda in CELDAS:
        if tablero[celda] == BLANCO:
            return False  # Hay al menos una celda que no está en blanco por lo que devolvemos False
    return True  # Ningún espacio en BLANCO por lo que se devuelve True


if __name__ == '__main__':
    main()
