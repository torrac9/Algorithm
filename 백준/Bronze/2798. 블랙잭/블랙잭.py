import sys
import itertools
#sys.stdin = open("C:/Users/이동근/Desktop/공부/input.txt", "r")

N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
com = list(itertools.combinations(card, 3))
result = []
for i in com:
    result.append(sum(i))
result.sort()
for i in range(len(result)):
    if result[i] > M:
        print(result[i-1])
        exit(0)
print(result[-1])