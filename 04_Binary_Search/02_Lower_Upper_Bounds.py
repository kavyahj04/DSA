# Lower Bound - arr[i] >= x

def lowerBound(nums, x):
    l, h = 0, len(nums)-1
    ans = nums[-1] + 1
    while l <= h:
        m = (l + h) // 2
        if nums[m] >= x:
            ans = nums[m]
            h = m - 1
        else:
            l = m + 1
    print(ans)
    return ans
nums = [-1,0,3,5,9,12]
x = 9
lowerBound(nums, x)

def upperBound(nums, x):
    l, h = 0, len(nums) - 1
    ans = nums[-1] + 1
    while l <= h:
        m = (l + h) // 2
        if nums[m] > x:
            ans = nums[m]
            h = m - 1
        else:
            l = m + 1
    print(ans)
    return ans

nums = [-1,0,3,5,9,12]
x = 9
upperBound(nums, x)
