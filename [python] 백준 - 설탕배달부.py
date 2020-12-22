# 설탕배달부
n = int(input())
sugar = [int(1e9)]*(n+1)

# 5먼저
for i in range(3,n+1):
    if i % 5 ==0:
        sugar[i] = i//5
sugar[3] = 1  
for i in range(3, n+1):
    if sugar[i]==int(1e9):
        if sugar[i-3] !=int(1e9) :
            sugar[i] = sugar[i-3]+1
        else :
            if sugar[i-3] != int(1e9):
                sugar[i] = min(sugar[i],sugar[i-3])+1

                

if sugar[n] == int(1e9) :
    print(-1)
else :
    print(sugar[n])
