#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#튜플

def solution(s):
    
    a  = list(map(int,s[1:-1].replace("{","").replace("}","").split(',')))
    
    dic={} 
    
    for i in range(len(a)):
        if a[i] in dic:
            dic[a[i]] =[dic[a[i]][0]+1]
        else:
            dic[a[i]]=[1]
    
    
    dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

    return list(dic.keys())

