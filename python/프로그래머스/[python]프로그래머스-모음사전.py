word = 'AEIOU'
word_list = []
def func(text):
    word_list.append(text)
    if len(text) == 5:
        
        return
    
    for c in word:
        func(text+c)


def solution(word):
    func('')
    for i,text in enumerate(word_list):
        
        if text == word:
            return i

solution('AAAAE')