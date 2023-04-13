import sys

N = int(sys.stdin.readline())

def fac(n: int) -> int:
    if n > 0:
        return n*fac(n-1)
    else:
        return 1

print(fac(N))