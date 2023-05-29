def greedy_coin_change(amount, coins):
    coins.sort(reverse=True)  # 동전들을 큰 순서로 정렬
    change = []  # 거스름돈으로 사용할 동전들을 저장하는 리스트

    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)

    return change

# 거스름돈으로 사용할 동전들과 거스름돈의 금액
coins = [500, 100, 50, 10]
amount = 1260

# 그리디 알고리즘 호출
change = greedy_coin_change(amount, coins)

print("거스름돈으로 줄 동전들:", change)
print("동전의 개수:", len(change))