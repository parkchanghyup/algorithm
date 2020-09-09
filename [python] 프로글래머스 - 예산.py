#Summer/Winter Coding(~2018) #예산

from typing import List
def solution(d:List[int], budget:int)->int:
    if sum(d) <= budget:
        return len(d)
    d.sort()
    answer =  0
    for num in d:
        if budget>= num:
            budget-=num
            answer+=1
        
    return answer
solution([1, 3, 2, 5, 4], 9)