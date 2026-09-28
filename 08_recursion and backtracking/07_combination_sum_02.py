def combinationSum(nums, target):
    nums.sort()
    ans, ds = [], []
    findCombinations(0, nums, target, ans, ds)
    print(ans)
    return ans 

def findCombinations(idx, nums, target, ans, ds):
    if target == 0:
        ans.append(ds.copy())
        return
    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i-1]:
            continue
        if nums[i] > target:
            break
        ds.append(nums[i])
        findCombinations(i+1, nums, target-nums[i], ans, ds)
        ds.remove(nums[i])

candidates = [10,1,2,7,6,1,5] 
target = 8
combinationSum(candidates, target)