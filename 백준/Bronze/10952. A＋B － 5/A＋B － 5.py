import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

# t = int(sys.stdin.readline())
# arr = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6],
#            [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
# com = []
# for _ in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     if a % 10 == 0:
#         print('10')
#     else:
#         a %= 10
#         result = arr[a][b % len(arr[a]) - 1]
#         print(result)
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0:
        exit()
    print(a+b)
