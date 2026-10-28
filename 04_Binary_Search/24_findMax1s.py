def searchInSorted(matrix):
    r, c = len(matrix), len(matrix[0])
    max_cnt = -1
    index = -1
    for i in range(r):
        cnt = 0
        for j in range(c):
            cnt += matrix[i][j]
        if cnt > max_cnt:
            max_cnt = cnt
            index = i
    print(max_cnt, index)
    return max_cnt
mat = [[1,1,1],[0,1,1],[0, 0, 1],[1,1,1],[1,1,1]]
# searchInSorted(mat)


def searchInSortedOptimal(matrix):
    r, c = len(matrix), len(matrix[0])
    max_cnt = -1
    index = -1
    for i in range(r):
        cnt = 0
        print(f"row - {c}")
        indx = getCount(matrix[i])
        print(f"BS - {indx}")
        cnt = c - (indx)
        print(f"count - {cnt}")
        if cnt > max_cnt:
            max_cnt = cnt
            index = i
    print(max_cnt,index)
    return max_cnt

def getCount(arr):
    l,h = 0, len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == 1:
            h = m - 1
        else:
            l = m + 1
    return l

searchInSortedOptimal(mat)

def rowWithMax1s(self, arr: list[list[int]]) -> int:
        # code here
        maxi = 0
        maxi_index = -1
        for i in range(len(arr)):
            cnt = 0
            l, h = 0, len(arr[i])-1
            while l <= h:
                m = (l + h) // 2
                if arr[i][m] == 0:
                    l = m + 1
                else:
                    h = m - 1

            cnt = len(arr[i]) - l
            if cnt > maxi:
                maxi = cnt
                maxi_index = i
        return maxi_index