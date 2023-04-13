import sys

N = int(sys.stdin.readline())
array = []

for i in range(N):
     word = array.append(str(sys.stdin.readline().strip()))

array = list(set(array))
array.sort()
array.sort(key=len)

for j in array:
         print(j)
         

# for i in range(1, N):
#     for j in range(i, 0 ,-1):
#         if len(array[j-1]) > len(array[j]):
#             array[j-1],array[j] = array[j], array[j-1]
# for i in range(1, N):
#     for j in range(i, 0, -1):
#         if len(array[j-1]) == len(array[j]):
#             if array[j-1] > array [j]:
#                 array [j-1], array[j] = array[j], array[j-1]