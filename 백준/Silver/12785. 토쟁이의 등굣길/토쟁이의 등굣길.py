import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

w, h = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())

d = [0] * 401
d[0] = 1
d[1] = 1

for i in range(2, 401):
    d[i] = i * d[i-1]

if w==x or h==y:
    print((d[x+y-2] // (d[x-1]*d[y-1])) % 1000007)
else:
    print(((d[x+y-2] // (d[x-1]*d[y-1])) * (d[w-x+h-y] // (d[w-x]*d[h-y]))) % 1000007)


# toast = [[0]*x for _ in range(y)]
# school = [[0]*(w-x) for _ in range(h-y)]

# for i in range(x):
#     for j in range(y):
#         toast[j][0] = 1
#         toast[0][i] = 1
# # for i in toast:
# #     print(*i)
# for j in range(1, x):
#     for i in range(1, y):
#         toast[i][j] = toast[i-1][j] + toast[i][j-1]

# if w == x or h == y:
#     print(toast[-1][-1] % 1000007)
#     #exit()
# else:
#     for i in range(w-x):
#         for j in range(h-y):
#             school[j][0] = toast[-1][-1]
#             school[0][i] = toast[-1][-1]
#     for j in range(1, w-x):
#         for i in range(1, h-y):
#             school[i][j] = school[i-1][j] + school[i][j-1]
#     print(school[-1][-1] % 1000007)
# for i in toast:
#     print(*i)
# print()
# for i in school:
#     print(*i)