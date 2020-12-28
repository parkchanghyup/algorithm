import heapq



def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    
    while scoville[0] < K:
        
        if len(scoville) < 2 :
            break
            
        answer +=1
        lo_1 = heapq.heappop(scoville)
        lo_2 = heapq.heappop(scoville)
        heapq.heappush(scoville,lo_1+lo_2*2)
        
    if scoville[0] < K:
        return -1
    return answer