from random import randrange

current_board = [['1', '2', '3'],
         ['4', 'X', '6'],
         ['7', '8', '9']
         ]
board_complete = False
valid = []
victory = [False, '']


def display_board(board):

    global victory

    divider_row = "+-------+-------+-------+"
    clear_row = "|       |       |       |"
    number_row_0 = f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |"
    number_row_1 = f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |"
    number_row_2 = f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |"

    print(divider_row, clear_row, number_row_0, clear_row, sep= "\n")
    print(divider_row, clear_row, number_row_1, clear_row, sep= "\n")
    print(divider_row, clear_row, number_row_2, clear_row, sep= "\n")
    print(divider_row)

    if victory[0]:
        return victory
    elif board_complete:
        return board_complete
    else:
        enter_move(board)

    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):

    global board_complete
    global victory

    if board_complete:
        return board_complete

    player_move = input("enter a number to place a 'O': ")
    valid_move = False

    try:
        if 0 < int(player_move) <= 9:
            for row in range(3):
                for col in range(3):
                    if board[row][col] == player_move:
                        board[row][col] = 'O'
                        valid_move = True


    except:
        print("invalid entry, enter an available number between 1-9:")
        enter_move(board)

    if valid_move == True:
        victory_for(board=board, sign='O')
        if victory[0]:
            display_board(board)
        else:
            draw_move(board)
    else:
        print("That space is taken, choose another one.")
        enter_move(board)

    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):

    global board_complete
    list(valid)
    valid.clear()

    for row in range(3):
        for col in range(3):
            if board[row][col] != 'O':
                if board[row][col] != 'X':
                    valid.append((row, col))
    if len(valid) == 1:
        board_complete = True
        display_board(board)

    return valid


    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    global victory

    if board[0][0] + board[0][1] + board[0][2] == sign * 3:
        victory = [True, sign]
        return victory

    elif board[1][0] + board[1][1] + board[1][2] == sign * 3:
        victory = [True, sign]
        return victory

    elif board[2][0] + board[2][1] + board[2][2] == sign * 3:
        victory = [True, sign]
        return victory

    elif board[0][0] + board[1][0] + board[2][0] == sign * 3:
        victory = [True, sign]
        return victory

    elif board[0][1] + board[1][1] + board[2][1] == sign * 3:
        victory = [True, sign]
        return victory

    elif board[0][2] + board[1][2] + board[2][2] == sign * 3:
        victory = [True, sign]
        return victory

    elif board[0][0] + board[1][1]+ board[2][2] == sign * 3:
        victory = [True, sign]
        return victory

    elif board[0][2] + board [1][1] + board[2][0] == sign * 3:
        victory = [True, sign]
        return victory
    else:
        return victory

    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


def draw_move(board):

    global victory

    print("X's turn:")

    list = make_list_of_free_fields(board)
    num = len(list)
    pos = ()

    for i in range(1):
        x = randrange(num)
        pos = list[x]

    current_board = board
    current_board[pos[0]][pos[1]] = 'X'

    victory_for(board=board, sign='X')

    display_board(board)

    # draws the computer's move and updates the board.

while current_board:
    if victory[0] == False and board_complete:
        print("game over - it is a draw.")
        break
    elif victory[0]:
        print(f"Congratulations {victory[1]}s, you have won!")
        break
    else:
        display_board(current_board)
