def solution(s):
    stack = []

    for char in s:

        if char == ')':
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append('(')

    if stack:
        return False

    return True