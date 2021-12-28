'''
각 단어에 맞는 숫자를 딕셔너리 형태로 생성
그리고 각 단어에 해당하는 숫자를 n이라고한다면 , 곱에 해당하느숫자는 10^n 꼴이다.
마지막으로 조건에 맞게 출력하면된다.
'''

dic  = {'black':'0',
       'brown':'1',
       'red':'2',
       'orange':'3',
       'yellow':'4',
       'green':'5',
       'blue':'6',
       'violet':'7',
       'grey':'8',
       'white':'9'}

a= input()
b= input()
c= input()

print(int(dic[a]+dic[b]) * (10**int(dic[c])))