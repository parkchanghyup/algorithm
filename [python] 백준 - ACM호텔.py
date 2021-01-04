n = int(input())
for _ in range(n):
    H,W,N = map(int,input().split())
    F = 1
    while N > H:
        N -= H
        F+=1
    
    print(str(N)+str(F).zfill(2))
        