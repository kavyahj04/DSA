# BFA 

def move_all_zeroes_BFA(arr):
    cnt = 0
    temp = []
    for i in range(len(arr)):
        if arr[i] == 0:
            cnt += 1
        else:
            temp.append(arr[i])
    for i in range(len(arr)):
        if i < (len(arr) - cnt):
            arr[i] = temp[i]
        else:
            arr[i] = 0
    print(arr)


# T - o(N) + O(N)

# S - O(N)
move_all_zeroes_BFA([1,2,3,0,4,0,0,5])        


def move_all_zeroes(arr):
    l = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            if i != l:
                arr[i], arr[l] = arr[l], arr[i]
            l+=1
    print(arr)
    return arr
    
move_all_zeroes([1,2,3,0,4,0,0,5])

# Complexity:

# Time	O(n) — single pass
# Space	O(1) — in-place swaps
