def maxSum(arr):
    max_sum = 0
    for i in range(len(arr)-1):
        curr = arr[i] + arr[i+1]
        max_sum = max(max_sum, curr)
    return max_sum