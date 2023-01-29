def solution(x, y, n):
    answer = 0
    dp = [int(1e9)] * (y + 1)
    dp[x] = 0

    for i in range(x + 1, y + 1):

        num_2, num_3, num_add = int(1e9), int(1e9), int(1e9)

        # i가 2로 나눠 질때만
        if i % 2 == 0:
            num_2 = dp[i // 2]

        # i가 3으로 나눠 질 때만
        if i % 3 == 0:
            num_3 = dp[i // 3]

        # i - n 이 0보다 클때만
        if i - n > 0:
            num_add = dp[i - n]

        min_num = min(num_2, min(num_3, num_add))

        dp[i] = min_num + 1

    if dp[y] > int(1e9):
        return -1
    else:
        return dp[y]
