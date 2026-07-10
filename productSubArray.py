def maxProduct(self, nums: List[int]) -> int:
        pre, suff = 1, 1
        maxi = float('-inf')
        for i in range(len(nums)):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            
            pre = pre * nums[i]
            suff = suff * nums[len(nums) - i - 1]

            maxi = max(maxi, max(pre, suff))
        return maxi