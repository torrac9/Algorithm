import sys

# sys.stdin = open("C:/Users/이동근/Desktop/공부/1주차/input.txt", "r")

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())

a = num1 * int(str(num2)[2])
b = num1 * int(str(num2)[1])
c = num1 * int(str(num2)[0])

print(num1 * int(str(num2)[2]))
print(num1 * int(str(num2)[1]))
print(num1 * int(str(num2)[0]))
print(a + b*10 + c*100)