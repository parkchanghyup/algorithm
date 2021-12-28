#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(numbers, hand):
    left = [3, 0]
    right = [3, 2]
    answer = ''
    for num in numbers:
        if num == 0:
            num = 11

        if num == 3 or num == 6 or num == 9:
            answer += 'R'
            right = [int(num / 3 - 1), 2]

        elif num == 1 or num == 4 or num == 7:
            answer += 'L'
            left = [int(num / 3), num % 3 - 1]

        else:
            right_dist = abs(right[0] - int(num / 3)) + abs(right[1] -
                                                            int(num % 3 - 1))
            left_dist = abs(left[0] - int(num / 3)) + abs(left[1] -
                                                          int(num % 3 - 1))

            if right_dist > left_dist:
                answer += 'L'
                left = [int(num / 3), num % 3 - 1]
            elif left_dist > right_dist:
                answer += 'R'
                right = [int(num / 3), num % 3 - 1]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = [int(num / 3), num % 3 - 1]
                else:
                    answer += 'L'
                    left = [int(num / 3), num % 3 - 1]

    return answer

