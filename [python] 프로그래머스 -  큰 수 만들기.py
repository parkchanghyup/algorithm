'''
앞에 있는 숫자들을 candidate 리스트에 하나씩 넣는다.
k> 0 일 때 현재 num 보다 작은숫자가 candidate에 들어있다면 하나씩 빼준다. 
(숫자의 크기는 앞자리가 가장 중요하기 때문이다.)
'''


def solution(number, k):
    answer = ''
    candidate = [] 
    
    for i,num in enumerate(number):
        # candidate가 비어있지 않고, candidate에 num보다 작은 숫자가 있다면 pop
        while candidate and candidate[-1] < num and k> 0:
            candidate.pop()
            k-=1
              
        candidate.append(num)
    # k가 0이상인경우 뒤에 서부터 짜른다. 
    if k > 0 :
        candidate = candidate[:-k]
    return ''.join(candidate)
        