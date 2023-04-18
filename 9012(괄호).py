import sys
n = int(sys.stdin.readline())

for i in range(n):
    s = 0

    ps = list(sys.stdin.readline().strip())

    if len(ps)%2 != 0 or ps[-1] == '(' or ps[0] == ')': #홀수 개이거나 끝이 ( 이거나 시작이 ) 면 NO
        print('NO')
    else:                                               #짝수 개이자, 시작이 (, 끝이 )
        while len(ps) >= 1:
            if ps[-1] == ')':
                s += 1
                ps.pop()
            else:
                ps.pop()
                s -= 1
                if s<0:
                    break
        if s == 0:
            print('YES')
        else: print('NO')