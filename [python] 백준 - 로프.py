## 긴거 부터 계속 걸어봥


m = int(input())

ropes = []
for i in range(m):
    ropes.append(int(input()))
    


ropes.sort(reverse = True)

max_weight = []
for idx,rope in enumerate(ropes):
    max_weight.append(rope*(idx+1))
    

max_weight.sort()

print(max_weight[-1])
    