def solution(n):
    answer = 0
    
    for num in str(n):
        answer = answer + int(num)
    return answer