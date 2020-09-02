#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    bridge_weight = 0
    idx = 0
    bridge_length -= 1
    while (1):

        if bridge_weight + truck_weights[idx] > weight:

            bridge.append(0)
        else:
            bridge.append(truck_weights[idx])
            bridge_weight += truck_weights[idx]
            idx += 1
        if len(bridge) > bridge_length:
            bridge_weight -= bridge.pop(0)

        answer += 1

        if idx == len(truck_weights):
            answer += bridge_length
            answer += 1
            break

    return answer

