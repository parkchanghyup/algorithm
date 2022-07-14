def check(s):
    '''
    올바른 괄호 문자열 인지 체크
    '''
    stack = []

    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == '[' and char == ']':
                stack.pop()
            elif stack[-1] == '(' and char == ')':
                stack.pop()
            elif stack[-1] == '{' and char == '}':
                stack.pop()
            else:
                stack.append(char)

    if len(stack) == 0:
        return True
    return False


def solution(s):
    answer = 0
    cnt = len(s)

    while cnt > 0:

        # 올바른 괄호 문자열 확인
        if check(s):

            answer += 1

        # 문자열 왼쪽으로 회전
        s = s[1:] + s[0]
        cnt -= 1

    return answer


solution("[](){}")
