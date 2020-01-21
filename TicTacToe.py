board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_on = True
winner = None
player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    display_board()
    # player=input("Whos the player?")
    position = input("Choose a position from 1-9! \n")
    position = int(position) - 1
    while game_on:

        handle_turn(position)
        flip_player()
        display_board()
        if check_if_game_over():
            break;

        position = input("Choose a position from 1-9! \n")
        position = int(position) - 1
    global winner
    if winner == "X" or winner == "O":
        print(winner, "is the winner!")
    else:
        print("Tie Game!")


def handle_turn(position):
    # position = input("Choose a position from 1-9! \n")
    # position = int(position) - 1
    while board[position] == "-":
        if player == 'X':
            board[position] = 'X'
        if player == 'O':
            board[position] = 'O'


def check_if_game_over():
    if check_if_won() == True or check_if_tie() == True:
        return True


def check_if_won():
    # check rows
    row_winner = check_for_rows()
    # check cols
    col_winner = check_for_cols()
    # # check diags
    diag_winner = check_for_diag()
    if row_winner == True or col_winner == True or diag_winner == True:
        return True


def check_for_rows():
    r1 = board[0] == board[1] == board[2] != "-"
    r2 = board[3] == board[4] == board[5] != "-"
    r3 = board[6] == board[7] == board[8] != "-"
    global winner
    if r1:
        winner = board[0]
        return True
    if r2:
        winner = board[3]
        return True
    if r3:
        winner = board[6]
        return True
    return False

def check_for_cols():
    c1 = board[0] == board[3] == board[6] != "-"
    c2 = board[1] == board[4] == board[7] != "-"
    c3 = board[2] == board[5] == board[8] != "-"

    global winner
    if c1:
        winner = board[0]
        return True
    if c2:
        winner = board[1]
        return True
    if c3:
        winner = board[2]
        return True
    return False

def check_for_diag():
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True
    return False

def check_if_tie():
    for i in range(9):
        if board[i - 1] == "-":
            return False
    return True


def flip_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

play_game()