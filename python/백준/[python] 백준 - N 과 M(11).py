def permutate(idx, Number,M):
    if Number==[]:
        pass
    elif len(Number) == M :
        result.append(Number)
        return

    for i in range(idx,N):
        permutate(i, Number+[numbers[i]], M)

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