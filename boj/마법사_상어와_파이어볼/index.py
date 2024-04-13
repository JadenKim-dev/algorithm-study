from sys import stdin
from collections import defaultdict
from functools import reduce

EMPTY = 0
readints = lambda : map(int, stdin.readline().split())
N, M, K = readints()

fires = defaultdict(list)
for _ in range(M):
    r, c, m, s, d = readints()
    fires[(r-1, c-1)].append((m, s, d))

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    tmp_fires = defaultdict(list)
    to_be_splitted = []
    for r, c in fires.keys():
        for m, s, d in fires[(r, c)]:
            nr, nc = (r+dr[d]*s)%N, (c+dc[d]*s)%N
            tmp_fires[(nr, nc)].append((m, s, d))
            if len(tmp_fires[(nr, nc)]) == 2:
                to_be_splitted.append((nr, nc))
    for r, c in to_be_splitted:
        sum_m, sum_s, is_all_odd, is_all_even = 0, 0, True, True
        for m, s, d in tmp_fires[(r, c)]:
            sum_m += m
            sum_s += s
            is_all_odd = is_all_odd and (d%2 == 1)
            is_all_even = is_all_even and (d%2 == 0)
        nm, ns = sum_m//5, sum_s//len(tmp_fires[(r, c)])
        if nm == 0:
            tmp_fires[(r, c)] = []
            continue
        nd_list = [0, 2, 4, 6] if is_all_odd or is_all_even else [1, 3, 5, 7]
        tmp_fires[(r, c)] = [(nm, ns, nd) for nd in nd_list]
    fires = tmp_fires

result = 0
for r, c in fires.keys():
    result += reduce(lambda a, b : a + b[0], fires[(r, c)], 0)
             
print(result)