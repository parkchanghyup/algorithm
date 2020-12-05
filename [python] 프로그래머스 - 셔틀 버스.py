def solution(n, t, m, timetable):
    # 입력값 분 단위로 통일
    timetable = [int(time[:2])*60+int(time[3:]) for time in timetable]
    timetable.sort()
    
    start = 540
    
    for _ in range(n):
        for _ in range(m):
            #대기가 있는 경우 1초전 도착
            if timetable and timetable[0] <=start:
                candidate = timetable.pop(0)-1
            else : #대기가 없으면 정시 도착
                candidate = start
        
        start +=t
        
    h,m  = divmod(candidate,60)
    
    return str(h).zfill(2)+':'+str(m).zfill(2)