from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(info, query):
    answer = []
    
    dic = {}
    
    # 그룹 생성
    lagauges = ['cpp','java','python','-']
    jobs  = ['backend','frontend','-']
    careers = ['junior','senior','-']
    foods = ['chicken','pizza','-']
    
    group = []
    for lagauge in lagauges:
        for job in jobs:
            for career in careers:
                for food in foods:
                    dic[lagauge +','+ job +','+ career +','+ food] = []
                    
    # 유저를 그룹에 매핑
    for people in info:
        people_info = people.split(' ')
        for lagauge in ['-',people_info[0]]:
            for job in ['-', people_info[1]]:
                for career in ['-',people_info[2]]:
                    for food in ['-',people_info[3]]:
                        dic[lagauge +','+ job +','+ career +','+ food].append(int(people_info[4]))
                        
    # score 정렬
    for value in dic.values():
        value.sort()   
    
    for q in query:
        lagauge, job, career, food_score = q.split(' and ')
        food, score = food_score.split(' ')
        scores = dic[lagauge +','+ job +','+ career +','+ food]

        # 이분 탐색
        idx = bisect_left(scores, int(score))
        answer.append(len(scores)-idx)
    
    return answer
