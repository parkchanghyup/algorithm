from typing import List


class Solution:
    def isValid(self, s: str) -> bool:

        dic = {']': '[', '}': '{', ')': '('}

        stack = []
        for char in s:
            # 스택이 비었으면 바로 push
            if not stack:
                stack.append(char)
            #  여는 괄호문자면 스택에 push
            elif char not in dic:
                stack.append(char)
            # 닫는 괄호 문자면 스택의 top와 비교
            elif stack.pop(-1) != dic[char]:
                return False

        if len(stack) > 0:
            return False

        return True