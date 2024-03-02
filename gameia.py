# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

# Función para verificar si un jugador ha ganado
def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all([casilla == jugador for casilla in fila]):
            return True

    # Verificar columnas
    for col in range(3):
        if all([tablero[fila][col] == jugador for fila in range(3)]):
            return True

    # Verificar diagonales
    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True

    return False

# Función para jugar
def jugar_tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"
    jugadas = 0

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, elige una fila (0, 1, 2): "))
        col = int(input(f"Jugador {jugador_actual}, elige una columna (0, 1, 2): "))

        if fila < 0 or fila > 2 or col < 0 or col > 2 or tablero[fila][col] != " ":
            print("Movimiento no válido. Inténtalo de nuevo.")
            continue

        tablero[fila][col] = jugador_actual
        jugadas += 1

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break
        elif jugadas == 9:
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

if __name__ == "__main__":
    jugar_tres_en_raya()
