#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#베스트앨범
def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        key = genres[i]
        value = plays[i]
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]
#재생횟수 순으로 정렬
    for name in dic:
        dic[name].sort(reverse=True)
    dic_sum = {}

    for name in dic:
        dic_sum[name] = (sum(dic[name]))


# 밸류를 기준으로 내림차순 정렬
    dic_sum = dict(
        sorted(dic_sum.items(), reverse=True, key=lambda item: item[1]))
    result = []
    #총 재생수가 많은 거 순서대로 해서 list로 만듦
    for name in list(dic_sum.keys()):
        if len(dic[name]) < 2:
            result.append(plays.index(dic[name][0]))
        else:
            result.append(plays.index(dic[name][0]))
            plays[plays.index(dic[name][0])] = 0
            result.append(plays.index(dic[name][1]))
    return result

