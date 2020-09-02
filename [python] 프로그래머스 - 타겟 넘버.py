#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 타겟 넘버
   
def solution(numbers, target):
    
    answer = 0    
    def func(idx,num):
        if idx == len(numbers):
            if num == target:
                nonlocal answer
                answer+=1
            return 0
        func(idx+1,num+numbers[idx])
        func(idx+1,num-numbers[idx])
    func(0,0)
    return answer

