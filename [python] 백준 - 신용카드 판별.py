def func(card):
    even = 0
    odd = 0
    # 짝수
    for i in range(0, len(card), 2):
        num = int(card[i]) * 2

        # 두자릿수
        if num >= 10:
            num = int(str(num)[0]) + int(str(num)[1])

        even += num

    for i in range(1, len(card), 2):
        num = int(card[i])
        odd += num


    # 짝수 자리의 숫자 합이 두자릿수

    result = (even + odd) % 10

    if result == 0:
        return True
    else:
        return False

n = int(input())

for i in range(n):
    card = input()
    
    if func(card):
        print('T')
    else :
        print('F')