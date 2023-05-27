def solution(N, number):
    
    dp = []
    
    for i in range(1, 9):
        numbers = set()
        check_number = int(str(N) * i)
        
        numbers.add(check_number)
        
        for j in range(i-1):
            for left in dp[j]:
                for right in dp[-j-1]:
                    numbers.add(left - right)
                    numbers.add(left * right)
                    numbers.add(left + right)
                    if right != 0 :
                        numbers.add(left // right)
        dp.append(numbers)                
        if number in numbers:
            return i
    return -1
