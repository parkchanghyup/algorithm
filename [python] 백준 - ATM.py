n = int(input())
times = list(map(int,input().split()))

times.sort()

result  = 0
for idx,time in enumerate(times):
    result = result + sum(times[:idx]) + time
    
print (result)