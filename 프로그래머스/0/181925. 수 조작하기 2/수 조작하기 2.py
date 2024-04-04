def solution(numLog):
    answer = ''
    compass = []
    for i in range(1, len(numLog)):
        compass.append(numLog[i]-numLog[i-1])
    for i in compass:
        if i == 1:
            answer += 'w'
        elif i == -1:
            answer += 's'
        elif i == -10:
            answer += 'a'
        else:
            answer += 'd'
    return answer