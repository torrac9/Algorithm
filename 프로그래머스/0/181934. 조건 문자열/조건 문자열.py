def solution(ineq, eq, n, m):
    if n < m:
        if ineq=='<':
            answer = 1
        else:
            answer = 0
    elif n==m:
        if eq=='=':
            answer = 1
        else:
            answer = 0
    else:
        if ineq=='>':
            answer = 1
        else:
            answer = 0
    return answer