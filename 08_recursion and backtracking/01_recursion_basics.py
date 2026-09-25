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

# backtrack1(5,5)

# backtracking 2 --> print n to 1

def backtrack2(n, cnt):
    if cnt > n:
        return
    backtrack2(n, cnt+1)
    print(cnt)

# backtrack2(5,1)

# backtracking 3 --> sum of n nums 

def backtrack3(n):
    if n == 0:
        return 0
    return n + backtrack3(n-1)

# val = backtrack3(3)
# print(val)


# backtracking 4 -> factorial of n

def backtrack3(n):
    if n == 1:
        return 1
    return n * backtrack3(n-1)

# val = backtrack3(5)
# print(val)


# backtracking 5 -> reverse an array 
temp = []
def reverse(arr, i):
    if i >= len(arr):
        return
    reverse(arr, i+1)
    temp.append(arr[i])
    print(temp)

# arr = [1,2,3,4,5]
# reverse(arr, 0)

# backtracking 6 -> reverse an array - 2 pointers
def reverse2(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverse2(arr, l+1, r-1)
    print(arr)

arr = [1,2,3,4,5]
reverse2(arr, 0, len(arr)-1)

# backtracking 7 -> reverse an array - 1 pointer
def reverse3(arr,i):
    if i >= len(arr) // 2:
        return
    arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    reverse3(arr, i+1)
    print(arr)

# arr = [1,2,3,4,5]
# reverse3(arr, 0)

# backtracking 8 -> check if string is palindrome or not

def palindrome(s, i):
    if i >= len(s) // 2:
        print(True)
        return True
    if s[i] != s[len(s)- i - 1]:
        print(False)
        return False
    return palindrome(s, i+1)

palindrome("aba", 0)

