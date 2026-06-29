#Brute Force 

def twoSum1(arr, target):
    for i in range(len(arr)):
        for j in range(i +1, len(arr)):
            sum_ = arr[i] +  arr[j]
            if sum_ == target:
                print(i, j)
                return i, j

nums = [2,7,11,15]
target = 9
# twoSum1(nums, target)

# Complexity 

# Time - O(n ** 2)

# Space - O(1)

# Better - Hashing

def twoSum2(arr, target):
    nums = {}
    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in nums:
            print(nums[diff],i )
            return nums[diff], i
        nums[arr[i]] = i

twoSum2(nums, target)

# two pointer approach

def twoSum3(arr, target):
    left = 0
    right = len(arr) - 1
    arr1 = sorted(arr)
    while left < right:
        sum_ = arr1[left] + arr1[right]
        if sum_ == target:
            print("yes")
            return left, right
        elif sum_ > target:
            right -= 1
        else:
            left += 1
    print("no")

twoSum3(nums, target)

# Complexity

# 	        Best	Average	Worst	Space
# twoSum1	O(1)	O(n²)	O(n²)	O(1)
# twoSum2	O(1)	O(n)	O(n²)	O(n)
# twoSum3	O(n log n)	O(n log n)	O(n log n)	O(1) 

# *sorted() creates a new list → O(n) space. If you sorted in-place it'd be O(1) (or O(log n) for sort's call stack).

# Best case for 1 and 2 is O(1) — answer is in first two elements.




