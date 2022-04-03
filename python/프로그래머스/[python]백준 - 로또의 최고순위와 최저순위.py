def solution(lottos, win_nums):
    
    dic = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    zero = 0
    win = 0
    for lotto in lottos:
        if lotto == 0:
            zero +=1
            continue
        if lotto in win_nums:
            win +=1
    print(win,zero)
    answer = [dic[win+zero],dic[win]]
    return answer
