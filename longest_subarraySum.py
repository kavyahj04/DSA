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

# Complexity

# O(n) time
# O(n) space.


def longestSubarrayOptimal(arr, k):
    l, r, sum_ = 0, 0, 0
    n = len(arr)
    maxLen = 0
    while l < n and r < n:
        
        if r < n:
            sum_ += arr[r]
        if sum_ == k:
            maxLen = max(maxLen, r - l + 1)
            
        while l <= r and sum_ > k:
            sum_ -= arr[l]
            l += 1
        
        
        r += 1
        
        
    print(maxLen)
    return maxLen

longestSubarrayOptimal(arr, k)

# T(n) -> O(2n)
# S -> O(1)
