# 바깥 영역 +1 하기
# import sys
from collections import deque

N = 10
circles = [[-9, 31], [-9, 7], [-6, 4], [-6, -2], [-2, 2], [-2, 0], [2, 4], [7, 23], [7, 15], [23, 31]]
stack = deque()
temp = []

count = 1 + N

# circles.sort(key=lambda x: (x[0], -x[1]))

for i in circles:
    while stack:
        value = stack.pop()
        temp.append(value)
        if i == value:
            count += 1
            break

        elif i[0] == value[0]:
            stack.append([min(i[1], value[1]), max(i[1], value[1])])
            break

    stack.append(i)
print(count)




# import sys

# n = int(sys.stdin.readline())
# sol = n+1
# arr = []
# for i in range(n):
#     x, r = map(int, sys.stdin.readline().split())
#     xl, xr = x-r, x+r
#     arr.append([xl, xr])


# print(arr)