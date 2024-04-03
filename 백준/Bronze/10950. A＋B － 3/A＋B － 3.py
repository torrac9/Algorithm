import sys

# sys.stdin = open("C:/Users/이동근/Desktop/공부/1주차/input.txt", "r")

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)