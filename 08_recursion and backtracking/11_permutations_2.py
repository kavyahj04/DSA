class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def backtrack(nums,ds, ans,freq):
            if len(ds) == len(nums):
                ans.append(ds.copy())
                return
            for i in range(len(nums)):
                if freq[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not freq[i-1]:
                    continue
                freq[i] = True
                ds.append(nums[i])
                backtrack(nums,ds, ans,freq)
                ds.pop()
                freq[i] = False
        ans, ds = [], []
        freq = [False] * len(nums)
        backtrack(nums,ds, ans,freq)
        print(ans)
        return list(ans)