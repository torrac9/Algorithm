import sys

M, N, L = map(int, sys.stdin.readline().split())
hunter = sorted(list(map(int, sys.stdin.readline().split()))) #헌터는 미리 sort
animal = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
cnt = 0


for a, b in animal:
    start = 0
    end = M-1
    while start < end:
        mid = (start+end)//2

        if hunter[mid] < a:         #동물과 사로의 x좌표 비교
            start = mid +1
        elif hunter[mid] > a:
            end = mid - 1
        else:
            start = mid
            break
    if abs(hunter[start]-a)+b <= L:     #현재의 L보다 작을때
        cnt += 1
    elif start+1 < M and abs(hunter[start+1]-a)+b <= L: #다음 사로의 L보다 작을때
        cnt += 1
    elif start > 0 and abs(hunter[start-1]-a)+b <= L:   #이전 사로의 L보다 작을때
        cnt += 1


print(cnt)