import math
def solution(brown, yellow):
    result = []
    sum = brown + yellow
    sq = sum**(1/2) // 1
    sqr = int(sq + 1)
    for i in range(2, sqr):
        br = i*2 + ((sum//i)-2)*2
        if br == brown and i*(sum//i) == sum:
            return [sum//i, i]
