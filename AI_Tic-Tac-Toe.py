from random import randint

def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

def board(matrix):
    print("---------")
    print("| " + matrix[0][2] + " " + matrix[1][2] + " " + matrix[2][2] + " |")
    print("| " + matrix[0][1] + " " + matrix[1][1] + " " + matrix[2][1] + " |")
    print("| " + matrix[0][0] + " " + matrix[1][0] + " " + matrix[2][0] + " |")
    print("---------")

def board_change(matrix, coord):
    if turn % 2 == 0:
        matrix[coord[0] - 1][coord[1] - 1] = "X"
    else:
        matrix[coord[0] - 1][coord[1] - 1] = "O"
    if ((player_1 == "easy") & (turn % 2 == 0)) | ((player_2 == "easy") & (turn % 2 != 0)):
        print('Making move level "easy"')
    elif ((player_1 == "medium") & (turn % 2 == 0)) | ((player_2 == "medium") & (turn % 2 != 0)):
        print('Making move level "medium"')
    return matrix

def outcome_check(matrix):
    X_win = 0
    O_win = 0
    spaces = 0
    for x in range(3):
        if (matrix[0][x] == matrix[1][x]) & (matrix[0][x] == matrix[2][x]):
            if (matrix[0][x] == "X"):
                X_win += 1
                break
            elif (matrix[0][x] == "O"):
                O_win += 1
                break
        elif (matrix[x][0] == matrix[x][1]) & (matrix[x][0] == matrix[x][2]):
            if (matrix[x][0] == "X"):
                X_win += 1
                break
            elif (matrix[x][0] == "O"):
                O_win += 1
                break
    if (matrix[0][0] == matrix[1][1]) & (matrix[0][0] == matrix[2][2]) | (
            matrix[0][2] == matrix[1][1]) & (
            matrix[0][2] == matrix[2][0]):
        if (matrix[1][1] == "X"):
            X_win += 1
        elif (matrix[1][1] == "O"):
            O_win += 1
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == " ":
                spaces +=1
    return X_win, O_win, spaces

def user():
    coord = input("Enter the coordinates: ")
    coord = coord.replace(" ", "")
    if (is_int(coord) == False):
        print("You should enter numbers!")
        pass
    else:
        coord = coord.replace("", " ")
        coord = coord.split()
        for k in range(len(coord)):
            coord[k] = int(coord[k])
    return coord

def easy():
    coord = [randint(1, 3), randint(1, 3)]
    for k in range(len(coord)):
        coord[k] = int(coord[k])
    return coord

def medium(matrix):
    temp_matrix_1 = [[], [], []]
    temp_matrix_2 = [[], [], []]
    on = 0
    count = 0
    coords = []
    for i in range(3):
        for j in reversed(range(3)):
            temp_matrix_1[j].append(matrix[i][j])
    diagonals = [matrix[i][i] for i in range(len(matrix))], [row[-i - 1] for i, row in enumerate(matrix)]
    for k in range(3):
        if ((matrix[k].count(" ") == 1) & ((matrix[k].count("X") == 2) | (matrix[k].count("O") == 2))):
            coords = [k+1, matrix[k].index(" ")+1]
            count +=1
            break
        elif ((temp_matrix_1[k].count(" ") == 1) & ((temp_matrix_1[k].count("X") == 2) | (temp_matrix_1[k].count("O") == 2))):
            temp_matrix_1[k][temp_matrix_1[k].index(" ")] = "."
            for i in range(3):
                for j in reversed(range(3)):
                    temp_matrix_2[j].append(temp_matrix_1[i][j])
            matrix = temp_matrix_2
            on += 1
            count += 1
            break
        elif k < 2:
            if ((diagonals[k].count(" ") == 1) & ((diagonals[k].count("X") == 2) | (diagonals[k].count("O") == 2))):
                diagonals[k][diagonals[k].index(" ")] = "."
                if k == 0:
                    for i in range(3):
                        matrix[i][i] = diagonals[0][i]
                elif k == 1:
                    matrix[0][2] = diagonals[1][0]
                    matrix[1][1] = diagonals[1][1]
                    matrix[2][0] = diagonals[1][2]
                on +=1
                count += 1
                break
    if on == 1:
        on -= 1
        for k in range(3):
            if "." in matrix[k]:
                coords = [k+1, matrix[k].index(".")+1]
    if count == 0:
        coords = easy()
    for k in range(len(coords)):
        coords[k] = int(coords[k])
    return coords


def max():
    maxv = -2

    px = None
    py = None

    X_win, O_win, spaces = outcome_check(matrix)

    if X_win == 1:
        return (-1, 0, 0)
    elif O_win == 1:
        return (1, 0, 0)
    elif spaces == 0:
        return (0, 0, 0)

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == ' ':
                matrix[i][j] = 'O'
                (m, min_i, min_j) = min()
                if m > maxv:
                    maxv = m
                    px = i
                    py = j
                matrix[i][j] = ' '
    return (maxv, px, py)


def min():
    minv = 2

    qx = None
    qy = None

    result = outcome_check(matrix)

    if X_win == 1:
        return (-1, 0, 0)
    elif O_win == 1:
        return (1, 0, 0)
    elif spaces == 0:
        return (0, 0, 0)

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == ' ':
                matrix[i][j] = 'X'
                (m, max_i, max_j) = max()
                if m < minv:
                    minv = m
                    qx = i
                    qy = j
                matrix[i][j] = ' '

    return (minv, qx, qy)



print("""Welcome to AI Tic-Tac-Toe
You can either play against another user, against the computer or let the computer battle it out and see the result.
There are three computer difficulties to choose from: Easy, Medium and Hard.
 """)
game_play = "Start"
while game_play != "exit":
    player_1 = input("Player 1:").lower()
    player_2 = input("Player 2:").lower()
    if ((player_1 != "easy") & (player_1 != "medium") & (player_1 != "hard") & (player_1 != "user")) | \
            ((player_2 != "easy") & (player_2 != "medium") & (player_2 != "hard") & (player_2 != "user")):
        print("You did not enter a correct option for one of the players, please enter Easy, Medium, Hard or User")
    else:
        matrix = [[], [], []]
        X_win = 0
        O_win = 0
        turn = 0
        for i in range(3):
            for j in reversed(range(3)):
                matrix[j].append(" ")
        board(matrix)
        spaces = 0
        while spaces < 9:
            if turn % 2 == 0:
                if player_1 == "user":
                    coord = user()
                elif player_1 == "hard":
                    (m, qx, qy) = min()
                    coord = [qx+1, qy+1]
                elif player_1 == "medium":
                    coord = medium(matrix)
                else:
                    coord = easy()
            else:
                if player_2 == "user":
                    coord = user()
                elif player_2 == "hard":
                    (m, px, py) = max()
                    coord = [px+1, py+1]
                elif player_2 == "medium":
                    coord = medium(matrix)
                else:
                    coord = easy()
            if len(coord) != 2:
                print("Please enter two coordinates!")
            elif (coord[0] < 4) & (coord[1] < 4):
                if (matrix[coord[0] - 1][coord[1] - 1] == " ")|(matrix[coord[0] - 1][coord[1] - 1] == "."):
                    matrix = board_change(matrix, coord)
                    board(matrix)
                    X_win, O_win, spaces = outcome_check(matrix)
                    turn += 1
                else:
                    if ((player_1 == "user") & (turn % 2 == 0)) | ((player_2 == "user") & (turn % 2 != 0)):
                        print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
            if (X_win >= 1):
                print("X Wins")
                break
            elif (O_win >= 1):
                print("O Wins")
                break
            elif spaces == 0:
                print("Draw")
                break

        game_play = input("Input 'exit' to quit, to play another game press enter: ")
