#tablero = [
#    ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
#    ['b1', 'b2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
#    ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
#    ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
#    ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
#    ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
#]

mappeo = {
    "a1": 0, "a2": 1, "a3": 2, "a4": 3, "a5": 4, "a6": 5, "a7": 6, "a8": 7,
    "b1": 0, "b2": 1, "b3": 2, "b4": 3, "b5": 4, "b6": 5, "b7": 6, "b8": 7,
    # TODO(Marcos): COMPLETAR ESTA MIERDA
}

tablero = [
    'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R',
    'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
    '0', '0', '0', '0', '0', '0', '0', '0',
    '0', '0', '0', '0', '0', '0', '0', '0',
    '0', '0', '0', '0', '0', '0', '0', '0',
    '0', '0', '0', '0', '0', '0', '0', '0',
    'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
    'R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R',
]

turno_jugador_1 = True
while True:
    if turno_jugador_1:
        print("Turno jugador 1: ")
    else:
        print("Turno jugador 2: ")

    posicion = input("que pieza mover?")
    print("la pieza es: ", tablero[mappeo[posicion]])
    nueva_posicion = input("a donde mover la pieza?")

    for fila in range(0, 8):
        for columna in range(0, 8):
            if columna != 7:
                print(tablero[fila * 8 + columna], end =" ")
            else:
                print(tablero[fila * 8 + columna])
    turno_jugador_1 = not turno_jugador_1







"""
Jugador -> 16 piezas

Pieza
   posicion: 
   
   tipo: Alfil, caballo, torre, rey, reina, peon
   regla segun tipo

Jugador 1:
tiene piezas que estan en cierta posicion

por turno: (posicion de la pieza que quiere mover, la posicion donde va a estar la pieza)
moviento = (i2, i3)
es_valido = validar_movimiento(movimiento)
if es_valido:
    moverlo
else:
    algo mas
"""