def printName(cnt):
    if cnt == 5:
        return
    print("Kavya")
    cnt += 1
    printName(cnt)
# printName(0)

def linear(n, cnt2):
    if cnt2 > n:
        return
    print(cnt2)
    cnt2 += 1
    linear(n, cnt2)

# linear(5,1)

def linear2(n, cnt2):
    if cnt2 <= 0:
        return
    print(cnt2)
    cnt2 -= 1
    linear2(n, cnt2)

# linear2(5,5)

# backtracking 1 --> print 1 to n

def backtrack1(n, cnt):
    if cnt < 1:
        return
    backtrack1(n, cnt-1)
    print(cnt)

backtrack1(5,5)

# backtracking 2 --> print n to 1

def backtrack2(n, cnt):
    if cnt > n:
        return
    backtrack2(n, cnt+1)
    print(cnt)

backtrack2(5,1)