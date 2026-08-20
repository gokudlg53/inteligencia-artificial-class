tablero = [["O", ".", ".","."], ["O", ".", ".", "."], ["O", ".", ".", "."], [".", "X", "X", "X"]]
def tablero_lleno(tablero):
    print()
    for fila in tablero:
        for elem in fila:
            print(elem, end=" ")
        print()
    print()
def JUEGO():
    tablero_lleno(tablero)

    print("esto es una prueba")
JUEGO()
