
# def isPrime(n):
#     for i in range(2,n):
#         if n % i == 0 :
#             print(True)
#             return True
#     return False

import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i != 0:
            return True
        return False
        

isPrime(7)