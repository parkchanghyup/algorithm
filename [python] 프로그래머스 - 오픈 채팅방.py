#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(record):
    answer = []
    input_data = []
    dic = {}
    actionList = {'Leave': '님이 나갔습니다.', 'Enter': '님이 들어왔습니다.'}
    action = []
    for i in range(len(record)):
        input_data.append(record[i].split(" "))
    for i in range(len(record)):
        if input_data[i][0] != 'Leave':
            dic[input_data[i][1]] = input_data[i][2]
        if input_data[i][0] != 'Change':
            action.append((input_data[i][0], input_data[i][1]))

    for act, ID in action:
        answer.append(dic[ID] + actionList[act])
    return answer

