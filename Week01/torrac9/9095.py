# 박희은님 코드

t = int(input())
case_list = [int(input()) for _ in range(t)]

cnt_temp = 0
temp = []
def sum_dfs (target, sum) : 
    global cnt_temp
    if sum == target :
        cnt_temp = cnt_temp + 1
        return
    
    # 1~3 더해보며 순회
    for i in range (1,4) :
        if sum + i <= target : 
            temp.append(i)
            sum_dfs(target, sum + i)
            temp.pop()
        
for case in case_list : 
    sum_dfs(case, 0)
    print(cnt_temp)
    cnt_temp = 0