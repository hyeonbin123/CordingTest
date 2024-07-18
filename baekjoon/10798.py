s=[input().strip() for _ in range(5)]
print(s)
for x in range(len(s)):
    for y in range(5):
        print(str(s[y][x]),end='')