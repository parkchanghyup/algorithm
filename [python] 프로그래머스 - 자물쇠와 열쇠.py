from typing import List

# 90도 회전
def rotation(arr):
    n = len(arr)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j]
    return ret

def check(key: List[List[int]], lock: List[List[int]]) -> bool:

    for rot in range(4):
        key = rotation(key)
        pos = False
        list_length = ((len(key) - 1) * 2 + len(lock))
        for i in range(list_length - len(key) + 1):
            if pos == True :
                return True
            for j in range(list_length - len(key) + 1):
                if pos == True :
                    return True
                _list = []
                for _ in range(list_length):
                    __ =[]
                    for _ in range(list_length):
                        __.append(0)
                        
                    _list.append(__)

                # 키 삽입
                for y in range(len(key)):
                    for x in range(len(key)):
                        _list[y + i][x + j] += key[y][x]
                # 자물쇠 삽입
                for y in range(len(lock)):
                    for x in range( len(lock)):

                        _list[y+len(key)-1][x+len(key)-1] += lock[y][x] 
                
                #풀리는지 확인
                pos =True            
                for y in range(len(lock)):
                    if not pos  : break
                    for x in range(len(lock)):
                        if not pos  : break
                        if _list[y+len(key)-1][x+len(key)-1] != 1:
                            pos =False
                            break
    return False

#키 형태변환-> 자물쇠 풀리는지 확인


def solution(key, lock):
    
    return check(key,lock)