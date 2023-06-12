def solution(nums):
    half = len(nums)//2
    kind = len(set(nums))
    answer = min(half, kind)
    print(answer)
    return answer