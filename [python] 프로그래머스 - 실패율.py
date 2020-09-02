#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(N, stages):
    answer = []
    dic = {}
    for i in range(1, N + 1):
        total = 0
        fail = 0
        for j in stages:
            if j >= i: total += 1
            if j > i: fail += 1
        fail = total - fail
        print(i, fail, total)
        if total == 0: dic[i] = [0]
        else:
            dic[i] = [fail / total]

    dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    answer = list(dic.keys())

    return answer

