import sys

# sys.stdin = open("C:/Users/이동근/Desktop/공부/1주차/input.txt", "r")

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for i in A:
    if i < X:
        print(i, end=" ")