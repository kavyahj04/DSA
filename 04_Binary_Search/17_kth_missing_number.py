def findKthPositive(nums, k):
    for i in range(len(nums)):
        if nums[i] <= k:
            k += 1
        else:
            break
    return k
    
def findKthPositiveBinarySearch(nums, k):
    l, h = 0, len(arr) - 1
    while l <= h :
        m = (l + h) // 2
        missing = arr[m] - (m + 1)
        if missing < k :
            l = m + 1
        else:
            h = m - 1
    return k + h + 1