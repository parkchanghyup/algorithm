#!/usr/bin/env python
# coding: utf-8

# In[19]:


def check(word_1,word_2):
    '''
    단어가 알파벳 하나만 다른지 확인
    '''
    cnt = 0
    for i in range(len(word_1)):
        
        if word_1[i] != word_2[i]:
            cnt +=1

    if cnt == 1:
        return True
    
    return False
          

def dfs(word,target,cnt,words):
    
    if word == target :

        return cnt
    
    result = int(1e9)
    
    for word_2 in words:
        if check(word,word_2):
            words.remove(word_2)
            result = min(result,dfs(word_2,target,cnt+1,words))
            words.append(word_2)
    return result

def solution(begin, target, words):

    
    answer = dfs(begin,target,0,words)
    
    if answer ==int(1e9):
        answer = 0
    
    
    return answer

