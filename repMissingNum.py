# BFA

def findRepMissing(nums):
    rep, miss = 0, 0
    for i in range(1, len(nums)+1):
        count = 0
        for j in range(len(nums)):
            if nums[j] == i:
                count += 1
        if count == 2:
            rep = i
        if count == 0:
            miss = i
        if rep and miss:
            break
    print([miss, rep])
    return [miss, rep]

nums = [1,2,2,4]
findRepMissing(nums)

# Better 

def findRepMissing2(nums):
    miss, rep = float('-inf'),float('-inf')
    hshArr = {i:0 for i in range(len(nums)+ 1)}
    for i in range(len(nums)):
        hshArr[nums[i]] = 1 + hshArr[nums[i]]
    for k, v in hshArr.items():
        if k != 0 and v == 0:
            miss = k
        elif v == 2:
            rep = k
    print([miss, rep])
    return [miss, rep]

findRepMissing2(nums)


# Optimal 

def findRepMissing3(nums):
    s1, s2 = 0, 0
    n = len(nums)
    sn = (n * (n + 1)) / 2
    s2n = (n * (n + 1) * (2*n + 1)) / 6
    val1, val2, x, y = 0,0,0,0

    for i in range(len(nums)):
        s1 += nums[i]
        s2 += nums[i] * nums[i]
    
    val1 = s1 - sn
    val2 = s2 - s2n
    val2 = val2 / val1
    x = (val1 + val2) / 2
    y = val2 - x
    print([int(x), int(y)])
    return(x, y)
findRepMissing3(nums)