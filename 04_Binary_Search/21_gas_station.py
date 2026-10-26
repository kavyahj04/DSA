def minimizeMaxDist(arr, k):
    n = len(arr)
    howmanyPlaced = [0] * n
    for i in range(k):
        maxV, maxI = -1,-1
        for j in range(len(arr)-1):
            diff = arr[j+1] - arr[j]
            secL = diff / (howmanyPlaced[j] + 1)
            if maxV < secL:
                maxV = secL
                maxI = j
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


## Binary Search Soultion

def minimizeDistBS(arr, k):
    def cntK(dist):
        val = 0
        for i in range(len(arr)-1):
            num_in_btwn = int((arr[i+1]-arr[i]) / dist)
            if (arr[i+1]-arr[i]) % dist == 0:
                val -= 1
            val += num_in_btwn
        return val
    l = 0
    h = -1
    for i in range(len(arr) - 1):
        h = max(h, (arr[i+1]-arr[i]))
    while h - l > 1e-6:
        m = (l + h) / 2
        ans = cntK(m)
        if ans > k:
            l = m
        else:
            h = m