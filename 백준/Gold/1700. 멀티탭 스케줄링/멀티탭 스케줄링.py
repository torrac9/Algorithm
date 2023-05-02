import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
tool = list(map(int, sys.stdin.readline().split()))

plug = []
result = 0
for i in range(m):
    if tool[i] in plug: #이미 있을 때
        continue
    
    if len(plug) != n:  #빈 공간이 있을 때
        plug.append(tool[i])
        continue
    
    far = 0 #가장 먼 인덱스
    temp = 0
    for p in plug:  #현재 꽂혀있는 플러그
        if p not in tool[i:]:   #앞으로 사용할 플러그
            temp = p
            break
        elif tool[i:].index(p) > far:   #현재까지 가장 먼 플러그보다 멀 때
            far = tool[i:].index(p)
            temp = p
    plug[plug.index(temp)] = tool[i]
    result += 1

print(result)