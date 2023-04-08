import sys

c = int(input())

for i in range(c) :
    sum = avr = s = 0
    a = list(map(int, sys.stdin.readline().split()))

    for j in a[1:] :
        sum += j
    avr = sum/a[0]
    for j in a[1:] :
        if j > avr :
            s += 1
    p = s*100/a[0]
    print(f"{p:.3f}%")

# n = int(input())
# s = sum = 0
# a = []

# for i in range(n) :
#     a.append(list(map(int,input().split())))
# for i in range(n) :
#     k = a[n-1][0]
#     for j in range(k) :
#         sum += a[n-1][j+1]
#     avr = sum / k
#     for j in range(k) :
#         if a[n-1][j+1] > avr :
#             s += 1
#     p = s*100/k
#     print(f"{round(p,3)}%")
# print(avr, sum, s, k, a)