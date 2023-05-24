def solution(numbers):
    answer = [-1] * len(numbers)
    stack  = []
    
    for idx,number in enumerate(numbers):
        while stack and stack[-1][1] < number:
            num_idx, _ =  stack.pop()
            answer[num_idx] = number
        stack.append((idx,number))
    
    return answer