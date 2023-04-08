import sys
n = 0

T = int(input())

for k in range(T) :
    R, S = list(map(str, sys.stdin.readline().split()))
    R = int(R)
    for i in S :
        for j in range(R) :
            print(i, end='')
            n += 1
            if n == R*len(S) :
                print('')
                n = 0