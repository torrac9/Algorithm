import sys
from collections import deque
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(sys.stdin.readline().strip())

chess = []
for i in range(n-7):
    for j in range(m-7):
        cnt = 0
        start = board[i][j]
        for k in range(i, i+8):
            for l in range(j, j+8):
                if ((k+l)%2 == (i+j)%2):
                    if board[k][l] != start:
                        cnt += 1
                else:
                    if board[k][l] == start:
                        cnt += 1
        if cnt > 32:
            cnt = 64-cnt
        chess.append(cnt)

print(min(chess))