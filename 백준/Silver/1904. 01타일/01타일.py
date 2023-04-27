import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

n = int(sys.stdin.readline())

arr = [0] * 1000001
arr[1] = 1
arr[2] = 2

for i in range(3, n+1):
    arr[i] = (arr[i-1] + arr[i-2])%15746

print(arr[n])