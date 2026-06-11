def divisors(n):
    nums = []
    for i in range(n):
        if i > 0 and n % i == 0:
            nums.append(i)
    print(nums)
    return nums

x = int(input())
divisors(x)