# BFA 

def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    matrix2 = [[0] * rows for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            matrix2[j][rows - 1 - i] = matrix[i][j]
    print(matrix2)
    return matrix2

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)

# Time Complexity - O(n ** 2)

# Space Complexity - O(n ** 2)

