def solution(a, d, included):
    answer = 0
    arr = []
    for i in range(len(included)):
        if included[i]:
            arr.append(a+d*i)
    answer = sum(arr)
    return answer