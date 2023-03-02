from collections import Counter


def solution(topping):
    answer = 0
    topping_counter = Counter(topping)
    temp = set()

    for top in topping:
        topping_counter[top] -= 1
        temp.add(top)
        if topping_counter[top] == 0:
            topping_counter.pop(top)
        if len(topping_counter) == len(temp):
            answer += 1

    return answer