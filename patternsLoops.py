def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("* ", end = "")
        print()


def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print("")

def pattern3(n):
    for i in range(n):
        n = 1
        for j in range(i + 1):
            print(n, end = "")
            n += 1
        print("")

def pattern4(n):
    num = 1
    for i in range(n):
        for j in range(i + 1):
            print(num, end = "")
        num+=1
        print("")

def pattern5(n):
    for i in range(n):
        for j in range(n - i):
            print("* ", end = "")
        print("")

def pattern6(n):
    for i in range(n):
        num = 1
        for j in range(n - i):
            print(str(num) + " " , end = "")
            num += 1
        print("")
        

def pattern7(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end = "")
        for j in range(2 * i + 1):
            print("*", end = "")
        for k in range(n - i - 1):
            print(" ", end = "")
        print("")

def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" ", end = "")
        for k in range(2*n - (2 * i + 1)):
            print("*", end = "")
        for l in range(i):
            print(" ", end = "")
        print("")

def pattern9(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end = "")
        for j in range(2 * i + 1):
            print("*", end = "")
        for k in range(n - i - 1):
            print(" ", end = "")
        print("")
    for i in range(n):
        for j in range(i):
            print(" ", end = "")
        for k in range(2*n - (2 * i + 1)):
            print("*", end = "")
        for l in range(i):
            print(" ", end = "")
        print("")

def pattern10(n):
    for i in range(2*n - 1):
        stars = i + 1 if i < n else (2*n - i) - 1
        for j in range(stars):
            print("*", end = "")
        print("")
    
def pattern11(n):

    for i in range(n):
        if i % 2 == 0:
            num = 0
        else:
            num = 1
        for j in range(i + 1):
            num = 1 - num
            print(num, end = "")
            
        print("")


def pattern12(n):
    for i in range(n):
        num = 1
        for j in range(i + 1):
            print(str(num), end = "")
        for k in range((2 * n) - (2 * (i + 1))):
            print(" ", end = "")
        for l in range(i + 1):
            print(str(num),  end = "")
        print("")

def pattern13(n):
    for i in range(n):
        num = 1
        for j in range(i + 1):
            print(str(num), end = "")
            num += 1
        for k in range((2 * n) - (2 * (i + 1))):
            print(" ", end = "")
        for l in range(i + 1):
            num -= 1
            print(str(num),  end = "")
            
        print("")

num = int(input())
pattern13(num)