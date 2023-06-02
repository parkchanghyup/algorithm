
def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    
    low = 1
    high = distance
    
    
    while low <= high:
        
        mid = (low+high) // 2 # 거리의 최솟값
        cnt = 0 # 제거된 바위의 수  
        left_rock = 0 # 왼쪽 바위 
        
        for rock in rocks:

            # 왼쪽 바위와의 거리가 mid 이상이라면 제거
            # 왼쪽 바위 위치 업데이트 x, 제거된 바위의 수 업데이트
            if rock - left_rock < mid: 
                cnt += 1
            # 바위를 제거하지 않아도 되는 경우
            else :
                left_rock = rock
        # 제거해야하는 바위의 수가 n보다 작거나 같은 경우
        # 정답으로 사용 가능한 경우이고, mid를 증가 시켜도 됨.
        if cnt <= n :
            low = mid+1
            answer  = mid
        # 제거해야 하는 바위의 수가 n보다 커서 mid를 낮춰야함
        else :
            high = mid - 1           
    
    
    return answer