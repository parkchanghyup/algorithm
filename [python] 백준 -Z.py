# 3 7 7
N,r,c = list(map(int,input().split()))
result = 0
while N>=1 :
    temp = 2**(N-1) - 1
    
    # 2사분면
    if r <= temp and c<= temp :
        
        N-=1
        continue
    # 1 사분면
    elif c > temp and r<=temp :
        
        c = c- temp-1
        result += (temp+1)*(temp+1)
    # 3 사분면 
    elif r> temp and c<= temp:
        
        r =r-temp-1
        result += (temp+1)*(temp+1) * 2
    # 4사분면 
    else :
        
        c = c- temp-1
        r = r- temp -1 
        result += (temp+1)*(temp+1) * 3
    N-=1
    
print(result)
        
    
    




    