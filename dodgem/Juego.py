
tablero = [["O", ".", ".","."], ["O", ".", ".", "."], ["O", ".", ".", "."], [".", "X", "X", "X"]]
def tablero_lleno(tablero):
    print()
    for fila in tablero:
        for elem in fila:
            print(elem, end=" ")
        print()
    print()
def jugadas(opcion):
    if opcion == 1:
        tablero[i][j] = "."
        j=j-1
        tablero[i][j] = "X"
    elif opcion == 2:
        tablero[i][j] = "X"
        i=i+1
        tablero[i][j] = "X"
    elif opcion == 3:
        tablero[i][j] = "."
        j=j+1
        tablero[i][j] = "X"
def JUEGO():
    tablero_lleno(tablero)

    print("esto es una prueba")
JUEGO()
