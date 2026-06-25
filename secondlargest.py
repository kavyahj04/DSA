# bruteforce 

def secondLargestBruteForce(arr):
    low = 0
    high = len(arr) - 1
    arr = quickSort(arr, low, high)
    largest = arr[-1]
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != largest:
            print(arr[i])
            return arr[i]


def quickSort(arr, low, high):
    if low < high:
        p_i = getPartitionIndex(arr, low, high)
        quickSort(arr, low, p_i - 1)
        quickSort(arr, p_i + 1, high)
    return arr

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
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    arr[low], arr[j] = arr[j], arr[low]

    return j

# secondLargest([12,2,56,3,88,88,9])

# optimal 

def secondLargest(arr):
    largest = arr[0]
    secondLargest = -1

    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]
    print(largest)
    print(secondLargest)
    return largest, secondLargest


secondLargest([1,3,44,55,666,2,3,99,55,66,22,33,33,123,752])

