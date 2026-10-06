def maxSum(arr):
    max_sum = 0
    for i in range(len(arr)-1):
        curr = arr[i] + arr[i+1]
        max_sum = max(max_sum, curr)
    return max_sum


# Summary Checklist
# Every big subarray contains adjacent pairs inside it.

# The sum of the 2 smallest numbers in a big subarray can never be larger than the sum of any adjacent pair inside it.

# Therefore, the overall maximum score across ALL subarrays will always be found by looking at one of those length-2 adjacent pairs.

# You don't need to check length 3, length 4, or length 100