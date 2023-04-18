n, s = map(int, input().split())            # 정수의 개수 n, 정수s
num_list = list(map(int, input().split()))  # 정수 n개

cnt = 0
picked = [False] * n    # 중복선택 방지 목적
temp = []               # 현재 순회중인 케이스 저장

def dfs (start, l) : 
    global cnt
    # 0개선택 방지
    if len(temp) == l and sum(temp) == s :
        cnt += 1
        print(temp)
        return
    elif len(temp) > l:
        return

    # if len(temp) == n :
    #     return

    # 인덱스 번호로 순회
    for i in range (start,n) : 
        #if not picked[i] :
        #picked[i] = True
        temp.append(num_list[i])
        dfs(i+1, l)
        #picked[i] = False
        temp.pop()
for i in range(n):
    dfs(0,i)
if sum(num_list) == s: #모든 원소를 가질 때
    cnt += 1
if s == 0:  
    cnt -= 1 # ''제외
print(cnt)