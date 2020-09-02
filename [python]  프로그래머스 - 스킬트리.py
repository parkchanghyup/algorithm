#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:

        trees = [s for s in tree if s in skill]
        pos = True

        for x, y in zip(trees, skill):

            if x != y:
                pos = False
                break
        if pos == True:
            answer += 1

    return answer

