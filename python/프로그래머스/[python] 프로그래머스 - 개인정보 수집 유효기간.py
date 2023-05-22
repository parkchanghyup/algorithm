def solution(today, terms, privacies):

    terms_dic = {}
    answer = []    
    
    for value in terms:
        key, value = value.split(' ')
        terms_dic[key] = value
        
    for idx, value in enumerate(privacies):
        date, key = value.split(' ')
        year,month,day = date.split('.')
        limit_month = int(terms_dic[key])
        
        month = int(month) + limit_month
        day = int(day) - 1 
        
        if day < 1 :
            day = 28
            month -= 1
        
        while month > 12:
            month -= 12
            year = int(year) + 1 
        
        
        limit_date = '.'.join([str(year),str(month).zfill(2),str(day).zfill(2)])

        if today > limit_date:
            answer.append(idx+1)
        
    
    return answer