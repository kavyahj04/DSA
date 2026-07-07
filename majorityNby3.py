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
majority1(arr)