'''
파스칼의 삼각형에 맞게 점화식을 세워 주면된다.
각행의 맨처음과 마지막은 1로 채우고
중간 부분은 dp[i][j] = dp[i-1][j-1] + dp[i-1][j] 로 채워주면된다.
'''

n, k = map(int, input().split())
dp = [[0] * 1 for i in range(1002)]
dp[1].append(1)
for i in range(2, 1002):
    for j in range(1, i + 1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
        
print(dp[n + 1][k + 1] % 10007)