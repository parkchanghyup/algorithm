'''
'''
n = int(input())
i = 1
total = 1
while total < n:
    i +=1
    total +=i

# 짝수번째 줄 (내림차순)
if i % 2== 0:
    cnt = total - n
    up,down = i,1
    while cnt >0:
        cnt -=1
        up -=1
        down +=1

# 홀수번쨰 줄 (오름차순)
else :
    cnt = total - n 
    up,down = 1,i
    while cnt > 0:
        cnt-=1
        up +=1
        down -=1
        
print(str(up)+'/'+str(down))
