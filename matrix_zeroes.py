# BFA 

def makeZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                markRow(i, cols)
                markCol(j, rows)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    print(matrix)
    return matrix

def markRow(i, cols):
    for j in range(cols):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(j, rows):
    for i in range(rows):
        if matrix[i][j] != 0:
            matrix[i][j] = -1



matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
makeZeroes(matrix)

# Time Complexity - O(n * m ) * O(n) * O(m)


# Better 

def makeZeroes2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    rowArr = [0] * rows
    colArr = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rowArr[i] = 1
                colArr[j] = 1
    
    for i in range(rows):
        for j in range(cols):
            if rowArr[i] == 1 or colArr[j] == 1:
                matrix[i][j] == 0
    print(matrix)
    return matrix

makeZeroes2(matrix)


# Time - O(2 * n * m)

# Space - O(n) + O(m)