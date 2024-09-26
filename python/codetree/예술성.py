import sys
from collections import deque
from typing import List, Tuple, Set

# 방향 상수 (우, 하, 좌, 상)
DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

def read_input() -> Tuple[int, List[List[int]]]:
    """입력을 읽어 배열의 크기와 배열을 반환합니다."""
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    return n, arr

def get_group(y: int, x: int, arr: List[List[int]], visited: List[List[bool]]) -> List[Tuple[int, int]]:
    """주어진 위치에서 시작하여 같은 숫자로 이루어진 그룹을 찾습니다."""
    n = len(arr)
    arr_num = arr[y][x]
    group = [(y, x)]
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny, nx = y + DY[d], x + DX[d]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx] == arr_num:
                visited[ny][nx] = True
                group.append((ny, nx))
                queue.append((ny, nx))
    return group

def find_groups(arr: List[List[int]]) -> List[List[Tuple[int, int]]]:
    """배열에서 모든 그룹을 찾습니다."""
    n = len(arr)
    visited = [[False] * n for _ in range(n)]
    groups = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                groups.append(get_group(i, j, arr, visited))
    return groups

def calculate_beautiful(group_1: List[Tuple[int, int]], group_2: List[Tuple[int, int]], arr: List[List[int]]) -> int:
    """두 그룹 간의 아름다움 점수를 계산합니다."""
    n = len(arr)
    group_2_set = set(group_2)
    cnt = 0
    for y, x in group_1:
        for d in range(4):
            ny, nx = y + DY[d], x + DX[d]
            if 0 <= ny < n and 0 <= nx < n and (ny, nx) in group_2_set:
                cnt += 1
    return (len(group_1) + len(group_2)) * arr[group_1[0][0]][group_1[0][1]] * arr[group_2[0][0]][group_2[0][1]] * cnt

def rotate_cross(arr: List[List[int]]) -> List[List[int]]:
    """배열의 십자가 부분을 반시계 방향으로 90도 회전합니다."""
    n = len(arr)
    new_arr = []
    for row in arr:
        new_arr.append(row[:])
    mid = n // 2
    for i in range(n):
        new_arr[mid][i] = arr[i][mid]
        new_arr[i][mid] = arr[mid][n-1-i]
    return new_arr

def rotate_square(arr: List[List[int]], sy: int, sx: int) -> None:
    """배열의 특정 정사각형 영역을 시계 방향으로 90도 회전합니다."""
    n = len(arr) // 2
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = arr[sy+i][sx+j]
    for i in range(n):
        for j in range(n):
            arr[sy+j][sx+n-1-i] = temp[i][j]

def rotate_all(arr: List[List[int]]) -> None:
    """전체 배열을 회전합니다: 십자가 부분은 반시계 방향, 나머지 정사각형은 시계 방향으로 회전합니다."""
    n = len(arr)
    rotated_cross = rotate_cross(arr)
    rotate_square(arr, 0, 0)
    rotate_square(arr, 0, n//2 + 1)
    rotate_square(arr, n//2 + 1, 0)
    rotate_square(arr, n//2 + 1, n//2 + 1)
    mid = n // 2
    for i in range(n):
        arr[i][mid] = rotated_cross[i][mid]
        arr[mid][i] = rotated_cross[mid][i]

def main():
    """메인 함수: 시뮬레이션을 실행하고 결과를 출력합니다."""
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
