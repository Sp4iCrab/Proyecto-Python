# Funcion para el tablero
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


# Funcion para el puntaje
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              PUNTAJE       ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")

# Funcion para saber si algun jugador gano
def check_win(player_pos, cur_player):

    # Todas las combinaciones ganadoras posibles
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop para detectar si alguna combinacion ganadora se cumpke
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):

            # Retornar True si hay alguna combinacion ganadora
            return True
    # Retornar false si no hay ninguna combinacion ganadora     
    return False       

# Funcion para detectar empate
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       

# Funcion para un solo juego
def single_game(cur_player):

    # Representa el juego de Tic Tac Toe
    values = [' ' for x in range(9)]

    # Almacena las posiciones ocupadas por X y O
    player_pos = {'X':[], 'O':[]}

    # El loop del juego para un solo juego
    while True:
        print_tic_tac_toe(values)
    
        # Bloque Try-Exception para el input MOVE
        try:
            print("Jugador ", cur_player, " turno. Que campo? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Input incorrecto, intentalo otra vez")
            continue

        # Chequeo para el MOVE input
        if move < 1 or move > 9:
            print("Input incorrecto, intentalo otra vez")
            continue

        # Chequeo si el campo no esta ocupado ya
        if values[move-1] != ' ':
            print("Campo ya esta ocupado")
            continue

        # Actualizacion de informacion

        # Actualizacion de estado 
        values[move-1] = cur_player

        # Actualizacion la posicion del jugador
        player_pos[cur_player].append(move)

        # Llamada de funcion para chequear ganador
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Jugador ", cur_player, " gano el juego")     
            print("\n")
            return cur_player

        # Llamada de funcion para empate
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Empate")
            print("\n")
            return 'D'

        # Cambiar movimientos de jugador
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

if __name__ == "__main__":

    print("Player 1")
    player1 = input("Ingrese nombre : ")
    print("\n")

    print("Player 2")
    player2 = input("Ingrese nombre : ")
    print("\n")

    # Almacena el jugador que escogio X y O
    cur_player = player1

    # Almacena las decisiones de los jugadores
    player_choice = {'X' : "", 'O' : ""}

    # Almacena las opciones
    options = ['X', 'O']

    # Almacena el puntaje
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    # Loop de juego para juegos consecutivos
    # El loop sigue hasta que los jugadores abandonen
    while True:

        # Menu
        print("Opciones", cur_player)
        print("1 para X")
        print("2 para O")
        print("3 para salir")

        # Bloque Try-Exception para input CHOICE
        try:
            choice = int(input())   
        except ValueError:
            print("Input incorrecto, intentalo otra vez\n")
            continue

        # Condiciones para elecciones del jugador
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("Puntaje final")
            print_scoreboard(score_board)
            break  

        else:
            print("Input incorrecto, intentalo otra vez\n")

        # Almacena el ganador para un solo juego
        winner = single_game(options[choice-1])

        # Edita el scoreboard acorde al ganador
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        # Cambia de jugador que elegio X u O
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1