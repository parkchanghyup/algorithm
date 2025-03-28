def check_level(level, diffs, times, limit):
    # 해당 level일때, 주어진 limit 안에 해결 가능한지 확인
    N = len(diffs)
    time_prev = 0
    spent_time = 0
    for idx in range(N):
        diff = diffs[idx]
        time = times[idx]
        if diff <= level:
            # 현재 퍼즐 푸는 시간 만큼 전체 시간에 더하고
            spent_time += time
            # time_prev 변수 초기화
            time_prev = time
            
        else:
            cnt = diff - level
            spent_time += cnt * (time + time_prev)
            spent_time += time
            time_prev = time
        
        if spent_time > limit :
            return False
    
    if spent_time > limit :
        return False
    return True
            
        
        

def solution(diffs, times, limit):
    # 현재 퍼즐의 난이도를 diff, 
    # 현재 퍼즐의 소요 시간을 time_cur, 
    # 이전 퍼즐의 소요 시간을 time_prev, 
    # 당신의 숙련도를 level
    # diff ≤ level이면 퍼즐을 틀리지 않고 time_cur만큼의 시간을 사용하여 해결합니다.
    
    # diff > level 이면 퍼즐을 총 diff-level번 틀리고
    # 틀릴때 마다 time_cur만큼의 시간을 추가로 사용하고
    # 추가로 time_prev 만큼의 시간을 사용해서 이전 퍼즐을 다시 풀고와야됨
    # 이전 퍼즐을 해결할때는 time_cur 만큼의 시간만 사용 무조건
    
    
    min_level = 1
    max_level = max(diffs) * len(diffs)
    
    
    while min_level < max_level:
        mid_level = (min_level + max_level) // 2
        if check_level(mid_level, diffs, times, limit):
            max_level = mid_level 
        else:
            min_level = mid_level +1
            
    return min_level