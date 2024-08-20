import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def find_all_prefixes(self, word):
        node = self.root
        prefixes = []
        for i, char in enumerate(word):
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_end:
                prefixes.append(i + 1)
        return prefixes

def is_valid_team_name(team_name, color_trie, nicknames):
    color_lengths = color_trie.find_all_prefixes(team_name)
    for length in color_lengths:
        if team_name[length:] in nicknames:
            return True
    return False

def process():
    C, N = map(int, input().split())
    
    color_trie = Trie()
    for _ in range(C):
        color_trie.insert(input().strip())
    
    nicknames = set(input().strip() for _ in range(N))
    
    Q = int(input())
    for _ in range(Q):
        team_name = input().strip()
        print("Yes" if is_valid_team_name(team_name, color_trie, nicknames) else "No")

process()