n = input()

target = int(n)
cnt = 1
while True:
    
    # 한자리수 0을 붙여준다
    if len(n) ==1 :
        n = '0'+n
    
    # 더하기 사이클 식 
    # eval () 함수는 '1+1' 과 같은 문자열을 계산해준다.
    # eval(1+1) -> 2
    # 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이는작업
    n = n[1]+str(eval(n[0]+ '+'+ n[1]))[-1]
    
    # 종료부
    if int(n)== target :
        break
    cnt +=1
print(cnt)