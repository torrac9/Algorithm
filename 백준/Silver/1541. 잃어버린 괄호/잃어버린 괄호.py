import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

arr = sys.stdin.readline().split('-')
sol = []

for i in arr:
    pl = list(map(int, i.split('+')))
    ans = sum(pl)
    sol.append(ans)
for i in range(len(sol)):
    if i != 0:
        sol[0] -= sol[i]
print(sol[0])