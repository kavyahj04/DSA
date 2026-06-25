def largestElement(arr):
    largest = arr[0]

    for i in range(2, len(arr)):
        if arr[i] >  largest:
            largest = arr[i]
        print(largest)
    return largest

largestElement([9,456,7,3,5,11,2,56])