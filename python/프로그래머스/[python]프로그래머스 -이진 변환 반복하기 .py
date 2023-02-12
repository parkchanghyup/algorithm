
def solution(s):
    answer = [0,0]
    
    while s != '1':
        temp_s = ''
        for char in s:
            if char == '0':
                answer[1]+=1
            else :
                temp_s+=str(char)
        
        s = str(bin(len(temp_s)))[2:]
        answer[0]+=1    
        
    return answer
