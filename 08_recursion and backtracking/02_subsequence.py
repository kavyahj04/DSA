def subs(ind, arr, n, temp):
    if ind >= n:
        print(temp)
        return
    temp.append(arr[ind])
    subs(ind+1, arr, n, temp)
    temp.remove(arr[ind])
    subs(ind+1, arr, n, temp)

arr = [3,1,2]
temp = []
n = 3
subs(0, arr,n, temp)


# Time complexity: O(2ⁿ · n)

# Each call to subs branches into two recursive calls (include arr[ind], exclude it), and this happens n times before hitting the base case. That gives a recursion tree with roughly 2ⁿ leaf nodes (one per subsequence) — actually about 2ⁿ⁺¹ - 1 total calls, which is O(2ⁿ).

# At each of those 2ⁿ leaves, you do print(temp), and temp can hold up to n elements — printing/copying a list of length n costs O(n). So total time = O(2ⁿ) × O(n) = O(2ⁿ · n).

# Space complexity: O(n) (auxiliary, excluding the printed output)

# Recursion call stack depth = n (one frame per level of ind), so O(n).
# temp itself holds at most n elements at any point (since you always remove before backtracking), so O(n).
# These aren't nested/multiplied — they coexist — so it stays O(n), not O(n²).
# If you count the output itself (all 2ⁿ printed subsequences, each up to length n), that's O(2ⁿ · n) — but that's output space, not auxiliary space, and interviewers usually want the two separated.

# Stack space is O(n)
