from collections import Counter, defaultdict


def solution(id_list, report, k):
    answer = []
    # 중복 값 제거
    reports = list(set(report))
    target = []
    dic = defaultdict(list)

    for report in reports:
        a, b = report.split()
        dic[a].append(b)
        target.append(b)
    counter = Counter(target)

    for id in id_list:
        cnt = 0
        for target in dic[id]:
            if counter[target] >= k:
                cnt += 1
        answer.append(cnt)

    return answer
