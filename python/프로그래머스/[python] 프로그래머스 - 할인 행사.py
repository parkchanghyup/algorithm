from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_list = []

    
    cnt = 0
    for item, num in zip(want,number):
        for i in range(num):
            want_list.append(item)
            
    want_counter = Counter(want_list)
    
    for i in range(len(discount) - 9):
        
        can_buy = discount[i:i+10]
        temp_counter = Counter(can_buy)
        if temp_counter == want_counter:
            cnt += 1
    return cnt
