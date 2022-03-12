def solution(s):
    answer = -1
    stack = []
    stack.append(s[0])
    idx = 1
    while idx < len(s):
        if not stack:
            stack.append(s[idx])

        elif stack[-1] == s[idx]:
            stack.pop()
        else:
            stack.append(s[idx])
        idx += 1

    if stack:
        return 0
    else:
        return 1


solution('abbcdaadca')