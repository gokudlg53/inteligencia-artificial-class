# inteligencia-artificial-class
10 DODGEM
10.1 RESTRICCIONES DEL PROYECTO
Tablero de tamaño n × n, con n par y n ≥ 4. En consecuencia, los tamaños permitidos son 4 × 4,
6 × 6, 8 × 8, etc. Cada jugador comienza con n−1 fichas.
10.2 REGLAS DEL JUEGO
▪ Configuración inicial: A ubica n−1 fichas en la columna 1, ocupando las filas 1 hasta n−1.
B ubica n−1 fichas en la fila n, ocupando las columnas 2 hasta n. La casilla (n, 1) queda vacía.
A realiza la primera jugada.
▪ Dirección de A: el avance de A es hacia la derecha. Una ficha A puede moverse una casilla
a la derecha o lateralmente una casilla hacia arriba o hacia abajo. Nunca puede moverse
hacia la izquierda.
▪ Dirección de B: el avance de B es hacia arriba. Una ficha B puede moverse una casilla hacia
arriba o lateralmente una casilla hacia la izquierda o hacia la derecha. Nunca puede moverse
hacia abajo.
▪ Destino dentro del tablero: la casilla destino debe estar vacía. No existen capturas y
ninguna ficha puede saltar sobre otra.
▪ Salida de A: una ficha A situada en la columna n puede salir del tablero mediante un
movimiento hacia la derecha. Una vez fuera, se retira definitivamente de la partida. No puede
salir por los bordes superior o inferior.
▪ Salida de B: una ficha B situada en la fila 1 puede salir del tablero mediante un movimiento
hacia arriba. Una vez fuera, se retira definitivamente. No puede salir por los bordes izquierdo
o derecho.
▪ Victoria por salida: un jugador gana inmediatamente cuando consigue sacar del tablero
todas sus fichas.
▪ Bloqueo: si al comenzar su turno un jugador todavía tiene fichas en el tablero pero no posee
ningún movimiento legal, pierde. No se permite pasar.
▪ Repetición para el proyecto: si la misma configuración del tablero con el mismo jugador en
turno aparece por tercera vez, la partida termina en empate. Las condiciones de victoria o
derrota anteriores tienen prioridad si se cumplen antes.
10.3 PARTIDA SIMULADA
La siguiente simulación utiliza un tablero de 4 × 4 y tiene únicamente fines ilustrativos. Las
jugadas se muestran en orden y el tablero se presenta después de cada acción.
18
Configuración inicial
1 2 3 4
1 A · · ·
2 A · · ·
3 A · · ·
4 · B B B
Turno 1: A mueve de (2, 1) a (2, 2).
1 2 3 4
1 A · · ·
2 · A · ·
3 A · · ·
4 · B B B
Turno 2: B mueve de (4, 2) a (3, 2).
1 2 3 4
1 A · · ·
2 · A · ·
3 A B · ·
4 · · B B
Turno 3: A mueve de (2, 2) a (2, 3).
1 2 3 4
1 A · · ·
2 · · A ·
3 A B · ·
4 · · B B
Turno 4: B mueve de (4, 3) a (3, 3).
1 2 3 4
1 A · · ·
2 · · A ·
3 A B B ·
4 · · · B
Turno 5: A mueve de (2, 3) a (1, 3).
1 2 3 4
1 A · A ·
2 · · · ·
3 A B B ·
4 · · · B
Turno 6: B mueve de (4, 4) a (3, 4).
1 2 3 4
1 A · A ·
2 · · · ·
3 A B B B
4 · · · ·
Turno 7: A mueve de (3, 1) a (2, 1).
1 2 3 4
1 A · A ·
2 A · · ·
3 · B B B
4 · · · ·
19
Turno 8: B mueve de (3, 4) a (2, 4).
1 2 3 4
1 A · A ·
2 A · · B
3 · B B ·
4 · · · ·
Turno 9: A mueve de (2, 1) a (2, 2).
1 2 3 4
1 A · A ·
2 · A · B
3 · B B ·
4 · · · ·
Turno 10: B mueve de (2, 4) a (1, 4).
1 2 3 4
1 A · A B
2 · A · ·
3 · B B ·
4 · · · ·
Turno 11: A mueve de (1, 1) a (1, 2).
1 2 3 4
1 · A A B
2 · A · ·
3 · B B ·
4 · · · ·
Turno 12: B mueve de (3, 3) a (2, 3).
1 2 3 4
1 · A A B
2 · A B ·
3 · B · ·
4 · · · ·
Resultado: tras el turno 12 de B, A conserva tres fichas pero ninguna puede avanzar ni
desplazarse lateralmente a una casilla libre; A pierde por bloqueo y B gana.
