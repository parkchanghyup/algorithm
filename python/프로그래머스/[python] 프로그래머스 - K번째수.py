#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# k번째 수
def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        test = array[commands[idx][0]-1:commands[idx][1]]
        test= sorted(test)
        
        answer.append(test[commands[idx][2]-1])
    return answer

