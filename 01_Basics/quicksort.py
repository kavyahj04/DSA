def quicksort(arr, low, high):
    if low < high:
        p_i = getPartitionIndex(arr, low, high)
        quicksort(arr, low, p_i - 1)
        quicksort(arr, p_i + 1, high)

def getPartitionIndex(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot:
            i += 1
        while arr[j] >= pivot:
            j -= 1
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

        i+=1
        j-=1
    temp = arr[j]
    arr[j] = pivot
    pivot = temp

    return j 