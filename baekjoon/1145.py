from itertools import combinations
from math import lcm

print(min([lcm(*number) for number in combinations(list(map(int,input().strip().split())),3)]))