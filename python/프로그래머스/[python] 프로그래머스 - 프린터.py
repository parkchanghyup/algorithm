#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#프린터
def solution(priorities, location):

    value = [] + priorities
    idx = [c for c in range(len(priorities))]

    i = 0
    while 1:
        #뒤에 문서중요도가 나보다 높은것이 있으면
        if value[i] < max(value[i + 1:]):
            value.append(value.pop(i))
            idx.append(idx.pop(i))
        else:
            i += 1

        if value == sorted(value, reverse=True):
            break
    return idx.index(location) + 1

