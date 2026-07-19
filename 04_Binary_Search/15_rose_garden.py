# BFA - For the brute force solution traverse through entire possible days from min to max AND CHECK FOR POSSIBLE FUNCTION FOR EACH 

# Optimal 

def findMinBloom(bloomDay, m, k):
    low, high = min(bloomDay), max(bloomDay)
    print(low, high)
    while low <= high:
        mid = (low + high) // 2
        if possible(bloomDay, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    print(low)
    return low

def possible(bloomDay, d, m, k):
    c, bd = 0, 0
    for i in range(len(bloomDay)):
        if bloomDay[i] <= d:
            c += 1
        else:
            print(bd)
            print(c//k)
            bd += c // k
            print(f"bd - {bd}")
            c = 0
    bd += c // k
    if bd >= m:
        print(d)
        print(bd)
        return True

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
findMinBloom(bloomDay, m, k)