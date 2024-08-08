import sys
input = sys.stdin.readline

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def solve_card_game(N, M, K, minsu_cards, chulsu_cards):
    cards = sorted(set(minsu_cards))
    card_indices = {card: i for i, card in enumerate(cards)}
    
    disjoint_set = DisjointSet(len(cards))
    
    results = []
    for chulsu_card in chulsu_cards:
        index = binary_search(cards, chulsu_card)
        
        if index < len(cards):
            root = disjoint_set.find(index)
            card = cards[root]
            results.append(card)
            
            if root + 1 < len(cards):
                disjoint_set.union(root, root + 1)
        else:
            root = disjoint_set.find(0)
            card = cards[root]
            results.append(card)
            
            if root + 1 < len(cards):
                disjoint_set.union(root, root + 1)
    
    return results

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left

N, M, K = map(int, input().split())
minsu_cards = list(map(int, input().split()))
chulsu_cards = list(map(int, input().split()))

result = solve_card_game(N, M, K, minsu_cards, chulsu_cards)

print('\n'.join(map(str, result)))