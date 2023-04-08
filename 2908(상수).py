import sys

A, B = list(map(str, sys.stdin.readline().split()))

C = list(reversed(A))
D = list(reversed(B))

AC = int(C[0]+C[1]+C[2])
BD = int(D[0]+D[1]+D[2])
if AC > BD :
    print(AC)
else : print(BD)