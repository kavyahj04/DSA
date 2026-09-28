def permutations(nums):
    def backtrack(nums,ds, ans,freq):
        if len(ds) == len(nums):
            ans.append(ds.copy())
        for i in range(len(nums)):
            if not freq[i]:
                freq[i] = True
                ds.append(nums[i])
                backtrack(nums,ds, ans,freq)
                ds.pop()
                freq[i] = False
    ans, ds = [], []
    freq = [False] * len(nums)
    backtrack(nums,ds, ans,freq)
    print(ans)
    return ans
nums = [1, 2, 3]
permutations(nums)