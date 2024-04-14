def solution(my_string, s, e):
    answer = ''
    str = my_string[s:e+1]
    answer = my_string[:s] + str[::-1] + my_string[e+1:]
    return answer