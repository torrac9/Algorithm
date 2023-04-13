import sys

wid, hei = list(map(int, sys.stdin.readline().split()))
line = int(sys.stdin.readline())
x = [0, wid]
y = [0, hei]

for i in range(line):
    num = list(map(int, sys.stdin.readline().split()))

    if num[0] == 1:
        x.append(num[1])
    else: y.append(num[1])
x.sort()
y.sort()
a = []
b = []

for i in range(len(x)) :
    a.append(x[i] - x[i-1])
for i in range(len(y)) :
    b.append(y[i] - y[i-1])
a.sort()
b.sort()

a.reverse()
b.reverse()
print(a[0]*b[0])

#     if roc == 0 and num > row:
#         num1 = num - row
#         if hei - num1 > num1:
#             hei2 = hei - num1
#         else: hei2 = num1
#         row = num
#     elif roc == 1 and num > col:
#         num2 = num - col
#         if wid - num2 > num2:
#             wid2 = wid - num2
#         else: wid2 = num2
#         col = num
# print(hei2*wid2)