# Juego-Tres-en-Raya-en-Python
El código permite a dos jugadores jugar "Tres en Raya" de forma interactiva en la consola de Python, garantizando que se sigan las reglas del juego y determinando un ganador o un empate.

# Funciona de la siguiente manera:

Inicialización del tablero: El juego comienza con un tablero vacío representado como una lista de listas, donde cada lista interna representa una fila del tablero y contiene espacios en blanco para cada casilla.

Alternancia entre jugadores: Los jugadores se alternan para realizar sus movimientos. El primer jugador es "X" y el segundo jugador es "O".

Jugadas de los jugadores: En cada turno, se le pide al jugador que elija una fila y una columna para realizar su movimiento. El juego valida si la jugada es válida (es decir, si la casilla está vacía y las coordenadas están dentro del rango del tablero).

Verificación de ganador: Después de cada movimiento, el juego verifica si el jugador actual ha ganado. Esto se hace comparando las filas, columnas y diagonales del tablero para ver si están ocupadas por el mismo jugador.

Finalización del juego: El juego termina cuando un jugador gana (se muestra un mensaje de felicitación), hay un empate (todas las casillas están ocupadas sin un ganador) o los jugadores deciden salir del juego.

Impresión del tablero: Después de cada movimiento, se imprime el estado actual del tablero para que los jugadores puedan ver la situación del juego.
