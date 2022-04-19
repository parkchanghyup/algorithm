def solution(price, money, count):
    for i in range(count+1):
        money -= price * i
        
    if money >= 0 :
        return 0
    return -money