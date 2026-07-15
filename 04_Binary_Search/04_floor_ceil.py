# floor - largest num in arr <= x
def floorNum(nums, x):
    ans = -1
    l, h = 0, len(nums) - 1
    while l <= h:
        m = (l + h) // 2
        if nums[m] <= x:
            ans = nums[m]
            l = m + 1
        else:
            h = m - 1
    print(ans)
    return ans
nums = [10,20,30,40,50]
floorNum(nums, 20)


# ceil - smallest num in arr >= x - Lower bound
def ceilNum(nums, x):
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
nums = [10,20,30,40,50]
ceilNum(nums, 25)