def aggressiveCowsLinear(stalls, cows):
    stallMax = max(stalls)
    stalls = sorted(stalls)
    print(f"started-- stalls --{stalls}--stallmax -- {stallMax}")
    for i in range(1, stallMax+1):
        if canWePlaceCow(list(stalls), i, cows):
            continue
        else:
            print(f"ans -- {i - 1}")
            return i - 1

def canWePlaceCow(stalls, dist, cows):
    cnt = 1
    last = stalls[0]
    print("Placing cow")
    for i in range(1, len(stalls)):
        print(f"distance is {dist}")
        print(stalls[i] - last)
        if stalls[i] - last >= dist:
            cnt += 1
            last = stalls[i]
        print(f"count is {cnt}")
        if cnt == cows:
            return True
    return False

arr = [0,3,4,7,10,9]
k = 4

aggressiveCowsLinear(arr, k)

def aggressiveCows(stalls, cows):
    stallMax = max(stalls)
    stalls = sorted(stalls)
    low, high = 1, stallMax
    while low <= high:
        mid = (low + high) // 2
        if canWePlaceCow(stalls, dist, cows):
            low = mid + 1
        else:
            high = mid - 1
        return high