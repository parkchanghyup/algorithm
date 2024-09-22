import sys
from collections import deque
from typing import List, Tuple

def read_input() -> Tuple[int, List[List[int]]]:
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    return n, arr

def get_group(y: int, x: int, arr: List[List[int]], visited: List[List[bool]]) -> List[Tuple[int, int]]:
    n = len(arr)
    arr_num = arr[y][x]
    group = [(y, x)]
    queue = deque([(y, x)])
    visited[y][x] = True

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx] == arr_num:
                visited[ny][nx] = True
                group.append((ny, nx))
                queue.append((ny, nx))

    return group

def find_groups(arr: List[List[int]]) -> List[List[Tuple[int, int]]]:
    n = len(arr)
    visited = [[False] * n for _ in range(n)]
    return [get_group(i, j, arr, visited) for i in range(n) for j in range(n) if not visited[i][j]]

def calculate_beautiful(group_1: List[Tuple[int, int]], group_2: List[Tuple[int, int]], arr: List[List[int]]) -> int:
    n = len(arr)
    group_2_set = set(group_2)
    cnt = sum(1 for y, x in group_1 for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]
              if 0 <= y + dy < n and 0 <= x + dx < n and (y + dy, x + dx) in group_2_set)
    return (len(group_1) + len(group_2)) * arr[group_1[0][0]][group_1[0][1]] * arr[group_2[0][0]][group_2[0][1]] * cnt

def rotate_cross(arr: List[List[int]]) -> List[List[int]]:
    """배열의 십자가 부분을 반시계 방향으로 90도 회전"""
    n = len(arr)
    new_arr = [row[:] for row in arr]  # 새로운 배열 생성
    mid = n // 2

    # 가로 줄 회전
    for i in range(n):
        new_arr[mid][i] = arr[i][mid]

    # 세로 줄 회전
    for i in range(n):
        new_arr[i][mid] = arr[mid][n-1-i]

    return new_arr

def rotate_square(arr: List[List[int]], sy: int, sx: int) -> None:
    """배열의 특정 정사각형 영역을 시계 방향으로 90도 회전"""
    n = len(arr) // 2
    temp = [[0] * n for _ in range(n)]

    # 임시 배열로 복사
    for i in range(n):
        for j in range(n):
            temp[i][j] = arr[sy+i][sx+j]

    # 시계 방향으로 90도 회전하여 원래 배열에 저장
    for i in range(n):
        for j in range(n):
            arr[sy+j][sx+n-1-i] = temp[i][j]

def rotate_all(arr: List[List[int]]) -> None:
    """전체 배열 회전: 십자가 부분 반시계 방향, 나머지 정사각형 시계 방향"""
    n = len(arr)
    # 십자가 부분 회전
    rotated_cross = rotate_cross(arr)

    # 4개의 정사각형 영역 회전
    rotate_square(arr, 0, 0)  # 좌상단
    rotate_square(arr, 0, n//2 + 1)  # 우상단
    rotate_square(arr, n//2 + 1, 0)  # 좌하단
    rotate_square(arr, n//2 + 1, n//2 + 1)  # 우하단

    # 회전된 십자가 부분을 원래 배열에 적용
    mid = n // 2
    for i in range(n):
        arr[i][mid] = rotated_cross[i][mid]
        arr[mid][i] = rotated_cross[mid][i]

def main():
    n, arr = read_input()
    answer = 0

    for _ in range(4):
        group_list = find_groups(arr)
        for i in range(len(group_list)):
            for j in range(i + 1, len(group_list)):
                answer += calculate_beautiful(group_list[i], group_list[j], arr)
        rotate_all(arr)

    print(answer)

if __name__ == "__main__":
    main()
