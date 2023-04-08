a = int(input())
b = int(input())

b3 = b // 100
b2 = (b // 10)%10
b1 = b % 10

print(a*b1, '\n', a*b2, '\n', a*b3, '\n', a*b, sep='')