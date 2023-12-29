def solution(clothes):
    hash = {}
    for name, kind in clothes:
        if kind in hash.keys():
            hash[kind] += [name]
        else:
            hash[kind] = [name]
    answer = 1
    for _, value in hash.items():
        answer *= (len(value) + 1)
    
    return answer-1