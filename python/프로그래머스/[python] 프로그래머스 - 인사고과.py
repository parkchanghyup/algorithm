def solution(scores):

    
    target = scores[0]
    target_score = sum(target)
    # 첫번재 점수가 큰 순으로 정렬하고 두번째 점수는 작은 순으로 정렬
    scores = sorted(scores, key = (lambda x : (-x[0],x[1])))
    answer = 1
    max_second = 0 

    for idx, score in enumerate(scores):
        # 원호가 인센티브를 못받는 경우 
        if score[0] > target[0] and score[1] > target[1]:
            return -1
        # 인센티브를 받을 수 있는 경우
        if score[1] >= max_second:
            # 원호보다 점수가 높은 경우
            if sum(score) > target_score:
                answer += 1
                max_second = score[1]
    return answer