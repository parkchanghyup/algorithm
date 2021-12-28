# 설탕배달
'''
sugar 리스트를 만들어 dp로 문제해결.
먼저 5킬로그램 봉지를 사용할 수 있는 경우의 수를 계산하고 (1)
dp [i] = dp[i-3] +1 의 점화식을 사용하여 문제해결 (2)
'''
n = int(input())
sugar = [int(1e9)]*(n+1)

# 5킬로그램 봉지 먼저 사용하는 경우의 수 계산
for i in range(3,n+1):
    if i % 5 ==0:
        sugar[i] = i//5
        
        
sugar[3] = 1  

# 점화식을 사용하여 문제 해결
for i in range(3, n+1):
    
    if sugar[i]==int(1e9):
        
        if sugar[i-3] != int(1e9) :
            sugar[i] = sugar[i-3]+1
            
        else :
            if sugar[i-3] != int(1e9):
                sugar[i] = min(sugar[i],sugar[i-3])+1

                
# 불가능한 경우
if sugar[n] == int(1e9) :
    print(-1)
    
else :
    print(sugar[n])
