from collections import deque


def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1


def bfs():
    q = deque()
    q.append([start, 0])

    visited = [0] * 10000
    visited[start] = 1

    while q:
        now, cnt = q.popleft()

        if now == end:
            return cnt
        now = str(now)

        for i in range(4):
            for j in range(10):
                temp = int(now[:i]+str(j) + now[i+1:])

                if visited[temp] == 0 and is_prime(temp) and temp > 1000:
                    visited[temp] = 1
                    q.append([temp, cnt + 1])


# 테스트 케이스 횟수
t = int(input())

for _ in range(t):
    # 입력
    start, end = map(int, input().split())

    # start ~ end의 단계 카운트
    result = bfs()
    print(result if result != None else "Impossible")
