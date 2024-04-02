def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if not mode and code[i] != '1':
            if not i%2:
                answer += code[i]
        elif mode and code[i] !='1':
            if i%2:
                answer += code[i]
        if code[i] == '1':
            mode = not mode
    return answer if answer else "EMPTY"