from collections import deque

def solution(people, limit):
    
    people.sort()
    people = deque(people)
    
    result = 0
    
    
    while people:
        # 제일 많이나가는사람과 제일 가벼운 사람을 함께태움
        sum_weight = people[0] + people[-1] 
        
        if sum_weight <= limit:
            people.pop()
            # pop() 연산에서 people 덱이 빌수도 있기 때문에 조건문 추가
            if people:
                people.popleft()
        # 불가능하면 제일 무거운사람만 내보낸다.
        else:
            people.pop()
            
        result+=1
    return result