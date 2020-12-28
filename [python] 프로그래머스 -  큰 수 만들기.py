def solution(number, k):
    answer = ''
    candidate = [] 
    for i,num in enumerate(number):
        while candidate and candidate[-1] < num and k> 0:
            candidate.pop()
            k-=1
              
        candidate.append(num)
    if k > 0 :
        candidate = candidate[:-k]
    return ''.join(candidate)
        