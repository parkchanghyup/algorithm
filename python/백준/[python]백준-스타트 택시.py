from collections import deque
import copy

N, M , fuel = list(map(int, input().split()))

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

taxi_pos = list(map(int ,input().split()))

guests = []

for _ in range(M):
    guests.append(list(map(int, input().split())))


dx =[0,0,1,-1]
dy = [1,-1,0,0]

def bfs(start):
    visited = [[-1] * N for _ in range(N)]
    [y, x] = start[0]-1, start[1] -1
    visited[y][x] = 0
    q = deque()
    q.append([y,x])

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < N) and (0<=ny < N) :
                if visited[ny][nx] == -1 and graph[ny][nx] != 1:
                    q.append((ny,nx))
                    visited[ny][nx] = visited[y][x] + 1

    return visited
while fuel > 0 :
    # 현재 위치에서 전체 유저의 위치를 구함
    all_dist = bfs(taxi_pos)
    new_guest = []
    flag =  True
    for idx, guest in enumerate(guests):

        dist = all_dist[guest[0]-1][guest[1]-1]
        if dist < 0 :
            flag = False
            break
        guests[idx].append(dist)

    if flag is False:
        fuel = -1
        break

    # guest = [현재위치, 목적지, 현재위치까지 거리, 현재위치에서 목적지 까지 거리)
    # 현재 위치에서 가장 가까운 사람
    guests.sort(key = lambda x : (x[4],x[0],x[1]),reverse = True)
    if len(guests)==0:
        break
    guest = guests.pop()

    # 거리 추가 한거 없애기
    for temp in guests:
        temp.pop()

    dist = bfs([guest[0],guest[1]])[guest[2]-1][guest[3]-1]

    if dist == -1:
        fuel = -1
        break

    if guest[4] + dist <= fuel:
        fuel = fuel - guest[4] + dist
        taxi_pos = [guest[2],guest[3]]
    else :
        fuel = -1
        break



print(fuel)