tablero = [["O", ".", ".","."], ["O", ".", ".", "."], ["O", ".", ".", "."], [".", "X", "X", "X"]]
Ficha = {
    "O1": (0, 0),
    "O2": (1, 0),
    "O3": (2, 0),
    "X1": (3, 1),
    "X2": (3, 2),
    "X3": (3, 3)
}
MOVIMIENTOS = {
    1: (0, -1),
    2: (-1, 0),
    3: (0, 1)
}
def tableron(tablero):
    print()
    for fila in tablero:
        for elem in fila:
            print(elem, end=" ")
        print()
    print()

def jugador1(op, i, j):
    if op in MOVIMIENTOS:
        tablero[i][j] = "."
        di, dj = MOVIMIENTOS[op]
        i += di
        j += dj
        tablero[i][j] = "X"
    return i, j
def jugador2(op, o, l):
    if op in MOVIMIENTOS:
        tablero[i][j] = "."
        di, dj = MOVIMIENTOS[op]
        i += di
        j += dj
        tablero[i][j] = "X"
    return i, j
def JUEGO():
    tableron(tablero)
    print("Que ficha quieres mover 1,2 o 3?")
    ficha = int(input("Ingresa un número: "))
    print("elige ficha izquierda(1), arriba(2) o derecha(3)")
    op = int(input("Ingresa un número: "))
    jugador1(op, i, j)
    tableron(tablero)
JUEGO()
