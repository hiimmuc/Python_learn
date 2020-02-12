# setting global variables
size = 3
condition_win = 3
player1_name = ""
player2_name = ""
current_player = 'X'
game_still_going = True
winner = None

# set up information
while True:
    size = int(input("Enter the size of map (n x n): "))
    condition_win = int(input("Condition to win: "))
    if (condition_win <= size):
        break
    else:
        print("set up map failed, try again....")

player1_name = input("Enter current_playerX's name: ")
player2_name = input("Enter current_playerO's name: ")
# create board


def init_board(row, col):
    board = [['0' for i in range(row)] for i in range(col)]
    for i in range(col):
        for j in range(row):
            board[i][j] = ' | -'
    return board


board = init_board(size, size)

# board[i][j][3] is '-' for the blank space

#  display board


def display_board(board_, row, col):
    board_map = "\n"
    for i in range(col):
        for j in range(row):
            board_map += f"{board_[i][j]}"
        board_map += ' |\n'
    print(board_map)


#  playgame


def play_game():
    global game_still_going
    global winner
    global current_player

    # init board:
    # board = init_board(size, size)
    display_board(board, size, size)
    # play:
    while game_still_going:

        #
        handle_turn(current_player)
        display_board(board, size, size)

        #
        if check_if_game_is_end():
            game_still_going = False
        #
        flip_current_player()
        #

    # game has ended:
    if check_if_win():
        flip_current_player()
        winner = current_player
        if winner == 'X' or winner == 'O':
            print(winner + " won!!!")
            if winner == 'X':
                print(f"{player1_name} beats {player2_name} !!!")
            else:
                print(f"{player2_name} beats {player1_name} !!!")
    elif check_if_tie():
        print("TIE.")


#  handle each turn


def enter_pos(current_player_now):
    global board
    try:
        while True:
            position = list()
            coordinate = input(
                f" -> {current_player_now.upper()}'s turn: ")
            position = coordinate.split(' ')
            if 1 <= int(position[0]) <= size and 1 <= int(position[1]) <= size:
                if board[int(position[0]) - 1][int(position[1]) - 1][3] == '-':
                    return position
                else:
                    print("Invalid position\nChoose again")
            else:
                print("Invalid position\nChoose again")
    except:
        print("Invalid input")
        enter_pos(current_player_now)


def handle_turn(current_player_now):
    try:
        position = enter_pos(current_player_now)
        pos_x = int(position[0]) - 1
        pos_y = int(position[1]) - 1
        board[pos_x][pos_y] = f" | {current_player_now.upper()}"
    except:
        print("Type again")
        handle_turn(current_player_now)


#  check win:
#  ->check cols
#  ->check rows
#  ->check diagonals
def check_if_win():
    if check_rows(size) or check_cols(size) or check_diagonals(size):
        return True
    else:
        return False


def check_rows(rows):
    result = [False for i in range(rows)]
    result_count = [1 for i in range(rows)]

    for row in range(rows):
        for temp in range(size - condition_win + 1):
            for count in range((temp + 1), condition_win):
                result[row] = board[row][count][3] == board[row][count - 1][3] != '-'
                if result[row]:
                    result_count[row] += 1
    for i in range(rows):
        if result[i] and result_count[i] == condition_win:
            return True

    return False


def check_cols(cols):
    result = [False for i in range(size)]
    result_count = [1 for i in range(size)]
    for col in range(cols):
        for temp in range(size - condition_win + 1):
            for count in range((temp + 1), condition_win):
                result[col] = board[count][col][3] == board[count - 1][col][3] != '-'
                if result[col]:
                    result_count[col] += 1
    for i in range(size):
        if result[i] and (result_count[i] == condition_win):
            return True

    return False


def check_diagonals(size):
    # number of diagonals
    able_diagonals = (1 + (size - condition_win) * 2) * 2
    # number of diagonal start in same edge with same direction
    num_dia = 1 + size - condition_win

    result = [False for i in range(able_diagonals)]
    result_count = [1 for i in range(able_diagonals)]
    # left to right check
    # loop for result list
    for count in range(able_diagonals // 2):
        # loop for the increasing places horizontally
        for temp in range(num_dia):
            # loop for the elements in diagonals
            for index in range(temp+1, condition_win):
                result[count] = board[index][index +
                                             temp][3] == board[index - 1][index + temp - 1][3]
                if result[count]:
                    result_count[count] += 1
        # loop for downward check
        for temp in range(1, num_dia):
            # loop for the elements in diagonals
            for index in range(temp+1, condition_win):
                result[count] = board[index +
                                      temp][index][3] == board[index + temp - 1][index - 1][3] != '-'
                if result[count]:
                    result_count[count] += 1
    # right to left check
    # reverse the board
    for row in range(size):
        board[row].reverse()

    for count in range(able_diagonals // 2, able_diagonals):
        # loop for the increasing places horizontally
        for temp in range(num_dia):
            # loop for the elements in diagonals
            for index in range(temp+1, condition_win):
                result[count] = board[index][index +
                                             temp][3] == board[index - 1][index + temp - 1][3] != '-'
                if result[count]:
                    result_count[count] += 1
        # loop for downward check
        for temp in range(1, num_dia):
            # loop for the elements in diagonals
            for index in range(temp+1, condition_win):
                result[count] = board[index +
                                      temp][index][3] == board[index + temp - 1][index - 1][3]
                if result[count]:
                    result_count[count] += 1

    # take the board back
    for row in range(size):
        board[row].reverse()

    for i in range(able_diagonals):
        if result[i] and result_count[i] == condition_win:
            return True

    return False
# check tie


def check_if_tie():
    full = True
    for i in range(size):
        for j in range(size):
            if board[i][j][3] == '-':
                full = False

    if not check_if_win() and full:

        return True
    else:
        return False
#


def check_if_game_is_end():
    if check_if_win() or check_if_tie():
        return True
    else:
        return False


#  flip current_player


def flip_current_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


# begin:...

play_game()

# board = [[' | O', ' | X', ' | O', ' | X'],
#          [' | O', ' | X', ' | O', ' | O'],
#          [' | X', ' | O', ' | X', ' | O'],
#          [' | X', ' | O', ' | O', ' | X']]

# print(check_rows(size))
# print(check_cols(size))
# print(check_diagonals(size))
# print(check_if_win())
# print(check_if_tie())
# print(check_if_game_is_end())
