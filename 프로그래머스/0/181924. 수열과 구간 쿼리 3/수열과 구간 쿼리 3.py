def solution(arr, queries):
    for j in queries:
        a = arr[j[0]]
        b = arr[j[1]]
        arr[j[0]] = b
        arr[j[1]] = a
   
    return arr