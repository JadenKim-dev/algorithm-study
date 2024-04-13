from sys import stdin
from itertools import product
from copy import deepcopy
from functools import reduce

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
cctvs = [
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

tv_infos = []
for i in range(n):
    for j in range(m):
        if 1 <= board[i][j] <= 5:
            tv_infos.append((board[i][j], i, j))

def convert(tv_type):
    if tv_type == 1 or tv_type == 3 or tv_type == 4:
        return [0, 1, 2, 3]
    elif tv_type == 2:
        return [0, 1]
    return [0]

answer = int(1e9)
for prd in product(*[convert(info[0]) for info in tv_infos]):
    tmp_board = deepcopy(board)
    for i in range(len(tv_infos)):
        tv_type, r, c = tv_infos[i]
        directions = cctvs[tv_type-1][prd[i]]
        for d in directions:
            x, y = r, c
            while True:
                nx, ny = x + dx[d], y + dy[d]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    break
                if board[nx][ny] == 6:
                    break
                x, y = nx, ny
                tmp_board[x][y] = 7
    answer = min(answer, reduce(lambda a, b: a + b.count(0), tmp_board, 0))

print(answer)