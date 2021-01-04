def solution(n, times):
    answer = 0
    low = 0
    high = max(times) * n
    
    while low <= high:
        # 1일당 배정 시간
        mid = (low + high) //2 
        
        count = 0
        for time in times:
            count = count + mid // time
            
            # 모든 인원을 검사 가능 하면 break
            if count >= n:
                break
                
        if count >= n :
            high = mid - 1
            answer= mid
            
        else :
            low = mid +1 
        
    
    return answer
solution(6,[7,10])