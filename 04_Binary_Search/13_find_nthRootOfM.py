
def findElement(n, m):
    l,r = 1, m
    val = -1
    while l <= r:
        mid = (l + r) // 2
        ans = checkroot(mid,n)
        if ans == m:
            val = mid
            print(val)
            return val
        elif ans < m:
            l = mid + 1
        else:
            r = mid - 1
    print(val)
    return val

def checkroot(mid,n):
    ans = 1
    for i in range(1,n+1):
        ans *= mid
    return ans

findElement(3, 64)