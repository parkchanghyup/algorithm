#다트게임
def solution(dartResult:str) -> int:
    answer = 0
    number = ['0','1','2','3','4','5','6','7','8','9','10']
    result =[]
    
    for i,num in enumerate(dartResult):
        #i가 숫자이면
        if num in number:
            #숫자 10 처리
            if num == '0' and len(result)>0 and dartResult[i-1]=='1':                
                result[-1]=10
                continue
            result.append(int(num))
        elif num == 'S':
            continue
        elif num == 'D':
            result[-1] = result[-1] **2
        elif num == 'T':
            result[-1] = result[-1]**3
        
        elif num=='#':
                result[-1] = -result[-1]
        else:
            if len(result)==1:
                result[-1]*=2
            else :
                result[-1]*=2
                result[-2]*=2
    
    return sum(result)

solution('1S*2T*3S')
               