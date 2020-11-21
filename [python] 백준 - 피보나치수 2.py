n = int(input())

num1,num2 = 0,1

for i in range(n):
    num1,num2 = num2,num1+num2
print(num1)