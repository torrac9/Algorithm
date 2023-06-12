import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while(scoville[0] < K and len(scoville) >= 2):
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+(b*2))
    if(scoville[0] < K):
        answer = -1
    return answer