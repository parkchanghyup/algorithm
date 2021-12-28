def solution(msg)
    dic = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
               'R','S','T','U','V','W','X','Y','Z']
    #사전내 단어중 가장 길이가 긴 단어의 길이

    result = []
    compare_word=''
    for i in range(len(msg))

        max_dic = len(max(dic,key=len))
        if i  len(compare_word) continue
        if max_dic  1
            for j in range(max_dic,-1,-1)
                if i+j  len(msg) continue         
                char = msg[ii+j]

                if char in dic

                    compare_word+=char
                    result.append(dic.index(char))
                    if i+j  len(msg)
                        dic.append(char+msg[i+j])
                    break
        else 
            compare_word +=msg[i]
            result.append(dic.index(msg[i]))
            if i+1  len(msg)

                dic.append(msg[i]+msg[i+1])

    return(result)