from __future__ import annotations
from typing import Dict, List
import sys

class AntNestNode:
    def __init__(self, name: str):
        self.name: str = name
        self.children: Dict[str, AntNestNode] = {}

    def add_child(self, name: str) -> AntNestNode:
        if name not in self.children:
            self.children[name] = AntNestNode(name)
        return self.children[name]

    def print_structure(self, depth: int = 0) -> None:
        if depth > 0:
            print("--" * (depth - 1) + self.name)
        for child in sorted(self.children.values(), key=lambda x: x.name):
            child.print_structure(depth + 1)

class AntNest:
    def __init__(self):
        self.root: AntNestNode = AntNestNode("")

    def add_path(self, path: List[str]) -> None:
        current = self.root
        for food in path:
            current = current.add_child(food)

    def print_structure(self) -> None:
        self.root.print_structure()

def process_input() -> AntNest:
    ant_nest = AntNest()
    n = int(sys.stdin.readline().strip())
    
    for _ in range(n):
        path = sys.stdin.readline().split()[1:]
        ant_nest.add_path(path)
    
    return ant_nest

def main() -> None:
    ant_nest = process_input()
    ant_nest.print_structure()

if __name__ == "__main__":
    main()