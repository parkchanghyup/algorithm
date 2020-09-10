# 올바른 괄호 문자열 판별
def collect_str(s: str) -> bool:
    stack = []
    for char in s:
        if not stack:
            if char == ')':
                return False
            stack.append(char)
        elif char == ')':
            stack.pop()
        else:
            stack .append(char)

    return True


def check(s: str) -> bool:
    print(1)
    return s.count('(') == s.count(')')


def reversestr(s):
    result = ''
    for char in s:
        if char == ')':
            result += '('
        else:
            result += ')'
    return result

def return_uv(s):
    u ,v = s,''
    for i in range(2,len(s),2):
        if check(s[:i]):
            u=s[:i]
            v=s[i:]
            break
    return u,v
def func(s):
    if s == '': return s
    if collect_str(s): return s

    u,v = return_uv(s)

    print(u, v)
    if collect_str(u):
        return u+func(v)

    else:
        return '(' + func(v) + ')' + reversestr(u[1:-1])

    
def solution(p):
    if p == '':
        return ''
    answer =func(p)
    
    return answer