n = int(input())

a= []
for i in range(n) :
    a.append(list(map(str,input().split('X'))))
for i in range(n) :
    while a[i].count('') > 0:
        a[i].remove('')
for i in range(n) :
    sum=0
    for j in range(len(a[i])):
        b=int(len(a[i][j]))
        sum+=b*(b+1)//2
    print(sum)
print(a)