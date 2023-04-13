import sys
k = 0
N = int(sys.stdin.readline())

for i in range(1, N+1):
    if i <= 99 :
        k += 1
    else:
        num = list(map(int, str(i)))
        if num[0]-num[1] == num[1]-num[2]:
            k += 1
print(k)