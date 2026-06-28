def findonce(arr):
    num = arr[0]
    for i in range(1,len(arr)):
        num ^= arr[i]
    print(num)
    return num

findonce([1,1,2,2,3,4,4,5,5])