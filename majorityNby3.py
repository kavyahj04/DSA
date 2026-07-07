# we know for sure that for every array we will have 2 majority elements 

# n / 3 

# 8 / 3 == 2 we need >2 = 3 occurences 3 + 3 + 2, so 2 elements 

# BFA

def majority1(arr):
    ls = []
    mn = len(arr) // 3
    for i in range(len(arr)):
        if not ls or ls[0] != arr[i]:
            count = 0
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    count += 1
            if count > mn:
                ls.append(arr[i])
            if len(ls) == 2:
                print(ls)
                return ls
arr = [1,1,1,3,3,2,2,2]
# majority1(arr)


# Better - Hashing 

def majority2(arr):
    nums = {}
    mn = len(arr) // 3
    ls = []
    for i in range(len(arr)):
        nums[arr[i]] = 1 + nums.get(arr[i], 0)
        if nums[arr[i]] > mn:
            ls.append(arr[i])
    print(ls)
    return ls

# majority2(arr)

# Optimal - Moore's algo

def majority3(arr):
    cnt1, cnt2 = 0, 0
    el1, el2 = float('-inf'), float('-inf')
    ls = []
    mn = len(arr) // 3
    for i in range(len(arr)):
        if cnt1 == 0 and arr[i] != el2:
            cnt1 += 1
            el1 = arr[i]
        elif cnt2 == 0 and arr[i] != el1:
            cnt2 += 1
            el2 = arr[i]
        elif el1 == arr[i]:
            cnt1 += 1
        elif el2 == arr[i]:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    print(el1, el2)

    # Manual Check 
    cnt1, cnt2 = 0, 0
    for i in range(len(arr)):
        if arr[i] == el1:
            cnt1 += 1
        elif arr[i] == el2:
            cnt2 += 1
    if cnt1 > mn:
        ls.append(el1)
    if cnt2 > mn:
        ls.append(el2)
    print(ls)
    return ls

majority3(arr)