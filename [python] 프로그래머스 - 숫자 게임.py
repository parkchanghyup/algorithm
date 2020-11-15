def binary_search(target, numbers):
    lo, hi = 0, len(numbers)-1
    result = -1
    while lo <= hi:
        mid = (lo+hi)//2

        if numbers[mid] <= target:
            lo = mid + 1
        else:
            result = mid
            hi = mid - 1

    return result


def solution(A, B):
    B.sort()
    answer = 0
    for num in A:

        idx = binary_search(num, B)

        if idx == -1:
            continue

        else:
            B.pop(idx)
            answer += 1

    return answer