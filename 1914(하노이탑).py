import sys

def hanoi(n, x, y):

    if n <= 20:
        if n > 1:
            hanoi(n-1, x, 6-x-y) #원판 갯수가 홀/짝일 때 다름
        print(x,y)
        if n > 1:
            hanoi(n-1,6-x-y,y)

n = int(sys.stdin.readline())

print(2**n-1)
hanoi(n, 1, 3)