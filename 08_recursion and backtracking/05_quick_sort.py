def quickSort(arr, low, high):
    if low < high:
        pidx = getPartitionIndex(arr, low, high)
        quickSort(arr, low, pidx-1)
        quickSort(arr, pidx+1, high)
    return arr

def getPartitionIndex(arr, low, high):
    pivot = arr[low]
    i, j = low, high
    while i < j:
        while arr[i] <= pivot and i <= high:
            i += 1
        while arr[j] >= pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], pivot
    return j