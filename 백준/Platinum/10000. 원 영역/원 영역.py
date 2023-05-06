import sys
import heapq

n = int(sys.stdin.readline())
circles = []

for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    end = x + r
    dist = 2 * r
    circles.append((end, dist))

circles.sort()

h = []
cnt = 1
for i in range(n):
    end, dist = circles[i]
    start = end - dist
    can_fill = False
    last_point = end
    while h:
        e, d = heapq.heappop(h)
        e = -e
        if e <= start:
            heapq.heappush(h, (-e, d))
            break
        if e != last_point and e - d >= start:
            continue
        if e - d >= start:
            last_point = e - d
        if last_point == start:
            can_fill = True
    cnt += 1
    if can_fill: 
        cnt += 1
    heapq.heappush(h, (-end, dist))
        
print(cnt)
# import sys
# from collections import deque

# N = 10
# circles = [[-9, 31], [-9, 7], [-6, 4], [-6, -2], [-2, 2], [-2, 0], [2, 4], [7, 23], [7, 15], [23, 31]]
# stack = deque()
# temp = []

# count = 1 + N

# # circles.sort(key=lambda x: (x[0], -x[1]))

# for i in circles:
#     while stack:
#         value = stack.pop()
#         temp.append(value)
#         if i == value:
#             count += 1
#             break

#         elif i[0] == value[0]:
#             stack.append([min(i[1], value[1]), max(i[1], value[1])])
#             break

#     stack.append(i)
# print(count)




# import sys

# n = int(sys.stdin.readline())
# sol = n+1
# arr = []
# for i in range(n):
#     x, r = map(int, sys.stdin.readline().split())
#     xl, xr = x-r, x+r
#     arr.append([xl, xr])


# print(arr)