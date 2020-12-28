def solution(clothes):
    closet = {}
    result =1
    for name in clothes:
        key = name[1]
        value = name[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key]= [value]
    for key in closet.keys():
    # 압입는 경우도 있으니 +1 해서 곱해주고 하나도 안입는 경우는 없으니 
    #마지막에 -1 해서 return한다

        result = result * (len(closet[key])+1)
        
    return result -1