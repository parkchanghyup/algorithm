def solution(n):
    
    three = ''
    
    # 3진법 변환
    while n>2 :
        n,m = divmod(n,3)
        three += str(m)
    
    three += str(n)
    
    
    return int(three,3)
