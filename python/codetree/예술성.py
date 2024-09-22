import sys
from collections import deque
from typing import List, Tuple

def read_input() -> Tuple[int, List[List[int]]]:
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    return n, arr

def get_group(y: int, x: int, arr: List[List[int]], visited: List[List[int]]) -> List[Tuple[int, int]]:
    """
    (y,x)를 포함하는 group return
    """
    n = len(arr)
    arr_num = arr[y][x]
    group = []
    queue = deque([(y, x)])
    visited[y][x] = 1
    group.append((y, x))

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx] == arr_num:
                visited[ny][nx] = 1
                group.append((ny, nx))
                queue.append((ny, nx))

    return group

def find_groups(arr: List[List[int]]) -> List[List[Tuple[int, int]]]:
    n = len(arr)
    visited = [[0] * n for _ in range(n)]
    group_list = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_temp = get_group(i, j, arr, visited)
                group_list.append(group_temp)

    return group_list


def calculate_beautiful(group_1: List[Tuple[int, int]], group_2: List[Tuple[int, int]], arr: List[List[int]]) -> int:
    """
    group_1, group_2의 조화로움 계산
    """
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    n = len(arr)

    # 맞닿아 있는 면 갯수
    cnt = 0
    group_2_set = set(group_2)  # 검색 속도 향상을 위해 set으로 변환

    for y, x in group_1:
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < n:
                if (ny, nx) in group_2_set:
                    cnt += 1

    return (len(group_1) + len(group_2)) * arr[group_1[0][0]][group_1[0][1]] * arr[group_2[0][0]][group_2[0][1]] * cnt


def rotate_center(arr):
    """
    배열의 가운데 십자가 부분 왼쪽으로 90도 회전
    """
    pass


def rotate_square(arr, y, x):
    """
    배열을 오른쪽으로 90도 회전
    """


def main():
    n, arr = read_input()

    # 최종 출력 값
    answer = 0
    for _ in range(4):
        group_list = find_groups(arr)

        # # find_groups test
        # test_arr = [[0] * n for _ in range(n)]
        # for num, group in enumerate(group_list, 1):
        #     for y, x in group:
        #         test_arr[y][x] = num
        #
        #
        # for row in test_arr:
        #     print(row)
        # break

        for i in range(len(group_list)):
            for j in range(i+1, len(group_list)):
                beatiful_score = calculate_beautiful(group_list[i], group_list[j], arr)
                answer += beatiful_score
                print(beatiful_score)
        break
        center_arr = rotate_center(arr)

        # 각 영역별로 회전
        square_arr = rotate_center(arr, 0, 0)
        square_arr = rotate_center(square_arr, 0, n//2+1)
        square_arr = rotate_center(square_arr, n//2+1, 0)
        square_arr = rotate_center(square_arr, n//2+1, n//2+1)

        for i in range(n):
            for j in range(n):
                if i == n//2 or j == n//2:
                    arr[i][j] = center_arr[i][j]
                else :
                    arr[i][j] = square_arr[i][j]

        print(answer)


if __name__ == "__main__":
    main()