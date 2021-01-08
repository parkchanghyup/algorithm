N,K =map(int, input().split())


dp = [] 

for i in range(K):
    dp.append([])
    
    for j in range(N) :
        if i == 0 :
            dp[i].append(1)
        elif j == 0:
            dp[i].append(i+1)
        else :
            dp[i].append((dp[i][j-1]+dp[i-1][j])%1000000000)
print(dp[-1][-1])   

