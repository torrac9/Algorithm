import sys

N = int(sys.stdin.readline())
pos = [0] * N
cnt = 0

def q(num):
    for i in range(num):
        if pos[num] == pos[i] or abs(pos[num] - pos[i]) == num - i:
            return 0
    return 1

def dfs(num):
    global cnt
    
    if num == N:
        cnt += 1
        return
    
    for j in range(N):
        pos[num] = j
        if q(num):
            dfs(num + 1)

dfs(0)
print(cnt)


# flag_a = [False]*N
# flag_b = [False]*(2*N-1)
# flag_c = [False]*(2*N-1)

# def Q(k: int) -> None:
#     global cnt
#     for i in range(N):
#         if(     not flag_a[k]
#             and not flag_b[k+i]
#             and not flag_c[k-i+N-1]):
#             pos[k] = i
#             if k == N-1 :
#                 cnt += 1
#             else:
#                 flag_a[i] = flag_b[k+i] = flag_c[k-i+N-1] = True
#                 Q(k+1)
#                 flag_a[i] = flag_b[k+i] = flag_c[k-i+N-1] = False

# Q(0)
# print(cnt)