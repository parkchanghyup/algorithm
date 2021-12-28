from typing import List
import collections
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result =[0]*len(T)

        for i in range(len(T)):
            if not stack : 
                stack.append(i)
            else:
                print(T[stack[-1]],T[i])
                while stack and T[stack[-1]]<T[i] :
                    idx = stack.pop(-1)
                    result[idx] = i-idx
                stack.append(i)  

        return result