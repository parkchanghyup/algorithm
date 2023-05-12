def solution(N, number):
    dp = []

    for i in range(1, 9):
        numbers = set()
        numbers.add(int(i * str(N)))

        for j in range(i - 1):
            for x in dp[j]:
                for y in dp[i - j - 2]:
                    numbers.add(x + y)
                    numbers.add(x * y)
                    numbers.add(x - y)
                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            return i

        dp.append(numbers)

    return -1