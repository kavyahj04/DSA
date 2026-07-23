def findPeak(matrix):
    r, c = len(matrix), len(matrix[0])
    l, h = 0, c - 1
    while l <= h:
        mid = (l + h) // 2
        maxRowIndx = findMaxIndex(matrix, r, c, mid)
        left = matrix[maxRowIndx][mid - 1] if (m - 1) >= 0 else -1
        right = matrix[maxRowIndx][mid + 1] if (m + 1) < c else -1
        if matrix[maxRowIndx][mid] > left and matrix[maxRowIndx][mid] > right:
            return {maxRowIndx, mid}
        elif matrix[maxRowIndx][mid] < left:
            h = mid - 1
        else:
            l = mid + 1
return [-1,-1]


def findMaxIndex(matrix, r, c, mid):
    maxV, indx = -1, -1
    for i in range(r):
        if matrix[i][mid] > maxV:
            maxV = matrix[i][mid]
            indx = i
    return i