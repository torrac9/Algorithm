import sys
#sys.stdin = open("C:/Users/이동근/Desktop/공부/input.txt", "r")

N = int(sys.stdin.readline())

for i in range(N):
    sol = int(i)
    for j in str(i):
        # print(j)
        sol += int(j)
    # print(sol)
    # print()
    if sol == N:
        print(i)
        exit(0)

print(0)
