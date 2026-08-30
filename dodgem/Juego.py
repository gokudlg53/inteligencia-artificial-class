import os , time
from rich.console import Console
from InquirerPy import inquirer
from InquirerPy.prompts.expand import ExpandChoice
from rich.progress import track
console = Console()
# indica posiciones de las fichas
n = 4
#como el nombre indica limpia el tablero
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
def Pos_ficha(N):
    FICHAS_O = {}
    FICHAS_X = {}
    for i in range(N -1):
        FICHAS_O[f"O{i+1}"] = (i, 0)
        FICHAS_X[f"X{i+1}"] = (N-1, i+1)
    return FICHAS_O, FICHAS_X
# indica los movimientos posibles para cada jugador
MOVIMIENTOS1, MOVIMIENTOS2 = {
    1: (0, -1),
    2: (-1, 0),
    3: (0, 1)
}, {
    1: (-1, 0),
    2: (0, 1),
    3: (1, 0)
}
# muestra el tablero actualizado
def tableron_act(N):
    tablero = [["." for _ in range(N)] for _ in range(N)]
    for pos in FICHAS_O.values():
        tablero[pos[0]][pos[1]] = "O"   
    for pos in FICHAS_X.values():
        tablero[pos[0]][pos[1]] = "X"  
    print()
    for fila in tablero:
        console.print("[yellow]"+" ".join(fila)+"\r")
def elec_tablero():
    console.print("[blue]Bienvenido al juego de DODGEM\r")
    console.print("[blue]El objetivo del juego es mover tus fichas hasta el otro lado del tablero\r")
    input()
    limpiar_pantalla()
    while True:
        try:
            n = int(console.input("[underline blue]Ingrese el tamano del tablero(ejemplo 4,6,8):\r"))
            if n > 0 and n % 2 == 0 and n >= 4 and n <= 10:
                for i in track(range(100), description="Generando terreno..."):
                    time.sleep(0.03)
                console.print("[blue]juego cargado\r")
                time.sleep(0.5)
                limpiar_pantalla()
                return n
            console.print("[red]Error: El número debe ser par y mayor a 0 o menor que 10.\r")
        except ValueError:
            console.print("[red]Error: Ingrese un número entero válido.\r")
# revisa si un jugador ha ganado el juego
def ganador(punto,jugador,punto1,punto2,n):
            # turno representa el jugador que ha ganado el punto, win representa si se ha ganado un punto
            #este es un ajuste para que las fichas coincida con el puntaje max
            n-=1
            #diccionario de fichas y movimientos
            turno = jugador if jugador == 2 else 1
            turno = 1 if turno == 2 else 2
            win = punto if punto == 1 else 0
            #restricciones de puntaje maximo y actualizacion de puntajes
            if turno == 1 and not win == 0:
                punto1 += win
            elif turno == 2 and not win == 0:
                punto2 += win
            if punto1 == n or punto2 == n:
                console.print("Jugador", turno, "ha ganado el juego!", style="bold green")
                exit()
            return punto1, punto2
def jugada(n):
    id_ficha = inquirer.expand(
        message="¿Qué ficha quieres mover?",
        choices=[
            ExpandChoice(key=str(i), name=f"Ficha {i}", value=i)
            for i in range(1,n)
        ],
    ).execute()
    op = inquirer.expand(
        message="elige como moverte: izquierda(1), arriba(2) o derecha(3)",
        choices=[
            ExpandChoice(key="1",name="izquierda",value=1),
            ExpandChoice(key="2",name="arriba",value=2),
            ExpandChoice(key="3",name="derecha",value=3)
        ],
    ).execute()
    return id_ficha,op
# realiza el movimiento del jugador y actualiza el turno
def jugador(op, id_ficha,turno,N):
    #diccionario de fichas y movimientos
    puntaje=0
    ficha = FICHAS_X if turno == 1 else FICHAS_O
    movimientos = MOVIMIENTOS1 if turno == 1 else MOVIMIENTOS2
    # esto indica la clave de la ficha que se va a mover según el turno y el id de la ficha
    clave = f"X{id_ficha}" if turno == 1 else f"O{id_ficha}"
    #se realiza el movimiento si es válido
    if op in movimientos and clave in ficha:
        i, j = ficha[clave]
        di, dj = movimientos[op]
        nueva_i, nueva_j = i + di, j + dj
        # muestra las restricciones de movimiento y actualiza la posición de la ficha si es válido
        if turno == 1 and not (0 <= nueva_i <= N- 1) or turno == 2 and not (0 <= nueva_j <= N-1):
            del ficha[clave]
            puntaje =1
            turno = 1 if turno == 2 else 2
            #restricciones de movimientos en caso de no haber movimiento valido
        elif turno == 1 and not (0 <= nueva_j <= N-1) or turno == 2 and not (0 <= nueva_i <= N-1) or (nueva_i, nueva_j) in FICHAS_X.values() or (nueva_i, nueva_j) in FICHAS_O.values():
            console.print("[red]Movimiento inválido\r")
            console.input("[green]Presiona Enter para continuar...\r")
        else:
            ficha[clave] = (nueva_i, nueva_j)
            turno = 1 if turno == 2 else 2
    return(turno,puntaje)
# inicia el juego y controla el flujo del mismo
def JUEGO():
    #valores iniciales de turno y puntajes
    turno = 1
    win1, win2 = 0, 0
    while True:
        limpiar_pantalla()
        tableron_act(n)
        console.print("es turno de el jugador", turno, style="bold green")
        console.print("X:", win1, "O:", win2, style="bold blue")
        id_ficha, op = jugada(n)
        turno, puntaje = jugador(op, id_ficha, turno, n)
        tableron_act(n)
        win1, win2 = ganador(puntaje, turno,win1,win2,n)
limpiar_pantalla()
n = elec_tablero()
FICHAS_O, FICHAS_X = Pos_ficha(n)
JUEGO()
