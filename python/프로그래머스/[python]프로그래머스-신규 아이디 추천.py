def solution(new_id):

    answer = ''
    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_word = ''
    for char in new_id:
        temp = ['-', '_', '.']
        if char.isalnum():
            new_word += char
        elif char in temp:
            new_word += char
        else:
            continue

    #  3단계
    while '..' in new_word:
        new_word = new_word.replace('..', '.')

    # 4단계
    while new_word and new_word[0] == '.':
        new_word = new_word[1:]
    while new_word and new_word[-1] == '.':
        new_word = new_word[:-1]

        # 5단계
    if new_word == '':
        new_word = 'a'

    # 6단계
    if len(new_word) > 15:
        new_word = new_word[:15]

    if new_word[-1] == '.':
        new_word = new_word[:-1]

    # 7단계

    while len(new_word) < 3:
        new_word += new_word[-1]

    return new_word