answer = 0
_ = input()
word = input()
cnt = 0
for char in word:
    num = ord(char) - ord('a') + 1
    answer += (num * 31**cnt)
    cnt += 1
print(answer%1234567891)
