# Rotate array by 1 element 

# [1, 2, 3, 4, 5]
# [2, 3, 4, 5, 1]

def rotateBy1(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr) - 1] = temp
    print(arr)
    return arr 

# rotateBy1([1,2,3,4,5,6])

# Time Complexity 
# O(n)

# Space Complexity 
# O(1)



# left rotate by d places 

# [1, 2, 3, 4, 5] d = 3
 
# [4, 5, 1, 2, 3]

# Brute force solution 

def rotateArrayByD(arr, d):
    temp = []
    n = len(arr)
    d = d % n # O(1)
    temp = arr[:d] # O(d) — copies d elements
    
    for i in range(d, n):  # O(n - d) — shifts n-d elements
        arr[i - d] = arr[i]
    
    for i in range(n-d, n): # O(d) — places d elements
        arr[i] = temp[i -(n-d)]
    print(arr)
    return arr

# rotateArrayByD([1,2,3,4,5,6], 7)


# T(n)
# Total = O(1) + O(d) + O(n-d) + O(d)

# = O(d + n - d + d)

# = O(n + d)

# Since d < n always (after d % n), d is dominated by n:

# = O(n)

# Space complexity:

# temp = arr[:d] → O(d) extra space

# In the worst case d ≈ n, so space is O(n).



# Optimal Solution 

def rotateKarrayOptimal(arr, d):
    n = len(arr)
    d = d % n # O(1)
    arr = reverseArray(arr, 0, d-1) # O(d/2) → O(d)
    arr = reverseArray(arr, d, n-1) # O((n-d)/2) → O(n-d)
    arr = reverseArray(arr, 0, n-1) # O(n/2) → O(n)
    print(arr)
    return arr


def reverseArray(arr, left, right):
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -=1 
    print(arr)
    return arr


rotateKarrayOptimal([1,2,3,4,5,6,7], 15)

# Time Complexity 
# Total = O(d) + O(n-d) + O(n)

# = O(d + n - d + n)

# = O(2n)

# = O(n)

# Space: O(1) — no extra memory, all swaps done in-place (unlike the brute force which used a temp array of size d).

