N   = int(input())

for i in range(N):
    s = input()

    result  = 0
    score = 1
    for char in s:
        if char == 'X':
            score = 1
        else :
            result +=score
            score+=1

    print(result)
    

