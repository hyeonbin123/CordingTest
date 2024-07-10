def main():
    s=input().strip()
    substrings = set()
    
    # 모든 가능한 부분 문자열 생성
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    print(len(substrings))
    
if __name__ == "__main__":
    main()