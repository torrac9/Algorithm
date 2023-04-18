import sys

a, b, c = map(int, sys.stdin.readline().split())

def devide(a, b, c):
    if b == 1:      #1로 끝
        return a%c
    elif b == 0:    #0으로 끝
        return (a*a)%c
    elif b%2 == 0:      #짝수
        if b > 1:
            return ((devide(a, b//2, c))**2) %c
    elif b%2 != 0:      #홀수
        if b > 1:
            return ((devide(a, b//2, c)**2)*a) %c

sol = devide(a, b, c)
print(sol)