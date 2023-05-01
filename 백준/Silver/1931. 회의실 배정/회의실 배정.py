import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\Krafton04\\input.txt", "r")

n = int(sys.stdin.readline())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, sys.stdin.readline().split())))
meeting.sort(key = lambda x: (x[1], x[0]))
cnt = 0
start = 0

for i in meeting:
    if i[0] >= start:
        cnt += 1
        start = i[1]

#print(meeting)
print(cnt)