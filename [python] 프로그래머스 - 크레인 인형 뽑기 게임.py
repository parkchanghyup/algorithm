#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(board, moves):
    result = []
    answer = 0
    for num in moves:
        num -= 1
        for i in range(len(board)):
            if board[i][num] != 0:
                result.append(board[i][num])
                board[i][num] = 0
                break
    while (1):
        pos = True
        for idx in range(len(result) - 1):
            if result[idx] == result[idx + 1]:
                result.pop(idx + 1)
                result.pop(idx)
                answer += 2
                pos = False
                break

        if pos:
            break

    return answer

