#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 수식 최대화
def minus(giho,numbers):
    numbers = list(map(int,numbers))
    cnt = giho.count('-')
    for i in range(cnt):
        for c in giho:        
            if c =='-':
                idx = giho.index('-')
                giho.pop(idx)
                numbers[idx] = numbers[idx]-numbers[idx+1]
                numbers.pop(idx+1)
                break
        
    return [giho,numbers]

def plus(giho,numbers):
    numbers = list(map(int,numbers))
    cnt = giho.count('+')
    for i in range(cnt):
        for c in giho:        
            if c =='+':
                idx = giho.index('+')
                giho.pop(idx)
                numbers[idx] = numbers[idx]+numbers[idx+1]
                numbers.pop(idx+1)
                break
        
    return [giho,numbers]
def mult(giho,numbers):
    
    numbers = list(map(int,numbers))

    cnt = giho.count('*')
    for i in range(cnt):
        for c in giho:        
            if c =='*':
                idx = giho.index('*')
                giho.pop(idx)
                numbers[idx] = numbers[idx]*numbers[idx+1]
                numbers.pop(idx+1)
                break
        
    return [giho,numbers]

def solution(expression):
    numbers = []
    giho = []
    cut = 0
    expression=list(expression)
    for idx in range(len(expression)):
        
        if expression[idx] in ['*','+','-'] :
            numbers.append(expression[cut:idx])
            giho.append(expression[idx])
            cut=idx+1
            for i in range(idx+1):
                expression[i]='.'
    
    while(1):
        try:
            expression.remove('.')
        except:
            break
        

    numbers.append(expression)
        
    rgiho=[]+giho
    rnumbers=[]
    for i in range(len(numbers)):
        num=''
        for j in range(len(numbers[i])):
            num+=numbers[i][j]
        rnumbers.append(int(num))
    max = 0   
    
    giho =[]+rgiho
    numbers=[]+rnumbers
    test = mult(giho,numbers)
    test = plus(test[0],test[1])
    test = minus(test[0],test[1])
    if max < abs(test[1][0]) : max = abs(test[1][0])
    
    
    giho =[]+rgiho
    numbers=[]+rnumbers
    test = mult(giho,numbers)
    test = minus(test[0],test[1])
    test = plus(test[0],test[1])
    if max < abs(test[1][0]) : max = abs(test[1][0])
        
    
    giho =[]+rgiho
    numbers=[]+rnumbers
    test = plus(giho,numbers)
    test = mult(test[0],test[1])
    test = minus(test[0],test[1])
    if max < abs(test[1][0]) : max = abs(test[1][0])
        
    
    giho =[]+rgiho
    numbers=[]+rnumbers   
    test = plus(giho,numbers)
    test = minus(test[0],test[1])
    test = mult(test[0],test[1])
    if max < abs(test[1][0]) : max = abs(test[1][0])
        
    giho =[]+rgiho
    numbers=[]+rnumbers    
    test = minus(giho,numbers)
    test = plus(test[0],test[1])
    test = mult(test[0],test[1])
    if max < abs(test[1][0]) : max = abs(test[1][0])
        
    
    giho =[]+rgiho
    numbers=[]+rnumbers   
    test = minus(giho,numbers)
    test = mult(test[0],test[1])
    test = plus(test[0],test[1])

    if max < abs(test[1][0]) : 
        max = abs(test[1][0])  
    return max

