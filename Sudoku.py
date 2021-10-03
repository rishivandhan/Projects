board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# backtracking functions to solve the board
def solve(sudokuBo):
    find = find_empty(sudokuBo)
    if not find:
        return True
    else:
        row, col = find
    # checking 1,10 to see if they are solution in board
    for x in range(1, 10):
        if valid(sudokuBo, x, (row, col)):
            sudokuBo[row][col] = x

            if solve(sudokuBo):
                return True

            sudokuBo[row][col] = 0

    return False


# function to see if the board is valid
def valid(sudokuBo, num, pos):
    # checking the row
    for x in range(len(sudokuBo[0])):
        if sudokuBo[pos[0]][x] == num and pos[1] != x:
            return False

    # check the coloumn
    for x in range(len(sudokuBo[0])):
        if sudokuBo[x][pos[1]] == num and pos[0] != x:
            return False

    # checking the box we are in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for x in range(box_y * 3, box_y * 3 + 3):
        for y in range(box_x * 3, box_x * 3 + 3):
            if sudokuBo[x][y] == num and (x, y) != pos:
                return False
    return True


# function to print the sudoku board
def draw_board(sudokuBo):
    for x in range(len(sudokuBo)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - ")
        for y in range(len(sudokuBo[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")

            if y == 8:
                print(sudokuBo[x][y])
            else:
                print(str(sudokuBo[x][y]) + " ", end="")


# finding the empty position in the board
def find_empty(sudokuBo):
    for x in range(len(sudokuBo)):
        for y in range(len(sudokuBo[0])):
            if sudokuBo[x][y] == 0:
                return x, y  # this returns the rows and columns of the algorithm
    return None


draw_board(board)
solve(board)
print("__________________________________")
draw_board(board)

