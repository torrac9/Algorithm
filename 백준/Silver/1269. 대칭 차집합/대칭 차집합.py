import sys
#sys.stdin = open("C:/Users/82103/Desktop/KraftonJungle/BOJ/input.txt", "r")

na, nb = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
result = A+B
setres = list(set(result))

# print(result)
# print(setres)
print(len(result)-(len(result)-len(setres))*2)