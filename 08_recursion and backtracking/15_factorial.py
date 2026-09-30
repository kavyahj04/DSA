def getPermutation(n, k):
    fact = 1
    numbers = []

    for i in range(1, n):
        fact *= i
        numbers.append(i)
    numbers.append(n)
    k = k - 1
    ans = []
    while True:
        idx = k // fact
        ans.append(str(numbers[idx]))
        numbers.pop(idx)
        if len(numbers) == 0:
            break
        k = k % fact
        fact = fact // len(numbers)

    return "".join(numbers)