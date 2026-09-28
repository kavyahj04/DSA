def subsets(self, nums: list[int]) -> list[list[int]]:
    def backtrack(idx,nums,temp, ans,n):
        if idx >= n:
            ans.append(temp.copy())
            return
        temp.append(nums[idx])
        backtrack(idx+1,nums,temp,ans,n)
        temp.remove(nums[idx])
        backtrack(idx+1,nums,temp,ans,n)
    temp, ans, n = [], [], len(nums)
    backtrack(0,nums,temp, ans, n)
    return ans