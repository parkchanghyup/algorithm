def solution(n, words):
    answer = []
    past = [words[0]]
    cnt = 1 
    pos = True
    for idx in range(1,len(words)):
        
        word = words[idx]
        if word in past or word[0] != words[idx-1][-1]:
            pos = False
            break
            
        past.append(word)
        
    
    if idx == len(words)-1 and pos ==True:
        return [0,0]
    idx +=1
    a,b = (divmod(idx,n))
    if b == 0 :
        return [n,a]
    return [b,a+1]