#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# H-Index
def solution(citations):
    answer = 0
    citations = sorted(citations,reverse=True)
    m_num = max(citations)
    
    for i in range(m_num,0,-1):
        cnt =0
        for num in citations:
            if num >= i : cnt+=1

        
        if cnt>= i :
            return i
    
    return 0

