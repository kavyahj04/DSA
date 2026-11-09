class Solution:
    def median(self, mat: list[list[int]]) -> int:
        def checkOccurences(m, r, c):
            cnt = 0
            for i in range(r):
                l, h = 0, c - 1
                while l <= h:
                    mid = (l + h) // 2
                    if mat[i][mid] <= m:
                        l = mid + 1
                    else:
                        h = mid - 1
                cnt += l
            return cnt

        rows, cols = len(mat), len(mat[0])
        mini, maxi = float("inf"), float("-inf")
        median = (rows * cols) // 2
        for i in range(rows):
            mini = min(mat[i][0], mini)
            maxi = max(mat[i][cols - 1], maxi)
        low, high = mini, maxi
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            n = checkOccurences(mid, rows, cols)
            if n <= median:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
