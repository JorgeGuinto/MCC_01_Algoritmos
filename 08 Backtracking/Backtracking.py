sudoku = [0]*9
# sudoku[0] = [5, 3, 0, 0, 7, 0, 0, 0, 0]
# sudoku[1] = [6, 0, 0, 1, 9, 5, 0, 0, 0]
# sudoku[2] = [0, 9, 8, 0, 0, 0, 0, 6, 0]
# sudoku[3] = [8, 0, 0, 0, 6, 0, 0, 0, 3]
# sudoku[4] = [4, 0, 0, 8, 0, 3, 0, 0, 1]
# sudoku[5] = [7, 0, 0, 0, 2, 0, 0, 0, 6]
# sudoku[6] = [0, 6, 0, 0, 0, 0, 2, 8, 0]
# sudoku[7] = [0, 0, 0, 4, 1, 9, 0, 0, 5]
# sudoku[8] = [0, 0, 0, 0, 8, 0, 0, 7, 9]

# sudoku[0] = [5, 0, 0, 9, 1, 3, 7, 2, 0]
# sudoku[1] = [3, 0, 0, 0, 8, 0, 5, 0, 9]
# sudoku[2] = [0, 9, 0, 2, 5, 0, 0, 8, 0]
# sudoku[3] = [6, 8, 0, 4, 7, 0, 2, 3, 0]
# sudoku[4] = [0, 0, 9, 5, 0, 0, 4, 6, 0]
# sudoku[5] = [7, 0, 4, 0, 0, 0, 0, 0, 5]
# sudoku[6] = [0, 2, 0, 0, 0, 0, 0, 0, 0]
# sudoku[7] = [4, 0, 0, 8, 9, 1, 6, 0, 0]
# sudoku[8] = [8, 5, 0, 7, 2, 0, 0, 0, 3]

sudoku[0] = [6, 9, 0, 0, 0, 0, 7, 0, 0]
sudoku[1] = [0, 0, 0, 0, 9, 6, 0, 0, 0]
sudoku[2] = [0, 8, 0, 7, 5, 3, 0, 9, 0]
sudoku[3] = [0, 2, 0, 3, 7, 4, 5, 6, 1]
sudoku[4] = [3, 6, 0, 0, 0, 5, 0, 2, 0]
sudoku[5] = [0, 0, 0, 9, 6, 0, 3, 7, 8]
sudoku[6] = [0, 0, 6, 0, 3, 1, 0, 8, 4]
sudoku[7] = [0, 4, 5, 8, 0, 7, 6, 0, 0]
sudoku[8] = [0, 0, 0, 0, 0, 0, 0, 5, 7]

def backtracking(sudoku):
    solutions = []
    start = 1
    i = j = 0
    while i < 9:
        j = 0
        while j < 9:
            if(sudoku[i][j] == 0):
                factible, k = legal(sudoku, i, j, start)
                if (factible):
                    solutions.append([k, i, j])
                    sudoku[i][j] = k
                    start = 1
                else:
                    x = solutions[len(solutions)-1]
                    sudoku[x[1]][x[2]] = 0
                    start = x[0] + 1
                    solutions.pop()
                    i = max(x[1] - 1, 0)
                    j = max(x[2] - 1, 0)
            j = j + 1
        i = i + 1
    printS(sudoku)


def legal (sudoku, i, j, start):
    factible = False
    for k in range(start,10,1):
        factible = horizontal(sudoku, i, j, k)
        if (factible):
            factible = vertical(sudoku, i, j, k)
            if(factible):
                factible = square(sudoku, i, j ,k)
                if(factible):
                    return factible, k
    return factible, 0
        


def horizontal (sudoku, i, j, k):
    for l in range(0, 9, 1):
        if (j != l):
            if (sudoku[i][l] == k):
                return False
    return True

def vertical (sudoku, i, j, k):
    for l in range(0, 9, 1):
        if (i != l):
            if (sudoku[l][j] == k):
                return False
    return True

def square (sudoku, i, j, k):
    if (i < 3):
        fila = 0
    elif (i < 6):
        fila = 1
    else:
        fila = 2
    if (j < 3):
        columna = 0
    elif (j < 6):
        columna = 1
    else:
        columna = 2    

    for x in range((3*fila), (3*fila + 3), 1):
        for y in range((3*columna), (3*columna + 3), 1):
            if (x != i or y != j):
                if (sudoku[x][y] == k):
                    return False
    return True

def printS (sudoku):
    for i in range(len(sudoku)):
        print(sudoku[i])


backtracking(sudoku)
