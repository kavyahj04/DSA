def search(matrix, target):
    r, c = len(matrix), len(matrix[0])
    l, h = 0, r * c - 1
    while l <= h:
        m = (l + h) // 2
        rw = m // c
        cl = m % c
        if matrix[rw][cl] == target:
            print(f"Element Found at row - {rw}, col - {cl}")
            return True
        elif matrix[rw][cl] < target:
            l = m + 1
        else:
            h = m - 1
    print("Element not found")
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 20
search(matrix, target)
