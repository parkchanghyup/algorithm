from itertools import permutations

def func(cand,k, dungeons)
    k = k
    dungeons = dungeons
    
    cnt = 0
    
    for i in cand
        dungeon = dungeons[i]
        
        if k = dungeon[0]
            k -= dungeon[1]
            cnt +=1
        else  
            return cnt
    
    return cnt


def solution(k, dungeons)
    answer = 0
    cands = list(permutations(range(len(dungeons)),len(dungeons)))
    
    for cand in cands
        cnt = func(cand,k, dungeons)
        
        if answer = cnt  
            answer = cnt
            
    return answer


solution(80,[[80,20],[50,40],[30,10]])