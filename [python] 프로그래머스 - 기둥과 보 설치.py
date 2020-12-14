def check(answer)->bool:
    
    for x,y,kind in answer:
        
        if kind ==0:
            if y==0 or (x-1,y,1) in answer or (x,y,1) in answer or (x,y-1,0) in answer:
                continue
        else :
            if  (x,y-1,0) in answer or ((x-1,y,1)in answer and( x+1,y,1)in answer )or (x+1,y-1,0)in answer:
                continue
                
        return False
    
    return True

def solution(n, build_frame):
    answer = set()
    
    for x,y,kind,install in build_frame:
        
        
        if install==1:
            answer.add((x,y,kind))
            
            if check(answer):
                continue
            else:
                answer.remove((x,y,kind))
        #제거
        else :
            answer.remove((x,y,kind))
            if  check(answer):
                continue
            else:
                answer.add((x,y,kind))
    answer = [list(i) for i in answer]
    return sorted(answer)