def solution(num_list):
    mul = 1
    sqr = 0
    for i in num_list:
        sqr += i
        mul *= i
    return 1 if mul < sqr**2 else 0