'''
이분탐색을 통해 심사 최소 시간을 구한다.
각 시간동안 심사관이 심사할 수있는 사람수를 구하여 
총 심사한 사람수가 n 보다 크다면 최소 시간을 줄여나가는 방식으로 이분탐색.
'''


def solution(n, times):
    answer = 0
    low = 0
    high = max(times) * n
    
    while low <= high:
        
        # 입국심사 최소 시간
        mid = (low + high) //2 
        
        count = 0
        for time in times:
            count = count + mid // time
            
            # 모든 인원을 검사 가능 하면 break
            if count >= n:
                break
        
        # 모든 인원을 검사 가능하면 answer을 업데이트 해주고
        # 최소 시간을 줄여나간다.
        if count >= n :
            high = mid - 1
            answer= mid
        # 모든인원을 검사 할수 없으면 최소 시간을 늘린다.
        else :
            low = mid +1 
        
    
    return answer
solution(6,[7,10])