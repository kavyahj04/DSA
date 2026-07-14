# BFA 

def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # rows × cols becomes cols × rows
    matrix2 = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            matrix2[j][rows - 1 - i] = matrix[i][j]
    print(matrix2)
    return matrix2

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)

# Time Complexity - O(n ** 2)

# Space Complexity - O(n ** 2)

def rotate2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(0, rows-1):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(rows):
        reverse(matrix[i])
    print(matrix)

def reverse(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

rotate2(matrix)