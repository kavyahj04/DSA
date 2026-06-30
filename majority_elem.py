# Find the majority element that appears more that N/2 

# Brute Force approach 

def majorityElem1(arr):
    n = len(arr) // 2
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[j] == arr[i]:
                count += 1
        if count >= n:
            print(arr[i])
            return arr[i]
    print(-1)
    return -1 

arr = [5,5,7,7,5,5,7,7,5,5,5,5,7,7,7,7,5,7,5]
majorityElem1(arr)


# Complexity 

# T(n) - O(n ** 2)


# Better Approach

def majorityElem2(arr):
    n = len(arr) // 2
    nums = {}
    for i in range(len(arr)):
        nums[arr[i]] = nums.get(arr[i], 0) + 1
    
    for key, val in nums.items():
        if val >= n :
            print(key)
            return key
    print(-1)

majorityElem2(arr)

# Complexity 

# Time - O(n) + O(n)(if all numbers are unique)

# Space - O(n)

# Optimal approach 

# Moore's voting algorithm


def majority3(arr):
    n = len(arr) // 2
    el = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if count == 0:
            el = arr[i]
            count += 1

        elif arr[i] == el:
            count += 1

        else:
            count -= 1
    #if there must exist one element then return el, if not mentioned this loop is required
    count = 0
    for i in range(len(arr)):
        if arr[i] == el:
            count += 1
    if count >= n:
        print(el)
        return el
    print(-1)
    return -1

majority3(arr)
        
# Complexity

# Time - O(n) + O(n) if not specified

# Space - O(1)