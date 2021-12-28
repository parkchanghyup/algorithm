import collections
n = int(input())
dic = collections.defaultdict(int)

for i in range(n):
    string= input()
    for idx,c in enumerate(string):
        dic[c] += 10**(len(string)-idx-1)
numbers = sorted(dic.values(),reverse=True)

answer= 0
num = 9
for i in range(len(numbers)):
    answer+=numbers[i] * num
    num -=1
print(answer)
    

