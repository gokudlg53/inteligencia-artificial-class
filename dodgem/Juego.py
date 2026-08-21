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
def ganador(punto,jugador):
    if punto == 3:
        print(f"El jugador {jugador} ha ganado el juego!")
        exit()
def jugador(op, id_ficha,turno):
    #diccionario de fichas y movimientos
    puntaje=0
    ficha = FICHA_X if turno == 1 else FICHA_O
    movimientos = MOVIMIENTOS1 if turno == 1 else MOVIMIENTOS2
    clave = f"X{id_ficha}" if turno == 1 else f"O{id_ficha}"
    #se realiza el movimiento si es válido
    if op in movimientos and clave in ficha:
        i, j = ficha[clave]
        di, dj = movimientos[op]
        nueva_i, nueva_j = i + di, j + dj
        #elimina la ficha si se sale del tablero 
        if turno == 1 and not (0 < nueva_i <= 3):
            del ficha[clave]
            puntaje =1
            turno = 1 if turno == 2 else 2
        elif turno == 2 and not (0 < nueva_j <= 3):
            del ficha[clave]
            puntaje =1
            turno = 1 if turno == 2 else 2
        elif (nueva_i, nueva_j) in FICHA_X.values() or (nueva_i, nueva_j) in FICHA_O.values():
            print("Movimiento inválido: Casilla ocupada por otra pieza.")
        #en caso de ser valido el movimiento se realiza y se cambia de turno
        else:
            ficha[clave] = (nueva_i, nueva_j)
            turno = 1 if turno == 2 else 2
    return(turno,puntaje)
def JUEGO():
    turno = 1
    puntos = 0
    while True:
        tableron_act()
        print(f"Turno del jugador {turno}")
        print("Que ficha quieres mover 1,2 o 3?")
        id_ficha = input("Ingresa un numero: ")
        print("elige ficha izquierda(1), arriba(2) o derecha(3)")
        op = int(input("Ingresa un numero: "))
        turno, puntaje = jugador(op, id_ficha, turno)
        tableron_act()
        ganador(puntaje, turno)
JUEGO()
