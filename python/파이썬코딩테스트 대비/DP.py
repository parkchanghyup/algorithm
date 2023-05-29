def fibonacci(n):
    # 기저 조건: n이 0 또는 1인 경우
    if n <= 1:
        return n

    # 다이나믹 프로그래밍을 위한 리스트 초기화
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    # 피보나치 수열 계산
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# 피보나치 수열의 10번째 항을 계산
result = fibonacci(10)
print(result)