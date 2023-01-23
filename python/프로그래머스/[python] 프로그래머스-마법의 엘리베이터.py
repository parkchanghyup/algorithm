def solution(storey):
    storey = str(storey)
    storey_list = []
    for num in storey:
        storey_list.append(int(num))
        
        
    
    cnt = len(storey)
    idx = cnt - 1
    answer = 0
    
    while idx > 0:

        if storey_list[idx] == 5 and storey_list[idx-1] == 9:
            answer += 6
            storey_list[idx-1] += 1
        
        elif storey_list[idx] > 5 :
            answer = answer + (10 - storey_list[idx] )
            storey_list[idx-1] += 1

        else :
            answer += storey_list[idx]
        
        idx -= 1
        
    
    if storey_list[0] == 9:
        return answer + 2
    
    elif storey_list[0] ==10:
        return answer + 1
    else :
        return answer + min(10-storey_list[0],storey_list[0])
        
        
    return answer

solution(95)

