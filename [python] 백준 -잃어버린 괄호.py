'''
그리디 알고리즘 문제로 +연산을 먼저처리하고 - 연산을 처리해주면 된다.
1. 숫자와 문자 를 분리하여 저장.
2. 문자중 +먼저 처리
3. +처리 후 -처리
'''



s =input()
nums = []
num = ''

# 숫자 문자 분리

for char in s:
    if char.isdigit():
        num+=char
    else:
        nums.append(int(num))
        num = ''
        nums.append(char)
nums.append(int(num))


# + 먼저 처리
nums2 = []

for idx,char in enumerate(nums):
    if char == '+':
        
        nums2[-1] += nums[idx+1]
        
    elif idx != 0 and nums[idx-1]=='+':
        continue
    else :
        nums2.append(char)
    

# - 처리
result = int(nums2[0])*2


for idx,num in enumerate(nums2):
    
    if num != '-':
        result -= int(num)
        
print(result)
    

