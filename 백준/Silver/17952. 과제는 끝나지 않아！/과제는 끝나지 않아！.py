import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n = int(sys.stdin.readline())
do = []
result = 0

for _ in range(n):
    homework = sys.stdin.readline().split()

    if homework[0] == '1':
        do.append([int(homework[1]), int(homework[-1])])
        #print(do[-1][-1])
        do[-1][-1] -= 1
        #print('1')
    elif homework[0] == '0'and do:
        do[-1][-1] -= 1
        #print('0')
    if do and do[-1][-1] == 0:
        result += int(do[-1][0])
        do.pop()
        #print(result)
    #print(do)

print(result)