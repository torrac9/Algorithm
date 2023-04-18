import sys

n = int(sys.stdin.readline())
sol = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        sol.pop()
    else:
        sol.append(num)
print(sum(sol))