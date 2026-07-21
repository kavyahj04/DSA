def minimizeMaxDist(arr, k):
    n = len(arr)
    howmanyPlaced = [0] * n
    for i in range(k):
        maxV, maxI = -1,-1
        for j in range(len(arr)-1):
            diff = arr[j+1] - arr[j]
            secL = diff / (howmanyPlaced[i] + 1)
            if maxV < secL:
                maxV = secL
                maxI = i
        howmanyPlaced[maxI] += 1
    maxAns = -1
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        secL = diff / (howmanyPlaced[i] + 1)
        maxAns = max(maxAns, secL)
    print(maxAns)
    return maxAns

arr = [1,2,3,4,5]
k = 4
minimizeMaxDist(arr, k)