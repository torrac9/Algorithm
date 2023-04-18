import sys

N, M = list(map(int, sys.stdin.readline().split()))

def binary(start, end):
    global result
    if start >= end:
         return None
    
    len = (start+end)//2
    internet = 1 #공유기를 설치하고 시작
    li = array[0]

    for i in range(N):
         if array[i] - li >= len: #공유기가 설치 가능하면 설치함
              internet += 1 
              li = array[i]
    if internet >= M: #공유기 M개 설치시
         return binary(len+1, end) or len
    else: return binary(start, len) #M개 안될 시


array = [int(input()) for i in range(N)]
array.sort()
result = binary(1, array[-1]-array[0])

if M == 2: #공유기가 2개일땐 처음과 끝
    print(array[-1]-array[0])
else:
    print(result)

# 이분탐색은 반복문으로 다시 풀어보자