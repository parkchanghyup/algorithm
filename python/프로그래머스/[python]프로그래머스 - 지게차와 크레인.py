from collections import deque


def build_boundary(storage):
    """외곽 경계를 추가한 새로운 storage 배열 생성"""
    rows = len(storage)
    cols = len(storage[0])
    # 0으로 채워진 경계 포함 배열 생성
    temp = [[0] * (cols + 2) for _ in range(rows + 2)]
    
    for i in range(rows):
        for j in range(cols):
            temp[i + 1][j + 1] = storage[i][j]
    
    return temp


def check_boundary(storage, request):
    """BFS를 사용한 경계 연결 영역 체크"""
    count = 0
    queue = deque([(0, 0)])
    visited = [[0] * len(storage[0]) for _ in range(len(storage))]
    visited[0][0] = 1
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        current_y, current_x = queue.popleft()
        
        for dy, dx in directions:
            next_y = current_y + dy
            next_x = current_x + dx
            
            if storage[next_y][next_x] == 0:
                if not visited[next_y][next_x]:
                    queue.append((next_y, next_x))
                    visited[next_y][next_x] = 1
            elif storage[next_y][next_x] == request:
                storage[next_y][next_x] = 0
                visited[next_y][next_x] = 1
                count += 1
    
    return count, storage


def check_all(storage, request):
    """전체 storage에서 특정 값 제거"""
    rows = len(storage)
    cols = len(storage[0])
    count = 0

    for y in range(rows):
        for x in range(cols):
            if storage[y][x] == request:
                storage[y][x] = 0
                count += 1
    return count, storage


def solution(storage, requests):
    """주어진 요청에 따라 storage 처리 후 남은 영역 계산"""
    total_area = len(storage) * len(storage[0])
    storage_with_boundary = build_boundary(storage)
    
    for request in requests:
        if len(request) == 1:
            removed_count, storage_with_boundary = check_boundary(storage_with_boundary, request)
        else:
            removed_count, storage_with_boundary = check_all(storage_with_boundary, request[0])
        total_area -= removed_count
        
        # 디버깅용 출력 (필요시 활성화)
        # for row in storage_with_boundary:
        #     print(row)
        # print('---' * 10)
    
    return total_area
