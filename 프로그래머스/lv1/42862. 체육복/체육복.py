def solution(n, lost, reserve):
    s_reserve = set(reserve)-set(lost)
    s_lost = set(lost) - set(reserve)
    
    for i in s_reserve:
        if i-1 in s_lost:
            s_lost.remove(i-1)
        elif i+1 in s_lost:
            s_lost.remove(i+1)
    answer = n - len(s_lost)
    return answer