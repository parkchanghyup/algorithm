def permutate(Number,M):
    if Number==[]:
        pass
    elif len(Number) == M :
        result.append(Number)
        return

    for i in range(N):
        # if visited[i] == 0:
            # visited[i] = 1
        permutate(Number+[numbers[i]], M)
            # visited[i] = 0

N, M = list(map(int,input().split()))

result = []
visited = [0] * (N)
numbers = list(map(int,input().split()))
numbers.sort()
permutate([],M)

for num in result:
    for n in num:
        print(n,end=' ')
    print('')