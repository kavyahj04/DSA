# BFA 

def rearrange(arr):
    pos, neg = [], []
    for i in range(len(arr)):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    n = len(arr) // 2
    for i in range(n):
        arr[2 * i] = pos[i]
        arr[2 * i + 1] = neg[i]
    print(arr)
    return arr

arr = [3,1,2,-1,-2,-8]
rearrange(arr)

# Time - O(n) + O(n) 

# Space - O(n)

# Optimal

def rearrange2(arr):
    pos, neg = 0, 1
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[pos] = arr[i]
            pos += 2
        else:
            arr[neg] = arr[i]
            neg += 2
    print(arr)
    return arr

rearrange2(arr)

# When elements are not equal

def rearrange3(arr):
    pos, neg = [], []
    for i in range(len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    if len(pos) >= len(neg):
        for i in range(len(neg)):
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]
        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            arr[index] = pos[i]
            index += 1
    else:
        for i in range(len(pos)):
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]
        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            arr[index] = neg[i]
            index += 1
    print(arr)
    return arr
arr = [-1, -2, -3, 3, 2]
rearrange3(arr)
        
            
        


    

