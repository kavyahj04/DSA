class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, h = max(nums), sum(nums)
        while l <= h:
            m = (l + h) // 2
            pntrs = self.getPainters(nums, k, m)
            if pntrs <= k:
                h = m - 1
            else:
                l = m + 1
        return l
            
    def getPainters(self, nums, k, mid):
        pntr = 1
        time = 0
        for i in range(len(nums)):
            if nums[i] + time <= mid:
                time += nums[i]
            else:
                pntr += 1
                time = nums[i]
        return pntr