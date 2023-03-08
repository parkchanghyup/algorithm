def solution(nums):
    number = len(nums) // 2

    pon = len(set(nums))

    return number if number < pon else pon

    return answer