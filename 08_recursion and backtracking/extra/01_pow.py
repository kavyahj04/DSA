def mypow(x, n):
    if n > 0:
        ans =  mypowfind(x, n)
    else:
        ans = 1 // mypowfind(x, n)
    print(ans)

def mypowfind(x, n):
    if n == 1:
        return x
    ans = mypowfind(x, n // 2)
    if (n % 2) == 0:
        return ans * ans
    else:
        return ans * ans * x

mypow(2, 10)