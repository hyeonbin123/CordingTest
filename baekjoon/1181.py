# 입력 받기
N = int(input())
words = set()  # 중복 제거를 위해 집합(set) 사용

for _ in range(N):
    words.add(input().strip())

# 정렬
sorted_words = sorted(words, key=lambda x: (len(x), x))

# 결과 출력
for word in sorted_words:
    print(word)