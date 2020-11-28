from typing import List
import itertools


def solution(nums: List[int]) -> int:
    answer=  0
    comb =list(itertools.combinations(nums,3))
    for a,b,c in comb:
        candidate = sum([a,b,c])
        
        for i in range(2,int(candidate**.5)+1):
            if candidate % i == 0:
                break
        else:
            answer+=1
    return answer