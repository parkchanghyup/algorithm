'''
예산이 적은곳부터 처리해주면된다.
'''


#Summer/Winter Coding(~2018) #예산

from typing import List

def solution(d:List[int], budget:int)->int:
	
    # 모든 예산을 처리할 수 있으면 바로 return
    if sum(d) <= budget:
        return len(d)
        
    d.sort()
    answer =  0
    
    # 예산이 적게드는곳 부터 처리
    for num in d:
        if budget>= num:
            budget-=num
            answer+=1

    return answer
solution([1, 3, 2, 5, 4], 9)