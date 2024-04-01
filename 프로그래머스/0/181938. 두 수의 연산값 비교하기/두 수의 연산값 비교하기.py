def solution(a, b):
    answer = int(str(a) + str(b))
    answer1 = 2*a*b
    return max(answer, answer1)