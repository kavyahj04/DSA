class Solution:
    def floorSqrt(self, n): 
        # code here
        l, h = 1, n
        ans = float("-inf")
        while l <= h:
            m = (l + h) // 2
            sq = m * m
            if sq  <= n:
                ans = m
                l = m + 1
            else:
                h = m - 1
        return ans