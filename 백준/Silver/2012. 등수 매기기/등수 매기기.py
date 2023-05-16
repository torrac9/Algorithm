import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n = int(sys.stdin.readline())
arr = []
result = 0
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

for i in range(n):
    result += abs((i+1)-arr[i])


#print(arr)
print(result)