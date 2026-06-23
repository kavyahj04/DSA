
# selection sort

def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        minN = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minN]:
                minN = j
        temp = arr[i]
        arr[i] = arr[minN]
        arr[minN] = temp
    print(arr)
    return arr

# arr = [12, 3, 145, 23, 0, 56, 7]
# selectionSort(arr)


# bubble sort

def bubbleSort(arr):
    for i in range(len(arr) - 1, -1, -1):
        didSwap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                didSwap = True
        if not didSwap:
            break

    print(f"bubble sort - {arr}")
    return arr


# arr = [12, 3, 145, 23, 0, 56, 7]
# bubbleSort(arr)


def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
    print(f"Insertion sort - {arr}")
    return arr

arr = [12, 3, 145, 23, 0, 56, 7]
insertionSort(arr)