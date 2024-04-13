from sys import stdin
from functools import reduce
from itertools import groupby, chain
EMPTY = 0

def blizzard(d, s):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(1, s+1):
        r, c = sr+dr[d-1]*i, sc+dc[d-1]*i
        board[r][c] = EMPTY

def explode():
    nums = [board[r][c] for r, c in routes if board[r][c]]
    converted_gems = [(len(list(group)), num) for num, group in groupby(nums)]
    is_exploded = False
    
    while True:
        remain_gems = []
        for cnt, num in converted_gems:
            if cnt >= 4:
                explode_cnt[num] += cnt
                is_exploded = True
            else:
                remain_gems.append([cnt, num])
                
        if not is_exploded:
            return remain_gems
    
        combined_remain_gems = []
        for num, group in groupby(remain_gems, key=lambda x: x[1]):
            cnt_sum = reduce(lambda a,b : a+b[0], group, 0)
            combined_remain_gems.append([cnt_sum, num])
        converted_gems = combined_remain_gems
        is_exploded = False

def transform_from(gems):
    for num, (r, c) in zip(chain.from_iterable(gems), routes):
        board[r][c] = num

readints = lambda : map(int, stdin.readline().split())
n, m = readints()
board = [list(readints()) for _ in range(n)]
magics = [list(readints()) for _ in range(m)]

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
d = 0
r = c = n//2
routes = []
for i in range(2, 2*n + 1):
    for _ in range(i//2):
        r += dr[d]
        c += dc[d]
        routes.append((r, c))
    d = (d+1)%4
routes.pop()
explode_cnt = [0]*4

sr, sc = n//2, n//2

for d, s in magics:
    blizzard(d, s)
    converted_gems = explode()
    board = [[EMPTY]*n for _ in range(n)]
    transform_from(converted_gems)
   
print(reduce(lambda a,b : a + b*explode_cnt[b], range(4), 0))