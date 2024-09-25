import sys
from typing import List, Tuple

# 방향 상수 (상, 하, 좌, 우)
DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

# 대각선 방향 상수
DIAGONAL_DX = [1, -1, 1, -1]
DIAGONAL_DY = [1, 1, -1, -1]


def is_valid(x: int, y: int, n: int) -> bool:
    """주어진 좌표가 유효한지 확인합니다."""
    return 0 <= x < n and 0 <= y < n


def read_input() -> Tuple[int, int, int, int, List[List[int]]]:
    """입력을 읽어 시뮬레이션 매개변수와 초기 배열을 반환합니다."""
    n, m, k, c = map(int, sys.stdin.readline().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    return n, m, k, c, arr


def grow_tree(arr: List[List[int]]) -> List[List[int]]:
    """나무를 성장시킵니다."""
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= 0:
                continue
            grow_cnt = 0
            for d in range(4):
                ny = i + DY[d]
                nx = j + DX[d]
                if is_valid(nx, ny, n) and arr[ny][nx] > 0:
                    grow_cnt += 1
            arr[i][j] += grow_cnt
    return arr


def reproduce_tree(arr: List[List[int]]) -> List[List[int]]:
    """나무를 번식시킵니다."""
    n = len(arr)
    visited = [[0] * n for _ in range(n)]

    # 나무가 성장할 수 있는 칸 미리 계산
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                visited[i][j] = 1

    for i in range(n):
        for j in range(n):
            if arr[i][j] < 0 or visited[i][j] == 1:
                continue
            reproduce_list = []
            for d in range(4):
                ny = i + DY[d]
                nx = j + DX[d]
                if is_valid(nx, ny, n) and visited[ny][nx] == 1:
                    reproduce_list.append((ny, nx))

            if reproduce_list:
                reproduce_num = arr[i][j] // len(reproduce_list)
                for y, x in reproduce_list:
                    arr[y][x] += reproduce_num
    return arr


def check_remove_tree(arr: List[List[int]], y: int, x: int, k: int) -> int:
    """제거될 나무의 수를 계산합니다."""
    remove_tree_num = arr[y][x]
    n = len(arr)

    for d in range(4):
        for mul in range(1, k + 1):
            nx = x + DIAGONAL_DX[d] * mul
            ny = y + DIAGONAL_DY[d] * mul
            if not is_valid(nx, ny, n) or arr[ny][nx] <= 0:
                break
            remove_tree_num += arr[ny][nx]
    return remove_tree_num


def exterminate_tree(arr: List[List[int]], k: int, c: int) -> Tuple[List[List[int]], int]:
    """나무를 제거하고 제초제를 뿌립니다."""
    n = len(arr)
    max_remove_tree = 0
    max_remove_tree_y, max_remove_tree_x = -1, -1

    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                remove_tree_num = check_remove_tree(arr, i, j, k)
                if max_remove_tree < remove_tree_num:
                    max_remove_tree = remove_tree_num
                    max_remove_tree_y, max_remove_tree_x = i, j

    # 제초제 뿌리기
    arr[max_remove_tree_y][max_remove_tree_x] = -c
    for d in range(4):
        for mul in range(1, k + 1):
            nx = max_remove_tree_x + DIAGONAL_DX[d] * mul
            ny = max_remove_tree_y + DIAGONAL_DY[d] * mul
            if not is_valid(nx, ny, n):
                break
            if arr[ny][nx] <= 0:
                if arr[ny][nx] > -c:
                    arr[ny][nx] = -c
                break
            arr[ny][nx] = -c

    return arr, max_remove_tree


def remove_poison(arr: List[List[int]]) -> List[List[int]]:
    """제초제 효과를 감소시킵니다."""
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] < 0:
                arr[i][j] += 1
    return arr


def main():
    """메인 함수: 시뮬레이션을 실행합니다."""
    n, m, k, c, arr = read_input()
    result = 0
    c += 1

    # 벽을 -99999로 설정
    for i in range(n):
        for j in range(n):
            if arr[i][j] == -1:
                arr[i][j] = -99999

    for _ in range(m):
        arr = grow_tree(arr)
        arr = reproduce_tree(arr)
        arr, remove_tree = exterminate_tree(arr, k, c)
        result += remove_tree
        arr = remove_poison(arr)

    print(result)


if __name__ == "__main__":
    main()