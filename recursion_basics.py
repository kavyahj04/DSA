def printNames(count, n):
    if count > n:
        return
    print("Kavya is doing great!!")
    printNames(count + 1, n)

# num = int(input())
# printNames(1, num)

def printLinear(count, n):
    if count > n:
        return
    print(count)
    printLinear(count + 1, n)


# num = int(input())
# printLinear(1, num)

def printReverse(n):
    if n == 0:
        return
    print(n)
    printReverse(n-1)

# num = int(input())
# printReverse(num)


def printLinear2(num, n):
    if num == 0:
        return
    printLinear2(num - 1, n)
    print(num)

# num = int(input())
# printLinear2(num, num)

def printReverse2(num, n):
    if num > n:
        return
    printReverse2(num + 1, n)
    print(num)

# num = int(input())
# printReverse2(1, num)

#sum of first n numbers 

#parameterized
def getSum(n, sum_):
    if n < 1:
        print(sum_)
        return
    getSum(n-1, sum_ + n)

# sum_ = 0
# num = int(input())
# getSum(num, sum_)

#functional
def getSum2(n):
    if n == 0:
        return 0
    return n + getSum2(n-1)


# num = int(input())
# getSum2(num)

#functional
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


# num = int(input())
# fact = factorial(num)
# print(fact)

def reverse(left, right):
    if left >= right:
        print(nums)
        return nums
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp
    reverse(left+1, right - 1)

# nums = [1, 2, 3, 4, 5]
# left, right = 0, len(nums) - 1
# reverse(left, right)

def reverse2(i, arr, n):
    if i >= n/2:
        print(arr)
        return 
    temp = arr[i]
    arr[i] = arr[n-i-1] 
    arr[n-i-1] = temp
    reverse2(i + 1, arr, n)

# nums = [1, 2, 3, 4, 5]
# n = len(nums)
# reverse2(0, nums, n)

def palindrome(i, s, n):
    if i >= n/2:
        print(True)
        return True
    if s[i] != s[n-i-1]:
        print(f"{s[i], s[n-i-1]}, False")
        return False
    palindrome(i + 1, s, n)

# name = "KavyaayvaKL"
# palindrome(0, name, len(name))


## Multiple Recursion Calls
def fib(n):
    if n <= 1:
        return n 
    return fib(n-1) + fib(n-2)

f = fib(3)
print(fib(3))