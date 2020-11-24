while True:
    string = input()

    if len(string) == 1:
        break

    S = []
    candidates = ['(',')','[',']']
    for char in string :
        if char in candidates:
            S.append(char)

    stack = []
    pos = True
    for char in S:

        # 여는 괄호면 push
        if char == '(' or char == '[':
            stack.append(char)

        elif char ==')' :
            if not stack:
                pos= False
                break
                
            elif stack[-1] == '(':
                stack.pop()
            else : 
                pos = False
                break

        elif char ==']':
            if not stack:
                pos = False
                break
            elif  stack[-1] == '[':
                stack.pop()
            else : 
                pos = False
                break

# pos = False 이거나 stack 가 비지 않았으면 no 출력
    if not pos or stack:
        print('no')
    else:
        print('yes')
    
