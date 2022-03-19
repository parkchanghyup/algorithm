from itertools import combinations
from collections import Counter


def solution(orders, course):

    answer = []
    for C in course:
        order_list = []
        for order in orders:
            order = sorted(order)
            order_list.extend(list(combinations(order, C)))
        counter = Counter(order_list)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f]
                       == max(counter.values())]

    return sorted(answer)
