# BFA
def maxSum(arr):
    maxS = float('-inf')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum_ = 0
            for k in range(i, j+1):
                sum_ += arr[k]
            if sum_ > maxS:
                maxS = sum_
    print(maxS)
    return maxS
            
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSum(arr)

# Time - O(n ** 3)


# Better

def maxSum2(arr):
    maxS = float('-inf')
    for i in range(len(arr)):
        sum_ = 0
        for j in range(i, len(arr)):
            sum_ += arr[j]
            if sum_ > maxS:
                maxS = sum_
    print(maxS)
    return maxS
            
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSum2(arr)

# Time - O(n ** 2)

# Optimal - Kadanes algorithm
def maxSum3(arr):
    maxS = float('-inf')
    sum_ = 0
    for i in range(len(arr)):
        sum_ += arr[i]

        if sum_ > maxS:
            maxS = sum_
        if sum_ < 0:
            sum_ = 0
    print(maxS)
    return maxS

maxSum3(arr)

# Time - O(n)

# if asked to print elements 

def maxSum4(arr):
    maxS = float('-inf')
    sum_ = 0
    start, end = 0, 0
    for i in range(len(arr)):
        if sum_ == 0:
            start = i

        sum_ += arr[i]

        if sum_ > maxS:
            maxS = sum_
            end = i
            
        elif sum_ < 0:
            sum_ = 0
    temp = []
    for i in range(start, end+1):
        temp.append(arr[i])
    print(temp)

maxSum4(arr)

