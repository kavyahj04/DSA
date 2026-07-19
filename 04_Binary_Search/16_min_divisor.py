import math
def smallestDivisor(nums: List[int], threshold: int) -> int:
        l, h = 1, max(nums)
        while l <= h :
            m = (l + h) // 2
            if isDivisor(nums, threshold, m):
                h = m - 1
            else:
                l = m + 1
        print(l)
        return l
    
def isDivisor(nums, t, m):
    v = 0
    for i in range(len(nums)):
        print(m)
        print(f"v - {math.ceil(nums[i] / m)}")
        v += math.ceil(nums[i] / m)
        print(f"total = {v}")
    # print(v)
    if v <= t:
        return True
    return False

nums = [1,2,5,9]
threshold = 6
smallestDivisor(nums, threshold)

# T(n) = > O(n) * O(log(m)) when m is max of n