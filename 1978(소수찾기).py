import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
c = 0

for i in a:
    s = 1
    if i == 0 or i == 1:
        continue
    else:
        for j in range(2, i):
            if i % j == 0:
                s = 0
        if s == 1:
            c += 1
print(c)