A = int(input())
B = int(input())
C = int(input())
d = A*B*C
d = str(d)

for i in range(0, 10) :
    i = str(i)
    L = d.split(i)

    print(len(L)-1)