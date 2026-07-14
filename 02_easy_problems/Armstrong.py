def armStong(x):
    dup, num = x, 0
    while x > 0:
        rem = x % 10
        x = x // 10
        num += rem ** 3
    print(num == dup)
    return num == dup

x = int(input())
armStong(x)