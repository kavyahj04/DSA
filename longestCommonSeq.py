#BFA

def longestSeq(arr):
    longest = float('-inf')
    for i in range(len(arr)):
        x = arr[i]
        count = 1
        while(linearSearch(arr, x+1)):
            count += 1
            x = x + 1
        longest = max(longest, count)
    print(longest)
    return longest

            

def linearSearch(arr, n):
    for i in range(len(arr)):
        if n == arr[i]:
            return True

arr = [102, 104, 101, 102, 3, 1, 100, 6,3, 3,3,98, 103,4,4, 2, 5, 99, 104, 102, 101, 98, 100]
longestSeq(arr)


# Time - O(n ** 2)
# Space - o(1)


# Better

def longestSeq2(arr):
    arr.sort()
    last_smaller = float('-inf')
    longest = float('-inf')
    for i in range(len(arr)):
        if i > 0 and arr[i] - 1 == last_smaller:
            count += 1
            last_smaller = arr[i]
        elif arr[i] != last_smaller:
            count = 1
            last_smaller = arr[i] 
        longest = max(longest, count)
    print(longest)
    return longest
longestSeq2(arr)


# TIME - O(n log n) + O(n)

# Space - O(1)


# optimal 

def longestSeq3(arr):
    
    nums = set(arr)
    longest = 0
    for n in nums:
        count = 1
        if n - 1 in nums:
            continue
        while n + 1 in nums:
            count += 1
            n = n + 1
           
        longest = max(longest, count)
    print(longest)
    return longest

longestSeq3(arr)

# Time - O(n)
# n-1 in nums: continue that check makes each number only ever get "walked" once across the whole run (each element visited by exactly one streak's while loop

# Space - O(n)