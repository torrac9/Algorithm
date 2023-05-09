import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

# def cantor(num, start):
#     num -= 1
#     for i in range(len(arr)):
#         if 3**num + start <= i <= (3**num)*2-1 + start:
#             arr[i] = ' '
#     if num > 0:
#         cantor(num, start)
#         cantor(num, start + (3**num)*2)
    
#     print(*arr, sep='')
#     if arr[-2] == ' ':
#         return arr

# while True:
#     try:
#         n = int(sys.stdin.readline())
#         if n == 0:
#             print('-')
#         else:
#             arr = ['-' for _ in range(3**n)]
#             print(*cantor(n, 0), sep= '')
#     except:
#         break
def cantor(n):
    if n == 1:
        print('-', end='')
        return
    n = n//3
    cantor(n)
    for i in range(n):
        print(' ', end='')
    cantor(n)
    return

while True:
    try:
        n = int(sys.stdin.readline())
        cantor(3**n)
        print()
    except:
        break