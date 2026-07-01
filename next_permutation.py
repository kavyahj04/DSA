def nextPermutation(arr):
    idx = -1
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            idx = i
            break
    
    if idx == -1:
        reversed(arr)
    
    for i in range(len(arr) -1, idx+1, -1):
        if arr[i] > arr[idx]:
            arr[i], arr[idx] = arr[idx], arr[i]
            break
    
    arr[idx + 1:] = arr[idx + 1:][:: -1]
    print(arr)
    return arr
arr = [1, 5, 4, 3, 2]
nextPermutation(arr)
    
    
