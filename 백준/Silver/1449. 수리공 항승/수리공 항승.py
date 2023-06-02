import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n, l = map(int, sys.stdin.readline().split())
pipe = list(map(int, sys.stdin.readline().split()))
pipe.sort()
tape = pipe[0] + l - 0.5
cnt = 1

for i in pipe:
    if tape < i:
        tape = i - 0.5 + l
        cnt += 1
    
#print(pipe)
print(cnt)