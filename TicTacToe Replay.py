board = [ "-","-","-",
          "-","-","-",
          "-","-","-",]


game_still_going = True


winner = None


current_player = "X"


def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose position from 1-9: ")

    valid = False        
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose position from 1-9: ")


        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You Can't go There. Choose Other Place Still Empty")

    board[position] = player

    display_board()


def check_if_game_over():
    check_if_winner()
    check_if_tie()


def check_rows():
    global game_still_going
    rows_1 = board[0] == board[1] == board[2] != "-"
    rows_2 = board[3] == board[4] == board[5] != "-"
    rows_3 = board[6] == board[7] == board[8] != "-"


    if rows_1 or rows_2 or rows_3:
        game_still_going = False
        

    if rows_1:
        return board[0]
    elif rows_2:
        return board[3]
    elif rows_3:
        return board[6]
    return


def check_columns():
    global game_still_going
    columns_1 = board[0] == board[3] == board[6] != "-"
    columns_2 = board[1] == board[4] == board[7] != "-"
    columns_3 = board[2] == board[5] == board[8] != "-"


    if columns_1 or columns_2 or columns_3:
        game_still_going = False
        

    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"


    if diagonals_1 or diagonals_2:
        game_still_going = False
        

    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


def check_if_winner():
    global winner

    rows_winner = check_rows()

    columns_winner = check_columns()

    diagonals_winner = check_diagonals()
    if rows_winner:
        winner = rows_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

  
def display_board():
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():


    display_board()


    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()
        
        flip_player()


    if winner == "X" or winner == "O":
        print(winner + " WON")
    elif winner == None:
        print("Tie")
        

play_game()
 
          
