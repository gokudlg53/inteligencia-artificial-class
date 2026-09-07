import os , time
from math import inf
from rich.console import Console
from InquirerPy import inquirer
from InquirerPy.prompts.expand import ExpandChoice
from rich.progress import track
from rich.align import Align
from rich.panel import Panel

cont = 0
PROFUNDIDAD_IA = 3
console = Console()

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
        tablero[pos[0]][pos[1]] = "[blue]O[/blue]"   
    for pos in FICHAS_X.values():
        tablero[pos[0]][pos[1]] = "[red]X[/red]"  
    print()
    for fila in tablero:
        contenido = " ".join(fila)
        console.print(f"[yellow]{contenido}[/yellow]")

def elec_tablero():
    console.print("[blue]Bienvenido al juego de DODGEM")
    console.print("[blue]El objetivo del juego es mover tus fichas hasta el otro lado del tablero")
    input()
    limpiar_pantalla()
    while True:
        try:
            n = int(console.input("[underline blue]Ingrese el tamano del tablero(ejemplo 4,6,8):"))
            if n > 0 and n % 2 == 0 and n >= 4 and n <= 10:
                for i in track(range(100), description="Generando tablero..."):
                    time.sleep(0.03)
                console.print("[blue]juego cargado")
                time.sleep(0.5)
                limpiar_pantalla()
                return n
            console.print("[red]Error: El número debe ser par y mayor a 0 o menor que 10.")
        except ValueError:
            console.print("[red]Error: Ingrese un número entero válido.")

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
                with console.screen(style="bold red on blue") as screen:
                    text = Align.center(
                        f"[black]Jugador {turno} ha ganado el juego![/black]",
                        vertical="middle"
                    )
                    screen.update(Panel(text))
                    time.sleep(5)
                limpiar_pantalla()
                exit()
            return punto1, punto2

def jugada(n):
    vivas = sorted(int(clave[1:]) for clave in FICHAS_X.keys())
    id_ficha = inquirer.expand(
        message="¿Qué ficha quieres mover?",
        choices=[
            ExpandChoice(key=str(i), name=f"Ficha {i}", value=i)
            for i in vivas
        ],
    ).execute()

    op = inquirer.expand(
        message="elige como moverte:",
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
            console.print("[red]Movimiento inválido")
            console.input("[green]Presiona Enter para continuar...")

        else:
            ficha[clave] = (nueva_i, nueva_j)
            turno = 1 if turno == 2 else 2

    return(turno,puntaje)

# guarda la posicion de las fichas y el jugador en turno
def buscaGanador(punto1,punto2,N):
    n_piezas = N-1

    if punto2 == n_piezas:
        return "IA"

    elif punto1 == n_piezas:
        return "Humano"

    else:
        return None

def movimientosValidos(fichas_propias, fichas_rivales, movimientos, N, es_x):
    disponibles = []

    for clave, (i, j) in fichas_propias.items():
        for op, (di, dj) in movimientos.items():
            nueva_i, nueva_j = i + di, j + dj
            
            # si es_x es True, se fija en nueva_i; si es False, se fija en nueva_j
            if es_x and not (0 <= nueva_i <= N-1) or not es_x and not (0 <= nueva_j <= N-1):
                disponibles.append((clave, op, "gana", None))
            
            elif es_x and not (0 <= nueva_j <= N-1) or not es_x and not (0 <= nueva_i <= N-1) or (nueva_i, nueva_j) in fichas_propias.values() or (nueva_i, nueva_j) in fichas_rivales.values():
                continue   
            
            else:
                disponibles.append((clave, op, "normal", (nueva_i, nueva_j)))

    return disponibles


# revisa si el jugador tiene al menos un movimiento valido /R
def tieneMovimientos(fichas_propias, fichas_rivales, movimientos, N, es_x):
    disponibles = movimientosValidos(
        fichas_propias,
        fichas_rivales,
        movimientos,
        N,
        es_x
    )

    # si no hay movimientos disponibles el jugador esta bloqueado /R
    if len(disponibles) == 0:
        return False

    return True


def alfaBeta(fichas_x, fichas_o, punto1, punto2, leTocaAlaIA, profundidad, N, alfa, beta):
    global cont
    cont += 1

    ganador = buscaGanador(punto1, punto2, N)

    if ganador == "IA":
        return 1

    elif ganador == "Humano":
        return -1

    # si le toca a la IA y no tiene movimientos pierde por bloqueo /R
    if leTocaAlaIA and not tieneMovimientos(
        fichas_o,
        fichas_x,
        MOVIMIENTOS2,
        N,
        False
    ):
        return -1

    # si le toca al humano y no tiene movimientos la IA gana por bloqueo /R
    if not leTocaAlaIA and not tieneMovimientos(
        fichas_x,
        fichas_o,
        MOVIMIENTOS1,
        N,
        True
    ):
        return 1

    elif profundidad == 0:
        return evaluarTablero(fichas_o, fichas_x, punto1, punto2, N)

    if leTocaAlaIA:
        mejorPuntaje = -inf

        for clave, op, tipo, nueva_pos in movimientosValidos(
            fichas_o,
            fichas_x,
            MOVIMIENTOS2,
            N,
            es_x=False
        ):
            nuevas_o = dict(fichas_o)                            
            nuevo_punto2 = punto2

            if tipo == "gana":
                del nuevas_o[clave]
                nuevo_punto2 += 1

            else:
                nuevas_o[clave] = nueva_pos

            puntaje = alfaBeta(
                fichas_x,
                nuevas_o,
                punto1,
                nuevo_punto2,
                False,
                profundidad - 1,
                N,
                alfa,
                beta
            )

            mejorPuntaje = max(puntaje, mejorPuntaje)
            alfa = max(alfa, mejorPuntaje)

            if alfa >= beta:
                break

    else: 
        mejorPuntaje = inf

        for clave, op, tipo, nueva_pos in movimientosValidos(
            fichas_x,
            fichas_o,
            MOVIMIENTOS1,
            N,
            es_x=True
        ):
            nuevas_x = dict(fichas_x)
            nuevo_punto1 = punto1

            if tipo == "gana":
                del nuevas_x[clave]
                nuevo_punto1 += 1

            else:
                nuevas_x[clave] = nueva_pos

            puntaje = alfaBeta(
                nuevas_x,
                fichas_o,
                nuevo_punto1,
                punto2,
                True,
                profundidad - 1,
                N,
                alfa,
                beta
            )

            mejorPuntaje = min(puntaje, mejorPuntaje)
            beta = min(beta, mejorPuntaje)

            if alfa >= beta:
                break

    return mejorPuntaje

def mejorMovimiento(n, punto1, punto2):
    mejorPuntaje = -inf
    movimiento = None

    for clave, op, tipo, nueva_pos in movimientosValidos(
        FICHAS_O,
        FICHAS_X,
        MOVIMIENTOS2,
        n,
        es_x=False
    ):
        nuevas_o = dict(FICHAS_O)
        nuevo_punto2 = punto2

        if tipo == "gana":
            del nuevas_o[clave]
            nuevo_punto2 += 1

        else:
            nuevas_o[clave] = nueva_pos

        puntaje = alfaBeta(
            FICHAS_X,
            nuevas_o,
            punto1,
            nuevo_punto2,
            False,
            PROFUNDIDAD_IA - 1,
            n,
            -inf,
            inf
        )

        print(f"{clave} op={op} ptje: {puntaje}")

        if puntaje > mejorPuntaje:
            mejorPuntaje = puntaje
            movimiento = (int(clave[1:]), op)

    return movimiento

def jugada_ia(n, punto1, punto2):
    global cont

    movimiento = mejorMovimiento(n, punto1, punto2)

    print(f"Número de tableros revisados: {cont}")
    cont = 0

    if movimiento is None:
        return None, None

    return movimiento

def evaluarTablero(fichas_o, fichas_x, punto1, punto2, N):
    avance_o = sum(j for (_, j) in fichas_o.values())
    avance_x = sum((N - 1 - i) for (i, _) in fichas_x.values())

    diferencia_puntos = (punto2 - punto1) * 2

    bruto = diferencia_puntos + (avance_o - avance_x) * 0.1

    return bruto / (abs(bruto) + 10)

def obtener_estado(turno):
    posiciones_x = tuple(sorted(FICHAS_X.values()))
    posiciones_o = tuple(sorted(FICHAS_O.values()))

    return posiciones_x, posiciones_o, turno

# inicia el juego y controla el flujo del mismo
def JUEGO():
    #valores iniciales de turno y puntajes
    turno = 1
    win1, win2 = 0, 0

    historial = {
        obtener_estado(turno):1
    } # guarda cuantas veces aparece cada estado del juego

    while True:
        limpiar_pantalla()
        tableron_act(n)

        console.print(
            "es turno de el jugador",
            turno,
            style="bold green"
        )

        console.print(
            "[red]X:",
            win1,
            "[blue]O:",
            win2
        )

        # revisa si el jugador que comienza el turno esta bloqueado /R
        if turno == 1:
            puede_mover = tieneMovimientos(
                FICHAS_X,
                FICHAS_O,
                MOVIMIENTOS1,
                n,
                True
            )

        else:
            puede_mover = tieneMovimientos(
                FICHAS_O,
                FICHAS_X,
                MOVIMIENTOS2,
                n,
                False
            )

        # si el jugador no tiene movimientos legales pierde inmediatamente /R
        if not puede_mover:
            if turno == 1:
                console.print(
                    "[bold blue]La IA ha ganado por bloqueo.[/bold blue]"
                )

            else:
                console.print(
                    "[bold red]El jugador ha ganado por bloqueo.[/bold red]"
                )

            return

        if turno == 1:
            id_ficha, op = jugada(n)

        else:
            id_ficha, op = jugada_ia(n, win1, win2)

            # si la IA no tiene movimientos validos pierde por bloqueo /R
            if id_ficha is None:
                console.print(
                    "[bold red]El jugador ha ganado por bloqueo.[/bold red]"
                )
                return

        turno_anterior = turno # guarda el turno actual para saber si la jugada fue valida

        turno, puntaje = jugador(
            op,
            id_ficha,
            turno,
            n
        )

        tableron_act(n)

        win1, win2 = ganador(
            puntaje,
            turno,
            win1,
            win2,
            n
        )

        if turno != turno_anterior: # solo se registra el estado si el turno cambio, es decir, si hubo una jugada valida
            estado = obtener_estado(turno)

            historial[estado] = historial.get(
                estado,
                0
            ) + 1  # aumenta en 1 la cantidad de veces que aparece este mismo estado

            if historial[estado] >= 3:  # si el mismo tablero con el mismo turno aparece 3 veces, la partida termina en empate
                console.print(
                    "[bold yellow]Empate por repeticion de jugadas.[/bold yellow]"
                )
                return


limpiar_pantalla()
n = elec_tablero()
FICHAS_O, FICHAS_X = Pos_ficha(n)
JUEGO()
