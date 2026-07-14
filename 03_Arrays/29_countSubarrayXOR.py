# BFA 
def count(nums, t):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            xr = 0
            for k in range(i, j+1):
                xr = xr ^ nums[k]
            if xr == t:
                count += 1
    print(count)
    return count
nums = [4, 2, 2, 6, 4]
k = 6
# count(nums, k)

# Better 

def count2(nums, k):
    count = 0
    for i in range(len(nums)):
        xr = 0
        for j in range(i, len(nums)):
            xr = xr ^ nums[j]
            if xr == k:
                count += 1
    print(count)
    return count

# count2(nums,k)

# Optimal solution 

def count3(nums, k):
    count = 0
    hst = {0:1}
    xr = 0
    for i in range(len(nums)):
        xr = xr ^ nums[i]
        x = xr ^ k
        if x in hst:
            count += hst[x]
        hst[xr] = 1 + hst.get(xr, 0)
    print(count)

count3(nums, k)