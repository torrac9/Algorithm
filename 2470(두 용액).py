import sys

n = int(sys.stdin.readline())
array = sorted(list(map(int, sys.stdin.readline().split())))

def binaray(array, start, end):
    min_len = 2000000000
    min_l = min_r = 0
    while start < end:
        sum = array[start] + array[end]
        #print(start, end)
        if min_len > abs(sum):
            min_len = min(min_len, abs(sum))
            min_l = array[start]
            min_r = array[end]
        if sum > 0:                             #합이 0보다크면 end -1
            end -= 1
        elif sum < 0:                           #합이 0보다 작으면 start+1
            start += 1
        else:                                   #합이 0이면 출력
            print(array[start],array[end])
            return
    #print(min_len)
    print(min_l, min_r)
    return


binaray(array, 0, n-1)