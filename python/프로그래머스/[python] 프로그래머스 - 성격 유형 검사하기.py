def solution(survey, choices):
    answer = ''
    answer_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for s, c in zip(survey, choices):
        c = c - 4
        if c < 0:
            answer_dict[s[0]] += abs(c)
        else:
            answer_dict[s[1]] += abs(c)

    choices_list = ['RT', 'CF', 'JM', 'AN']

    for s in choices_list:

        if answer_dict[s[0]] >= answer_dict[s[1]]:
            answer += s[0]
        else:
            answer += s[1]

    return answer


solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])