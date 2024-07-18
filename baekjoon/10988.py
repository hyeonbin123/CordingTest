# 단어 입력 받기
word = input().strip()

# 단어를 뒤집은 문자열 생성
reversed_word = word[::-1]

# 단어가 팰린드롬인지 확인
if word == reversed_word:
    print(1)
else:
    print(0)
