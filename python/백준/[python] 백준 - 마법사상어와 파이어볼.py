N,M,K = list(map(int,input().split()))

fire = []
for _ in range(M):
    fire.append(list(map(int,input().split())))

graph = [[[] for _ in range(N)] for _ in range(N)]

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

new_fire = []
for (r, c, m, s, d) in fire:
    r -= 1
    c -= 1
    graph[r][c].append([m,s,d])
    new_fire.append([r,c,m,s,d])

while K>0:

    graph = [[[] for _ in range(N)] for _ in range(N)]

    for (r,c,m,s,d) in new_fire:

        for i in range(1,s+1):
            c = c + dx[d]
            r = r + dy[d]

            if c  < 0 :
                c = N-1
            elif c == N:
                c = 0

            if r < 0:
                r = N-1
            elif r== N:
                r = 0

        graph[r][c].append([m,s,d])


    new_fire = []

    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) == 1:

                new_fire.append([i, j] + graph[i][j][0])
            elif len(graph[i][j]) > 1:
                sum_m = 0
                sum_s = 0
                sum_d = []
                for (m, s, d) in graph[i][j]:
                    sum_m += m
                    sum_s += s
                    sum_d.append(d)

                mm = sum_m // 5
                ss = sum_s // len(graph[i][j])
                if mm == 0:
                    continue

                check =[0,0]
                for d in sum_d:
                    check[d%2]+=1
                if check[0] >0 and check[1] >0:
                    dd = [1,3,5,7]
                else :
                    dd = [0,2,4,6]


                for d in dd:
                    new_fire.append([i, j, mm, ss, d])


    K -= 1


result = 0
for (i,j,m,s,d) in new_fire:
    result += m
print(result)

