import sys
from collections import deque
#sys.stdin = open("C:/Users/82103/Desktop/KraftonJungle/BOJ/input.txt", "r")

N = deque(sys.stdin.readline().strip())
index = len(N)
cnt = 0
M = int(sys.stdin.readline())
for i in range(M):
    cmd = sys.stdin.readline().strip()
    # print(cmd)
    if cmd[0] == "L" and index > 0:
        index -= 1
        cnt -= 1
        N.rotate(1)
    if cmd[0] == "D" and index < len(N):
        index += 1
        cnt += 1
        N.rotate(-1)
    if cmd[0] == "B" and index != 0:
        # N = N[0: index -1] + N[index :]
        N.pop()
        index -= 1
    if cmd[0] == "P":
        # N = N[0: index] + cmd[2] + N[index :]
        N.append(cmd[2])
        index += 1

# print(index)
# print(cnt)
if cnt > 0:
    for _ in range(cnt):
        N.rotate(1)
elif cnt < 0:
    for _ in range(-cnt):
        N.rotate(-1)
for i in N:
    print(i, end="")