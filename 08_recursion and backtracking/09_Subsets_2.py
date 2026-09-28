def subset(nums):
    def backtrack(idx, nums,ds, ans):
        ans.append(ds.copy())
        for i in range(idx, len(nums)):
            if i != idx and nums[i] == nums[i-1]:
                continue
            ds.append(nums[i])
            backtrack(i + 1, nums,ds, ans)
            ds.remove(nums[i])
    nums.sort()
    ans, ds = [], []
    backtrack(0, nums,ds, ans)
    print(ans)
    return ans
nums = [2,3,2,1]
subset(nums)