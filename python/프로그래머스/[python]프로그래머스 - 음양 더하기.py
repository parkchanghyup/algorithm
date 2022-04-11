def solution(absolutes, signs):
    answer = 0
    a = False
    
    for num,boolen in zip(absolutes,signs):
        if boolen:
            answer +=num
        else :
            answer -= num
    return answer
