from sys import stdin
from itertools import combinations
from functools import reduce

n, m, h = map(int, stdin.readline().split())
bridge = [[False]*(n-1) for _ in range(h)]
for _ in range(m):
    r, c = map(int, stdin.readline().split())
    bridge[r-1][c-1] = True

candidates = []
for i in range(h):
    for j in range(n-1):
        if not bridge[i][j]:
            candidates.append((i, j))

def get_dest(idx, bridge):
    for i in range(h):
        if idx < n-1 and bridge[i][idx]:
            idx += 1
        elif idx > 0 and bridge[i][idx-1]:
            idx -= 1
    return idx

def is_valid(bridge):
    return reduce(lambda a,b: a and get_dest(b, bridge)==b, range(n), True)

def sol():
    if is_valid(bridge):
        return 0
    for num in range(1, 4):
        for comb in combinations(candidates, num):
            for r, c in comb:
                bridge[r][c] = True
            if is_valid(bridge):
                return num
            for r, c in comb:
                bridge[r][c] = False
    return -1
print(sol())