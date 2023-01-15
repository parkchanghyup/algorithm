from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine).most_common()
    for item, item_num in cnt:
        k = k-item_num
        answer += 1
        if k <= 0:
            return answer
        
        
    
    return answer
