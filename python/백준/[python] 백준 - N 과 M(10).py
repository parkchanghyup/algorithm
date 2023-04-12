def permutate( idx,Number,M):
    if Number==[]:
        pass
    elif len(Number) == M :
        result.append(Number)
        return

    for i in range(idx,N):
        if visited[i] == 0:
            visited[i] = 1
            permutate(i+1, Number+[numbers[i]], M)
            visited[i] = 0

N, M = list(map(int,input().split()))

result = []
visited = [0] * (N)
numbers = list(map(int,input().split()))
numbers.sort()
permutate(0,[],M)

temp_= []
for temp in result:
    temp_.append(tuple(temp))

result = sorted(list(set(temp_)))

for num in result:
    for n in num:
        print(n,end=' ')
    print('')