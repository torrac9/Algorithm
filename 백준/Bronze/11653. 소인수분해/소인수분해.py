import sys
import math

a = int(sys.stdin.readline())

def is_prime_number(x):
    for i in range(2, x+1):
        if x%i == 0:
            print(i)
            is_prime_number(x//i)
            return

is_prime_number(a)