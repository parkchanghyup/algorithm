from collections import defaultdict


def solution(gems):

    gem = len(set(gems))

    dic = defaultdict(int)
    left, right = 0, 0
    min_length = len(gems)
    dic[gems[right]] += 1
    while left < len(gems) and right < len(gems):
        # print(dic,left,right)
        if len(dic) < gem:
            right += 1
            if right == len(gems):
                break
            dic[gems[right]] += 1

        else:
            if (right - left) < min_length:
                min_length = right-left
                answer = [left+1, right+1]
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            left += 1

    return answer


solution(["AA", "AB", "AC", "AA", "AC"])
