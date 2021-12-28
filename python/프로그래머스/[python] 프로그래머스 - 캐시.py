from typing import List
import collections
def solution(cacheSize: int, cities:List[str])->int:
    answer:int = 0
    deque = collections.deque(maxlen = cacheSize)
    
    for i in cities:
        i = i.lower()
        if i in deque:
            deque.remove(i)
            deque.append(i)
            answer+=1
        else:
            deque.append(i)
            answer+=5
            
    
    return answer