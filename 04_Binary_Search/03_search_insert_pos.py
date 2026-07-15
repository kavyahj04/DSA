def searchInsert(nums, x):
    l, h = 0, len(nums)-1
    ans = nums[-1] + 1
    while l <= h:
        m = (l + h) // 2
        if nums[m] >= x:
            ans = m
            h = m - 1
        else:
            l = m + 1
    print(ans)
    return ans
nums = [-1,0,3,5,9,12]
x = 9
searchInsert(nums, x)