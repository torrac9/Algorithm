import sys

N, R, C = map(int, sys.stdin.readline().split())
def Z(N, r, c):
    if N == 0:
        return 0
    return 2*(r%2)+(c%2) + 4*Z(N-1,r//2, c//2) #0, 1, 2, 3 칸으로 위치를 특정하고 4의 배수로 더해준다

print(Z(N, R, C))