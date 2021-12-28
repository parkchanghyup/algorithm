n = int(input())

strings = []
for _ in range(n):
    strings.append(input())
    
s= list(strings[0])
    
    
for i in range(1,n):
    for j in range(len(s)):
        if s[j] != strings[i][j]:
            s[j] = '?'
print(''.join(s))
    
