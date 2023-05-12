import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
arr = []
arr.append(a[0]) #초기상태의 arr[0] = a[0]

def binaray(left, right, target):       #새로 만들어줄 LIS의 mid위치에 넣어줄 수 있는가가 관건
    while left < right:
        mid = (left+right)//2

        if arr[mid] < target:
            left = mid + 1
        else: right = mid
    return right

j = 0
index = []          #위치를 저장할 배열

for i in range(n):
    if arr[j] < a[i]:      #현재 arr의 마지막 값보다 a[i]가 크면
        arr.append(a[i])    #마지막 칸에 들어온다
        index.append(j+1)
        j += 1              #배열의 길이 +1
    else:                           #현재 arr마지막 값보다 a[i]가 작으면
        len = binaray(0, j, a[i])   #이분탐색으로 자리를 찾는다
        arr[len] = a[i]             #그 자리와 바꾼다
        index.append(len)
a.reverse()
index.reverse()

print(j+1)
#print(a)
#print(index)
result = []                 # 정답 부분 수열
y = j
for x in range(1, n+1):
    if index[x-1] == y:     #
        result.append(a[x-1])   # 
        y -= 1
result.reverse()
print(*result)