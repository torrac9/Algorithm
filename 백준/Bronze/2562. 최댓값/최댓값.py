import sys

# sys.stdin = open("C:/Users/이동근/Desktop/공부/1주차/input.txt", "r")

max1 = 0
idx = 0

for i in range(9):
    a = int(sys.stdin.readline())
    if a > max1:
        max1 = a
        idx = i

print(max1)
print(idx+1)