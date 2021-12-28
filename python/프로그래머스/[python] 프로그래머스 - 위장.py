'''
옷 종류별로 딕셔너리를 생성하고 경우의 수를 계산해준다.
경우의 수를 계산할때는 딕셔너리 길이에 + 1을 하여 계산해준다(입지 않는경우의수)
그리고 하나도 입지 않는 경우는 존재하지 않으므로 마지막에 -1을 하여 return 한다.
'''


import collections

def solution(clothes):
    
    dic = collections.defaultdict(list)
    
    # 옷종류별로 딕셔너리 생성
    for a,b in clothes: 
        dic[b].append(a)
    
    answer = 1
    
    # 경우의 수 계산
    for _ in dic:
        answer *= (len(dic[_])+1)
    
    # -1 하여 return
    return answer-1