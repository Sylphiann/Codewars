# kata: https://www.codewars.com/kata/5262119038c0985a5b00029f

# ---
from math import sqrt, floor

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, floor(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

print(is_prime(-41))