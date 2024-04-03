import sys

# sys.stdin = open("C:/Users/이동근/Desktop/공부/1주차/input.txt", "r")

N = int(sys.stdin.readline())

for i in range(1, 10):
    print(f"{N} * {i} = {N*i}")