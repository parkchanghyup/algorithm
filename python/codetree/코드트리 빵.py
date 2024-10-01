from collections import deque
from typing import List, Tuple, Dict
import heapq

# 상, 좌, 우, 하 방향으로의 이동을 나타내는 상수
DX = [0, -1, 1, 0]
DY = [-1, 0, 0, 1]


def read_input() -> Tuple[int, int, List[List[int]], Dict[int, Tuple[int, int]]]:
    """
    사용자 입력을 읽어 게임 초기 상태를 설정합니다.
    """
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    convs = {i: tuple(map(lambda x: int(x) - 1, input().split())) for i in range(m)}
    return n, m, arr, convs


def get_base_camps(arr: List[List[int]]) -> List[Tuple[int, int]]:
    """
    격자에서 모든 베이스 캠프의 위치를 찾습니다.
    """
    return [(i, j) for i in range(len(arr)) for j in range(len(arr)) if arr[i][j] == 1]


def move_user(arr: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[int, int]:
    """
    사용자를 시작 위치에서 목표 위치로 이동시킵니다.
    """
    n = len(arr)
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        (y, x), path = queue.popleft()
        if (y, x) == end:
            return path[0] if path else start

        for d in range(4):
            ny, nx = y + DY[d], x + DX[d]
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != -1 and (ny, nx) not in visited:
                visited.add((ny, nx))
                new_path = path + [(ny, nx)] if path else [(ny, nx)]
                queue.append(((ny, nx), new_path))

    return start



def get_first_base_camp(arr, start):
    """
    시작 위치에서 가장 가까운 베이스 캠프를 찾습니다.
    """
    n = len(arr)
    distances = [[float('inf')] * n for _ in range(n)]
    distances[start[0]][start[1]] = 0
    pq = [(0, start)]

    while pq:
        dist, (y, x) = heapq.heappop(pq)

        if distances[y][x] < dist:
            continue

        if arr[y][x] == 1:
            return y, x

        for d in range(4):
            ny, nx = y + DY[d], x + DX[d]
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != -1:
                new_dist = dist + 1
                if new_dist < distances[ny][nx]:
                    distances[ny][nx] = new_dist
                    heapq.heappush(pq, (new_dist, (ny, nx)))

    return -1, -1


def main():
    """
    메인 함수: 게임 로직을 실행합니다.
    """
    n, m, arr, convs = read_input()
    users: List[Tuple[int, int]] = []
    answer = 0
    cnt = 0

    while cnt < m:
        no_access_pos = []

        # 유저 이동
        for idx, user in enumerate(users):
            conv = convs[idx]
            # 이미 도착했으면 continue
            if conv == user:
                continue

            user = move_user(arr, tuple(user), conv)
            users[idx] = user
            if conv == tuple(user):
                cnt += 1
                no_access_pos.append(user)

        # 이동 불가 처리
        for y, x in no_access_pos:
            arr[y][x] = -1

        if len(users) == len(convs):
            answer += 1
            continue

        # 베이스캠프로 이동
        conv = convs[len(users)]
        y, x = get_first_base_camp(arr, conv)
        users.append((y, x))
        arr[y][x] = -1

        # 턴 증가
        answer += 1

    print(answer)


if __name__ == '__main__':
    main()
