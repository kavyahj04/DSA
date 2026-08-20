def divideArr(arr, k):
    l, r = float("-inf"), float("-inf")
    output = []
    arr.sort()
    for i in range(len(arr)):
        if i % 3 == 0:
            l = arr[i]
        elif i % 3 == 2:
            r = arr[i]
            diff = r - l
            if diff > k:
                return []
            else:
                output.extend([arr[i-2:i+1]])
    print(output)
arr = [1,3,4,8,7,9,3,5,1]
k = 2
divideArr(arr, k)