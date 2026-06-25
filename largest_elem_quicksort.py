
# largest element in an array
def getPartitionIndex(arr, low, high):
    pivot = arr[low]
    i = low
    j = high 
    while i < j:
        while i < high and arr[i] <= pivot:
            i += 1
        while j > low and arr[j] > pivot:
            j -= 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
 
    temp = pivot
    arr[low] = arr[j]
    arr[j] = pivot

    return j




def quickSort(arr, low, high):
    if low < high:
        p_i = getPartitionIndex(arr, low, high)
        quickSort(arr, low, p_i - 1)
        quickSort(arr, p_i +1 , high)
    return arr

def largestElementInArray(arr):
    low = 0
    high = len(arr) - 1
    arr = quickSort(arr, low, high)
    print(arr[-1])
    return arr[-1]
    


largestElementInArray([7,9,4,6,2,5,1])

