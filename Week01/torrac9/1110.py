import sys

N = int(sys.stdin.readline())

result = str(N%10) + str((N//10 + N%10)%10)
cnt = 1
while 1:
    if int(result) != N:
        result = str(int(result)%10) + str((int(result)//10 + int(result)%10)%10)
        cnt += 1
    else: break
print(cnt)