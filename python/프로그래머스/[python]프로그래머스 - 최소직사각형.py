def solution(sizes):
    answer = 0
    left,right = [],[]
    for size in sizes:
        sorted_size = sorted(size)
        left.append(sorted_size[0])
        right.append(sorted_size[1])
    
    left.sort()
    right.sort()
    return left[-1] * right[-1]