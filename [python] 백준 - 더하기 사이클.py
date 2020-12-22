n = input()

target = int(n)
cnt = 1
while True:
    # 한자리수 
    if len(n) ==1 :
        n = '0'+n
    
    n = n[1]+str(eval(n[0]+ '+'+ n[1]))[-1]
    
    if int(n)== target :
        break
    cnt +=1
print(cnt)