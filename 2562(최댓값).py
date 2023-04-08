a= [None] * 9
for i in range(1, 10) :
    a[i-1] = int(input())

print(max(a))
print(a.index(max(a))+1)