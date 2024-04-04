def solution(arr, queries):
    answer = []
    for i in queries:
        arr1 = arr[i[0] : i[1]+1 : ]
        arr2 = []
        for j in arr1:
            if j > i[2]:
                arr2.append(j)
        if arr2:
            answer.append(min(arr2))
        else:
            answer.append(-1)
    return answer