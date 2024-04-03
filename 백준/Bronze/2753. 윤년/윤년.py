import sys

# sys.stdin = open("C:/Users/이동근/Desktop/공부/1주차/input.txt", "r")

year = int(sys.stdin.readline())

print(1 if year%4 == 0 and year%100 != 0 or year%400 == 0 else 0)