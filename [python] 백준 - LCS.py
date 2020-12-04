first = input()
second = input()
first_len = len(first)+1
second_len = len(second) +1

dp = [[0]* first_len for j in range(second_len)]

for i in range(1,second_len):
    for j in range(1,first_len):
        if first[j-1]==second[i-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[i][j])
        