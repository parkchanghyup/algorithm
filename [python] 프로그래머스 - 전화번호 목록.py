#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        st1 = phone_book[i]
        for j in range(len(phone_book)):
            st2 = phone_book[j]
            if i==j :  #같은 인덱스면 생략
                continue
                #길이가 더 길면 생략
            if len(st1)>len(st2):
                   continue
            if st1 in st2[:len(st1)]:
                return False
    return True
cs

