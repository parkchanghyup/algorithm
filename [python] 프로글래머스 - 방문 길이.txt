def solution(dirs)
    answer = 0

    x, y = 0, 0

    # U D R L
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    dir = 0
    root = []
    for char in dirs

        if char == 'U'
            dir = 0
        elif char == 'D'
            dir = 1
        elif char == 'R'
            dir = 2
        elif char == 'L'
            dir = 3
            
        

        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if -6  nx  6 and -6  ny  6
            candidate = sorted([(x, y), (nx, ny)])

            if candidate not in root
                root.append(candidate)
            x = nx
            y = ny

    return len(root)