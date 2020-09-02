#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 소수 찾기 
from itertools import permutations
import math
def prime(num):
    if num in [0,1]: return False
    pos = True
    for i in range(2,int(math.sqrt(num))):
        if num%2 == 0:
            pos =False
            break
            
    return pos
def solution(numbers):
    prime = set()
    number = list(numbers)
    numbers=[]
    
    for n in range(1,len(number)+1):
        
        numbers.extend( list(permutations(number,n)))
    for i in range(len(numbers)):
        num =''
        for j in range(len(numbers[i])):
            num +=numbers[i][j]
        prime.add(int(num))
    answer = 0
    
    
    for num in prime:
        if num in[2,3]: answer +=1
        if num>=4:
            sqrt_n=int(math.sqrt(num))
            pos =True
            for d in range(2,sqrt_n+1):
                
                if num % d == 0:
                    pos=False
                    break
            if pos==True:
                
                answer+=1
    
        
    return answer

