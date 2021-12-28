'''
와일드카드가 접두사에 있는 경우와 접미사에 있는 경우를 나누어서 처리
와일드카드 부분을 a 와 z로 변경하고 bisect함수를 이용하여 해당 되는 단어가 몇개인지 구하면된다.

예를 들어 쿼리에 'pro???'  가 들어있고 단어에는 [proabc, procdd,prabcd] 가들어있다면 
prabcd  proaaa(?를 a로변경) proabc procdd prozzz(? 를 z로 변경) 
prozzz의 인덱스 (4) - proaaa의 인덱스 (1) - 1 = 2  -> 해당하는 가사의 갯수 2 
'''

# 가사 검색

import bisect
import collections

def func(a,left,right):
    left_idx = bisect.bisect_left(a,left)
    right_idx = bisect.bisect_right(a,right)

    return right_idx - left_idx

def solution(words, queries):
    answer = []
    # 단어 길이 순으로 분리하기위해 딕셔너리 생성
    dic = collections.defaultdict(list)
    dic_reverse = collections.defaultdict(list)
    for word in words:
        # 단어 길이 순으로 분리
        dic[len(word)].append(word)
        dic_reverse[len(word)].append(word[::-1])


    #정렬
    for key in dic.keys():
        dic[key].sort()
        dic_reverse[key].sort()

    for query in queries: # 쿼리를 하나씩 확인하며 처리
        #접미사에 와일드 카드가 붙은 경우
        if query[0] != '?':
            answer.append(func(dic[len(query)],query.replace('?','a'),query.replace('?','z')))

        #접두사에 와일드 카드가 붙은 경우
        else :
            query = query[::-1]
            answer.append(func(dic_reverse[len(query)],query.replace('?','a'),query.replace('?','z')))
    return answer