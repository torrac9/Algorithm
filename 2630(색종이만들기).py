import sys

n= int(sys.stdin.readline())
arr=[]
white = blue = 0

for i in range(n):
    arr.append(list(map(int,input().split())))

def cut(n, x, y):
    global white, blue
    define = 0
    #while n >= 1:
        #print('0')
        #if arr[x][y] == 0:
    for i in range(1, n+1):
        for j in range(1, n+1):
            define += arr[x+i-1][y+j-1]
    if define == n**2:
            blue += 1
    elif define == 0:
            white += 1
    else: 
        cut(n//2, x, y)
        cut(n//2, x+n//2, y)
        cut(n//2, x, y+n//2)
        cut(n//2,x+n//2, y+n//2)
    return

cut(n, 0, 0)

print(white)
print(blue)