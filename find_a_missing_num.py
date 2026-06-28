# [1, 2, 3,  5]

# Ans - 4


def findBF(arr):
    nums = set(arr)
    min_ = min(arr)
    max_ = max(arr)

    for i in range(min_, max_):
        if i not in nums:
            print(i)
            return i

findBF([7,5,8,6,3])

def findExor(arr):

    min_ = min(arr)
    max_ = max(arr)
    xor = 0
    for i in range(min_, max_ + 1):
        xor ^= i        # XOR all expected numbers
    for num in arr:
        xor ^= num      # XOR all actual numbers
    print(xor)
    return xor
    

findExor([3, 4, 5, 7, 8])