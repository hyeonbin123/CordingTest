from collections import Counter
n = int(input().strip())
player = Counter(input().strip()[0] for _ in range(n))
selected_player = [letter for letter, count in player.items() if count >= 5]
print(''.join(sorted(selected_player)) if selected_player else 'PREDAJA')