def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# 예시 배열과 타겟 값
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12

# 이분 탐색 호출
result = binary_search(arr, target)

if result != -1:
    print("타겟 값이 배열의 인덱스", result, "에 위치합니다.")
else:
    print("타겟 값이 배열에 존재하지 않습니다.")