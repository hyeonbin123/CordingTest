s=input().strip()
positions = [s.find(chr(i)) for i in range(ord('a'), ord('z') + 1)]
print(' '.join(map(str, positions)))