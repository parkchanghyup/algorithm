'''
정규표현식을 이용하여 알파벳과 '-' 을 제외한 문자를 제거하고
단어들을 길이에 따라 정렬해준다.
마지막단어가 'E-N-D'가 될때까지 반복.
'''

import re

words = []

while True:
    words.extend(input().split())
    if words[-1] =='E-N-D' : 
        
        break

words = [re.sub('[^a-z-]','',x.lower()) for x in words ]
words.sort(key =lambda x :  len(x),reverse = True)
print(words[0].lower())