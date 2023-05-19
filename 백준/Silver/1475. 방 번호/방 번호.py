import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n = list(sys.stdin.readline().strip())
arr = [0] * 10
result = 0

for i in n:
    arr[int(i)] += 1
if (arr[6] + arr[9])%2 == 0:
    sn = (arr[6] + arr[9]) // 2
else:
    sn = ((arr[6] + arr[9]) // 2)+1

arr[6] = arr[9] = sn

for i in arr:
    result = max(result, i)

# print(n)
# print(arr)
print(result)