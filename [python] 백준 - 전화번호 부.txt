m = int(input())
for _ in range(m):
    n = int(input())
    numbers=[]
    for i in range(n):
        numbers.append(input())
 
 
    numbers.sort()
 
    pos = True
    for i in range(len(numbers)-1):
        num = numbers[i]
        next_num = numbers[i+1]
 
        if num == next_num[:len(num)]:
            pos = False
            break
 
 
    if pos :
        print('YES')
    else :
        print('NO')