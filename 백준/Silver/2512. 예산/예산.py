import sys
#sys.stdin = open("C:\\Users\\82103\\Desktop\\Krafton Jungle\\BOJ\\input.txt", "r")

n = int(sys.stdin.readline())
requests = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
left = 0
right = max(requests)
sum = 0
result = 0

while right >= left:
    mid = (right + left) // 2

    for i in requests:
        if i > mid:
            sum += mid
        else:
            sum += i
        
    if sum <= m:
        result = mid
        left = mid+1
        sum = 0
    else:
        right = mid-1
        sum = 0
print(result)

# def binary(requests, start, end):
#     sum = 0
#     if end - start == 1:
#         return start
#     if start >= end:
#         return end-1
#     mid = (start + end) // 2
#     for i in requests:
#         if i < mid:
#             sum += i
#         else:
#             sum += mid
#     if sum > m:
#         return binary(requests, start, mid)
#     else:
#         return binary(requests, mid, end)
    
# if m >= sum(requests):
#     print(max(requests))
#     exit()

# response = binary(requests, n, max(requests))
# #print(requests)
# print(response)