def isArraySorted(arr):
    for i in range(len(arr)):
        if i > 0 and arr[i] < arr[i-1]:
            print(False)
            return False
    print(True)
    return True 

isArraySorted([11,2,3,4,5,6,7,8,9])