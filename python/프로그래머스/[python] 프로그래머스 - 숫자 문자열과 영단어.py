def solution(s):
    answer = ''
    
    number_dic = {'zero' : '0',
                 'one' : '1',
                 'two' : '2',
                 'three' : '3',
                 'four' : '4',
                  'five' : '5',
                 'six' : '6',
                 'seven' : '7',
                 'eight' : '8',
                 'nine' : '9'}
    word = ''
    for char in s:
        if char.isnumeric():
            answer += str(char)
            continue
        
        word += char
        if word in number_dic.keys():
            answer += number_dic[word]
            word = ''
    
    
    return int(answer)