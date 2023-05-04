import sys
import heapq
#sys.stdin = open("input.txt", "rt")

n = int(sys.stdin.readline())
lecture = []
for _ in range(n):
    lecture.append(list(map(int, sys.stdin.readline().split())))
lecture.sort(key = lambda x: (x[1], x[2]))
arr = [0]*(n+1)
room = []
for i in range(1, n+1):
    heapq.heappush(room, i)

h = []
for i in lecture:
    while h and h[0][0] <= i[1]:
        end, r = heapq.heappop(h)
        heapq.heappush(room, r)
    
    r = heapq.heappop(room)
    heapq.heappush(h, [i[2], r])
    arr[i[0]] = r

print(max(arr))
for i in arr[1:]:
    print(i)