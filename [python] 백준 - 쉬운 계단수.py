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
    
