'''

계단수는 인접한 모든 자리수의 차이가 1이 나기때문에 점화식을 다음과 같이 세움
j == 0 일때 -> dp[j] = dp[j+1] 
j = (1~8) -> dp[j] = dp[j-1] + dp[j+1]
j = 9 -> dp[j] = dp[j-1]

그리고 각 연산 수행시 % 연산 도 수행.
'''



# 쉬운 계단수

n = int(input())


dp = [0] * 10
dp_prev = [0]*10
    
for i in range(1,10):
    dp[i] = 1

for i in range(1,n):
    dp_prev = dp.copy()
    for j in range(10):
        if j == 0:
            dp[j] =( dp_prev[j+1])%1000000000
        elif j==9:
            dp[j] = (dp_prev[j-1] )%1000000000
        else:
            dp[j] = (dp_prev[j-1]+ dp_prev[j+1])%1000000000

print(sum(dp)%1000000000)
    
