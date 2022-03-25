from collections import deque
import sys
H, W = map(int, sys.stdin.readline().split(" "))

arr = []

for i in range(H):
    
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append(temp)


dx = [0,0,1,-1]
dy = [1,-1,0,0]

cheese = 0
for i in range(H):
    for j in range(W):
        if arr[i][j] == 1:
            cheese += 1


def bfs():
    count = 0
    while q:
        y,x = q.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny =y +dy[i]
            if 0<=nx<W and 0<=ny <H and visited[ny][nx] == 0:
                visited[ny][nx] = 1

                if arr[ny][nx] == 1:
                    arr[ny][nx] = 2
                    count +=1
                else :
                    q.append([ny,nx])


    return count


def delete():
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 2:
                arr[i][j] = 0

q= deque()

answer = 0
temp = 0
while True :
    visited = [[0 for _ in range(W)] for _ in range(H)]
    q.append([0,0])
    visited[0][0] = 1
    count = bfs()
    if count == 0 :
        break
    
    temp = count    
    answer +=1

    delete()

print(answer)
print(temp)