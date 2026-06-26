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
