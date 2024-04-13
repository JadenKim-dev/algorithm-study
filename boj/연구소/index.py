from sys import stdin
from itertools import combinations
from copy import deepcopy
from collections import deque
from functools import reduce

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

virus, empty = [], []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            empty.append((i, j))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
for comb in combinations(empty, 3):
    board_now = deepcopy(board)
    for x, y in comb:
        board_now[x][y] = 1
    for x, y in virus:
        q = deque(); q.append((x, y))
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if board_now[nx][ny] == 0:
                    board_now[nx][ny] = 2
                    q.append((nx, ny))
    answer = max(answer, reduce(lambda a, b : a + b.count(0), board_now, 0))
print(answer)