import random

game_still_going = True
win = 0
v_spliter = ' | '
empty_dot = '•'


# board = [empty_dot, empty_dot, empty_dot,
#          empty_dot, empty_dot, empty_dot,
#          empty_dot, empty_dot, empty_dot]

board = [empty_dot for _ in range(9)]

def who_the_first():
    roll = random.randint(0, 1)
    if roll == 0:
        print('Computers turn first')
        computer_turn = random.randint(0, 8)
        board[computer_turn] = "X"
        return "X", "O"
    else:
        print('The first turn is yours')
        return "O", "X"

def display_board():
    print(board[0] + v_spliter + board[1] + v_spliter + board[2])
    print(board[3] + v_spliter + board[4] + v_spliter + board[5])
    print(board[6] + v_spliter + board[7] + v_spliter + board[8])

def check_is_it_available(position):
    for position in board:
        if position != empty_dot:
            print('Not available, try another')
            return 0
        else:
            return 1

def if_win():
    def checking_(n0, n1, n2, n3, n4, n5, n6, n7, n8):
        arg01 = board[n0] == board[n1] == board[n2] != empty_dot
        arg02 = board[n3] == board[n4] == board[n5] != empty_dot
        arg03 = board[n6] == board[n7] == board[n8] != empty_dot

        if arg01 or arg02 or arg03:
            print('win')
            exit(0)

    def check_rows():
        checking_(0, 1, 2, 3, 4, 5, 6, 7, 8)

    def check_col():
        checking_(0, 3, 4, 1, 4, 7, 2, 5, 8)

    def check_dgnls():
        checking_(0, 4, 8, 2, 4, 6, 2, 4, 6)

    check_rows()
    check_col()
    check_dgnls()


def if_tie():
    pass


def flip_player():
    return



def check_if_gameover():
    if_win()
    if_tie()

def check_input():
    while True:
        position = input("Choose the position 1-9\n")
        try:
            position = int(position)
            if 0 < position < 10:
                return position - 1

        except:
            print('Wrong type')


def handle_turn(player_sign):
    position = check_input()
    check_is_it_available(position)
    
    board[position] = player_sign
    display_board()

def comp_turn(computer_sign):
    print("comp turn")

def play_game():
    computer_sign, player_sign = who_the_first()
    display_board()

    while game_still_going == True:
        check_if_gameover()
        handle_turn(player_sign)
        comp_turn(computer_sign)


play_game()


# board
# display_board
# play_game
# user input
    # check is it possible to enter here
# check win
    # check rows
    # check columns
    # check diagonalies
# check tie
# flip player