def checkroot(n):
    l, r, ans = 1, n, 1
    while l <= r:
        m = (l + r) // 2
        if m * m <= n:
            ans = m
            l = m + 1
        else:
            r = m - 1
    print(f"The ans is {ans}")
    return ans 
n = 36
checkroot(n)