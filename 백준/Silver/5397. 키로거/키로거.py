import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n = int(sys.stdin.readline())

for _ in range(n):
    arr = sys.stdin.readline().strip()
    lpw = []
    rpw = []
    for i in arr:
        if i == '-':
            if lpw:
                lpw.pop()
        elif i == '<':
            if lpw:
                rpw.append(lpw.pop())
        elif i == '>':
            if rpw:
                lpw.append(rpw.pop())
        else:
            lpw.append(i)
    lpw.extend(reversed(rpw))
    #print(arr)
    print(*lpw, sep='')