import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

n = int(sys.stdin.readline())
x = sorted(list(map(int, sys.stdin.readline().split())))
x.reverse()

for i in range(1, n):
    x[0] += x[i]/2
result = round(x[0], 5)

if result % 1 == 0:
    print(round(result))
else:
    print(result)