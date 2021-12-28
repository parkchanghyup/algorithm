#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(n, computers):
    answer = 0
    visited = []

    def DFS(start):

        stack = [start]
        while stack:
            n = stack.pop()
            if n not in visited:
                visited.append(n)
                for i in range(len(computers[start])):
                    if computers[n][i] == 1 and i not in visited:

                        stack.append(i)

    for i in range(len(computers)):
        if i not in visited:
            DFS(i)

            answer += 1

    return answer

