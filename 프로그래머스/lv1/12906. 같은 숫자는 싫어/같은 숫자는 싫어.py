def solution(arr):
    new_arr = []
    new_arr.append(arr[0])
    for i in arr:
        if new_arr[-1] != i:
            new_arr.append(i)
    answer = new_arr
    return answer