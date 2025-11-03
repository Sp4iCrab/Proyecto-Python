import random

def menu():
    print("1.Iniciar juego")
    print("2.Salir")
    opcion = int(input("Seleccione una opción: "))

def menu_in_game():
    print("1.Pedir carta")
    print("2.Plantarse")
    print("3.Dinero")
    print("4.Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def limpiar(mano_jugador, mano_banca):
    mano_jugador.clear()
    mano_banca.clear()


def evaluar_mano(mano_jugador, mano_banca, dinero, apuesta):
    if sum(mano_jugador) > 21:
        limpiar(mano_jugador, mano_banca)
        print("Te has pasado de 21. Pierdes.")
        dinero -= apuesta

    elif sum(mano_banca) > 21:
        limpiar(mano_jugador, mano_banca)
        print("La banca se ha pasado de 21. Ganas.")
        dinero += apuesta

    elif sum(mano_jugador) == 21:
        limpiar(mano_jugador, mano_banca)
        print("¡21! Ganas.")
        dinero += apuesta

    elif sum(mano_banca) == 21:
        limpiar(mano_jugador, mano_banca)
        print("La banca tiene 21. Pierdes.")
        dinero -= apuesta

    elif sum(mano_jugador) == 21 and sum(mano_banca) == 21:
        limpiar(mano_jugador, mano_banca)
        print("Empate.")

    return dinero

def juego():
    menu()
    cartas = list(range(1, 12))
    mano_jugador = []
    mano_banca = []
    dinero = 100
    apuesta = 5

    while True:
        opcion = menu_in_game()
        if opcion == 1:
            carta = random.choice(cartas)
            mano_jugador.append(carta)
            mano_banca.append(random.choice(cartas))
            print(f"Mano de la banca: {mano_banca} (Total: {sum(mano_banca)})")
            print(f"Tu baraja: {mano_jugador} (Total: {sum(mano_jugador)})")
            dinero = evaluar_mano(mano_jugador, mano_banca, dinero, apuesta)
            
        elif opcion == 2:
            mano_banca.append(random.choice(cartas))
            print(f"Mano de la banca: {mano_banca} (Total: {sum(mano_banca)})")
            print(f"Tu baraja: {mano_jugador} (Total: {sum(mano_jugador)})")
            dinero = evaluar_mano(mano_jugador, mano_banca, dinero, apuesta)
            
        elif opcion == 3:
            print(f"Dinero actual: {dinero}")
        
        elif opcion == 4:
            break

        else:
            print("Opción no válida")

            
juego()

