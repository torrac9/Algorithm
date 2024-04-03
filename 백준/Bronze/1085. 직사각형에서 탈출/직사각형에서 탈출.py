import sys

# sys.stdin = open("C:/Users/이동근/Desktop/공부/1주차/input.txt", "r")

x, y, w, h = map(int, sys.stdin.readline().split())

print(min(abs(x-w), abs(y-h), x, y))