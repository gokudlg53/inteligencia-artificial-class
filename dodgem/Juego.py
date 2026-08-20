FICHA_O = {
    "O1": (0, 0),
    "O2": (1, 0),
    "O3": (2, 0),
}
FICHA_X = {
    "X1": (3, 1),
    "X2": (3, 2),
    "X3": (3, 3)
}
MOVIMIENTOS1 = {
    1: (0, -1),
    2: (-1, 0),
    3: (0, 1)
}
MOVIMIENTOS2 = {
    1: (-1, 0),
    2: (0, 1),
    3: (1, 0)
}
def tableron_act():
    tablero = [["." for _ in range(4)] for _ in range(4)]
    for pos in FICHA_O.values():
        tablero[pos[0]][pos[1]] = "O"
    for pos in FICHA_X.values():
        tablero[pos[0]][pos[1]] = "X"
    print()
    for fila in tablero:
        print(" ".join(fila))
    print()
    
def jugador1(op, id_ficha):
    clave = f"X{id_ficha}"
    if op in MOVIMIENTOS1 and clave in FICHA_X:
        i, j = FICHA_X[clave]
        di, dj = MOVIMIENTOS1[op]
        nueva_i, nueva_j = i + di, j + dj
        FICHA_X[clave] = (nueva_i, nueva_j)
def jugador2(op, id_ficha):
    clave = f"O{id_ficha}"
    if op in MOVIMIENTOS2 and clave in FICHA_O:
        i, j = FICHA_O[clave]
        di, dj = MOVIMIENTOS2[op]
        nueva_i, nueva_j = i + di, j + dj
        FICHA_O[clave] = (nueva_i, nueva_j)
def JUEGO():
    jugada = 0
    while jugada <= 2:
        tableron_act()
        print("Que ficha quieres mover 1,2 o 3?")
        id_ficha = input("Ingresa un número: ")
        print("elige ficha izquierda(1), arriba(2) o derecha(3)")
        op = int(input("Ingresa un número: "))
        jugador1(op, id_ficha)
        tableron_act()
        print("Que ficha quieres mover 1,2 o 3?")
        id_ficha = input("Ingresa un número: ")
        print("elige ficha izquierda(1), arriba(2) o derecha(3)")
        op = int(input("Ingresa un número: "))
        jugador2(op, id_ficha)
        tableron_act()
        jugada += 1
JUEGO()
