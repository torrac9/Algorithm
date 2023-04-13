import sys
arr = []*9

for i in range(9):
    arr.append(int(sys.stdin.readline()))
arr.sort()
total = sum(arr)
h = total - 100

for i in arr:
    for j in arr:
        if i+j == h and i != j:
            arr.remove(i)
            arr.remove(j)
            for k in arr:
                print(k)
            sys.exit()