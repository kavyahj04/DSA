
def search1(matrix, target):
    r, c = len(matrix), len(matrix[0])
    for i in range(r):
        l, h = 0, c-1
        while l <= h:
            m = (l + h) // 2
            if matrix[i][m] == target:
                print(f"Element Found at row - {i} and col - {m}")
                return [i,m]
            elif matrix[i][m] < target:
                l = m + 1
            else:
                h = m -1
    print("Element not found")
    return [-1, -1]


def search2(matrix, target):
    r, c = len(matrix)-1, len(matrix[0])-1
    l, h = 0, c
    while (l <= r and h <= c):
        if matrix[l][h] == target:
            print(f"Element Found at row - {l} and col - {h}")
            return[l,h]
        elif matrix[l][h] < target:
            l += 1
        else:
            h -= 1
    print("Element not Found")
    return [-1,-1]

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 6
search1(matrix, target)


