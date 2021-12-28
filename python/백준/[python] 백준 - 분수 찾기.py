'''
대각선으로 홀수(n) 번째 줄의 경우 숫자가  3/1 -> 2/2 ->  1/3 
이런식으로 분자가 n부터 시작해서 1로 작아지고 분모는 1부터 시작해서 n으로 커진다.

대각선으로 짝수(n) 번째 줄의 경우 숫자가 1/4 -> 2/3 -> 3/2 -> 4/1 
이런식으로 분자가 1에서 n으로 커지고 분모는 n에서 1로 작아진다.

'''


n = int(input())
i = 1
total = 1

while total < n:
    i +=1
    total +=i

# 짝수번째 줄 : 분자 오름차순 ,분모 내림차순
if i % 2== 0:
    cnt = total - n
    up,down = i,1
    while cnt >0:
        cnt -=1
        up -=1
        down +=1

# 홀수번쨰 줄 :분모 오름차순 ,분자 내림차순
else :
    cnt = total - n 
    up,down = 1,i
    while cnt > 0:
        cnt-=1
        up +=1
        down -=1
        
print(str(up)+'/'+str(down))
