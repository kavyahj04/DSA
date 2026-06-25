def removeDupFromSorted(arr):
    sorted_arr = set(arr)
    len_arr = len(sorted_arr)
    arr[:len_arr] = sorted_arr
    print(arr)
    return arr

removeDupFromSorted([1,1,2,2,3,3,4,4])
        
