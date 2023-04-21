import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
preorder = []

def pretopost(l, r):
    if l > r:
        return
    root = preorder[l]
    index = None
    for i, j in enumerate(preorder[l + 1:], l + 1): #enumerate : list, set, string등을 순서값과 함께 입력으로 받아서 enumerate 객채를 리턴
        if j > root:            #서브트리 분할
            index = i
            break
    if index == None:
        index = r + 1
    pretopost(l+1, index - 1)
    pretopost(index, r)
    print(root, end=' ')        #마지막에 root 출력

while 1:
    try:
        node = int(input())
        preorder.append(node)
    except:
        break

pretopost(0, len(preorder)-1)