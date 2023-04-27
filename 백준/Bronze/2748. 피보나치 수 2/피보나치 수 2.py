import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

d = [0] * 91
d[1] = 1
d[2] = 1
n = int(sys.stdin.readline())

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])