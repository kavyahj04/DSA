nums = [0,0,1,2,2,0,1,0,2,0,0]

def sort(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while m <= h:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    print(nums)
    return nums

sort(nums)