'''
divmod 함수를 사용하여 계속해서 n을 3으로나누고  나머지를 three 문자열에 추가해주고
int()함수의 Base를 이용하여 10진법으로변환 해준다.
'''

def solution(n):
    
    three = ''
    
    # 3진법 변환
    while n>2 :
        n,m = divmod(n,3)
        three += str(m)
    
    three += str(n)
    
    # 10진법으로 변환
    return int(three,3)
