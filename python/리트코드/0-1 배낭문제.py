def zero_one_knapsack(cargo):
    capacity = 15
    pack = []
    
    for i in range(len(cargo)):
        pack.append([])
        for j in range(capacity+1):
            if i ==0 or j == 0:
                pack[i].append(0)
            elif cargo[i-1][1] <= j:
                pack[i].append(max(pack[i-1][j],
                                  pack[i-1][j-cargo[i-1][1]]+cargo[i-1][0])
                )
            else:
                pack[i].append(pack[i-1][j])
    
            
                   
                     
    return pack[-1][-1]
    