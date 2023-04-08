import sys
import math

A, B, V = list(map(int, sys.stdin.readline().split()))
print(math.ceil((V-A)/(A-B))+1)

# V = (A-B)N + A
# N = (V-A)/(A-B)


# One = A - B # 하루에 올라가는 거리
# if V%One == 0:
#     Total = V // One - B
#     print(Total)
# else :
#     Total = V // One # 대충 올라간 시간
#     print(Total)

# import sys        #함수

# A, B, V = list(map(int, sys.stdin.readline().split()))
# Total = day = 0

# while V >= Total :
#     Total += A
#     day += 1
#     if Total >= V :
#         break
#     Total -= B
# if (Total - A) >= V :
#     print(day-1)
# else : print(day)