from itertools import permutations


discount_percent = []

def get_candidate(n, path):
    """
    할인율 후보 구하기 
    """

    if len(path) == n:
        discount_percent.append(path)
        return

    for i in range(4):
        get_candidate(n,path+[(i+1) * 10]) 
        
    

def solution(users, emoticons):
    answer = []

    get_candidate(len(emoticons), [])

    max_emoticon_plus = 0
    max_price = 0       
    
    # 완전 탐색 
    for discount_p in discount_percent:               
        emoticon_price = [y - (x * y) / 100 for x,y in zip(discount_p, emoticons)]
        emoticon_plus = 0
        buy_price = 0
                   
        for percent, price in users:
            temp_price = 0
            for idx,p in enumerate(discount_p):
                
                if p >= percent:
                    temp_price += emoticon_price[idx]
                    
            if temp_price >= price:
                emoticon_plus +=1
            else : 
                buy_price += temp_price
                
        if emoticon_plus > max_emoticon_plus:
            max_emoticon_plus = emoticon_plus
            max_price = buy_price
        elif emoticon_plus== max_emoticon_plus and (buy_price >= max_price):
            max_price= buy_price
            
    return [max_emoticon_plus,int(max_price)]