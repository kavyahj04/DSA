def combinationSum(nums, target):
    ans, ds = [], []
    findCombination(0,nums, target, ans, ds)
    print(ans)
    return ans

def findCombination(idx,nums, target, ans, ds):
    if idx == len(nums) or target < 0:
        if target == 0:
            ans.append(ds.copy())
        return
    ds.append(nums[idx])
    findCombination(idx, nums, target-nums[idx], ans, ds)
    ds.remove(nums[idx])
    findCombination(idx+1,nums, target, ans, ds)

candidates = [2,3,6,7]
target = 7
combinationSum(candidates, target)