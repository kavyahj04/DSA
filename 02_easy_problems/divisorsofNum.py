# def divisors(n):
#     nums = []
#     for i in range(n):
#         if i > 0 and n % i == 0:
#             nums.append(i)
#     print(nums)
#     return nums

import math

def divisors(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0 and  i != n // i: 
            print(i, int(n/i))

divisors(8)