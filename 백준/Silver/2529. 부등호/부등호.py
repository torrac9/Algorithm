import sys
import itertools
#sys.stdin = open("C:/Users/82103/Desktop/KraftonJungle/BOJ/input.txt", "r")

k = int(sys.stdin.readline())
A = sys.stdin.readline().split()
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
per = list(itertools.permutations(nums,k+1))
sol = []

def arr(array, i):
    global sol
    if i == k:
        sol = array
        return
    result = []
    for j in array:
        if A[i] == "<":
            if j[i] < j[i + 1]:
                result.append(j)
        elif A[i] == ">":
            if j[i] > j[i + 1]:
                result.append(j)
    arr(result, i + 1)

arr(per, 0)

max_num = ''.join(map(str, sol[-1]))
min_num = ''.join(map(str, sol[0]))

print(max_num)
print(min_num)

# k+1 자릿수의 숫자를 나열해놓고 (Permutaion으로)
# (최댓값인 k=9일 때 10자릿수, 나열된 숫자의 갯수는 10!)
# 조건A로 걸러서 최댓값, 최솟값 판별