from itertools import chain

def solution(n):
    maps = [[0] * n for _ in range(n)]
    
    x,y = 0,-1
    number = 0
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                y+=1
            elif i%3 ==1 :
                x +=1
            elif i%3 ==2 :
                x-=1
                y-=1
            number +=1
            maps[y][x] = number
    result = [x for x in chain(*maps) if x != 0]
    return result