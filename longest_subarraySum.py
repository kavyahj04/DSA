def longestSubarray(arr, k):
    maxLen = 0
    prefixSum = {0 : -1}
    sum_ = 0
    for i in range(len(arr)):
        sum_ += arr[i]
        diff = sum_ - k
        if diff in prefixSum:
            l = i - prefixSum[diff]
            maxLen = max(maxLen, l)
        if sum_ not in prefixSum:
            prefixSum[sum_] = i
    print(maxLen)
    return maxLen

arr = [2, 1, 3, 1, 2, 4, 1]
k = 6

longestSubarray(arr, k)