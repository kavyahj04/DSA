def subsequenceSum(nums,k):
    def backtrack(idx,temp, sum, ans):
        if idx >= len(nums):
            if sum == k:
                ans.append(temp.copy())
            return
        temp.append(nums[idx])
        backtrack(idx+1, temp, sum+nums[idx], ans)
        temp.remove(nums[idx])
        backtrack(idx+1, temp, sum, ans)
    temp,ans, sum = [],[], 0
    backtrack(0,temp,sum, ans)
    print(ans)
nums = [1,2,1]
k = 2
subsequenceSum(nums,k)