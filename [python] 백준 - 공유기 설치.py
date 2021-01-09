import bisect


N,C = map(int,input().split())
house = []
for i in range(N):
    house.append(int(input()))

    
# 집좌표 정렬
house.sort()

low = 1 
high = house[-1] - house[C-2]

[1,2,4,8,9]
while low <= high:
    
    mid =  (low+high)// 2
    # 첫번째 집에 설치
    install = house[0]
    count = 1
    
    for i in range(1,N):
        if house[i] >= install+mid :
            count +=1
            install = house[i]
    
    if count >= C:
        low = mid +1 
        answer = mid
    else:
        high = mid -1
print(answer)
    
    