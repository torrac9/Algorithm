def solution(arr, queries):
    for query in queries:
         for i in range(query[0], query[1]+1):
                if i%query[2] == 0:
                    arr[i] += 1
    print(arr)
    return arr