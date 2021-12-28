'''
heapq을 이용하여 문제에 제시된 조건으로 스코빌 지수를 업데이트시켜주고,
스코빌지수가 K미만이라면 -1을 return해준다.
'''

import heapq



def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    # 스코빌 지수 업데이트
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