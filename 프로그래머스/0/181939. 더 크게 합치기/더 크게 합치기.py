def solution(a, b):
    answer = int(str(b) + str(a))
    answer1 = int(str(a) + str(b))
    
    return max(answer, answer1)