import sys

n = int(sys.stdin.readline())
arr = [1000000]

for i in range(n):
    height = int(sys.stdin.readline())

    while height >= arr[-1]:
            arr.pop()
    arr.append(height)

#print(arr)
print(len(arr)-1)