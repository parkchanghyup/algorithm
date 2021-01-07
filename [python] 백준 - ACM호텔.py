# 먼저 1층부터 H층까지 각 층의 1호에 손님을 배치
# 101 -> 201 -> 301 ->...-> h01 
# 그리고 각 층의 2호에 손님을 배치.. 반복
# zfill()을 이용하여 101 호에서 1 '01' 을 맞춰준다.


n = int(input())

for _ in range(n):
    
    H,W,N = map(int,input().split())
    F = 1
    
    # 각층의 앞쪽부터 손님을 배치
    while N > H:
        N -= H
        F+=1
    
    # zfill()을 이용하여 호실 양식을 맞춰준다.
    print(str(N)+str(F).zfill(2))
        