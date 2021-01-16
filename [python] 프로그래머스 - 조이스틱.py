def solution(name):
    
    move_up = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
    move_down = ['O','P','Q','R','S','T','U','V','W','X','Y','Z']
    move_down = move_down[::-1]
    
    
    S = [c for c in name]
    # 총 움직임 횟수 
    result = 0
    
    # 커서 위치
    cursor = 0
    
    # 체크할 리스트
    check = ['A'] * len(S)
    
    while True:
        # 현재 커서의 문자
        char = S[cursor]
        
        # 위로 올리는게 빠르면 위로 움직이고 현재 커서는 'A'로 바꿔준다
        if char in move_up:
            result += move_up.index(char)
            S[cursor] = 'A'
            
        # 밑으로 내리는게 빠르면 밑으로 움직이고 현재 커서는 'A' 로 변경
        else :
            result +=move_down.index(char)+1
            S[cursor] = 'A'
            
        # 더이상 바꿀 문자가 없으면 return
        if S== check:
            return result
        
        # 왼쪽으로 가는것이 빠른지 오른쪽으로 가는것이 빠른지 확인하는코드
        
        cursor_l = cursor_r = cursor
        left,right = 0,0
        
        while S[cursor_l] == 'A':
            cursor_l -=1
            if cursor_l < 0 : 
                cursor_l  = len(S)-1
            left +=1
                        
        
        while S[cursor_r] == 'A':
            cursor_r +=1
            if cursor_r >= len(S):
                cursor_r = 0
            right +=1
            
            
        # 왼쪽으로 가는게 빠르면 왼쪽으로이동
        if left < right :
            cursor = cursor_l
            result +=left
        # 오른쪽으로 가는게 빠르면 오른쪽으로 이동
        else:
            cursor = cursor_r
            result+=right
            
solution('BBABAAAB')