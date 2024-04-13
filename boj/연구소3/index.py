from sys import stdin
from itertools import combinations, product
from copy import deepcopy
from collections import deque
BLANK = 0; WALL = 1; UNACT = 2; ACT = 3;
INF = int(1e9)
MAX = 2500

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
viruses = [(i, j) for i, j in product(range(n), range(n)) if board[i][j] == 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sol():
    min_time = INF
    for comb in combinations(viruses, m):
        min_time = min(min_time, get_spread_time(comb))
    return min_time if min_time < INF else -1

def get_spread_time(act_viruses):
    tmp_board = deepcopy(board)
    count_blank = sum([line.count(BLANK) for line in board])
    for x, y in act_viruses:
        tmp_board[x][y] = ACT
    q = deque(act_viruses)
    for second in range(MAX):
        if count_blank == 0:
            return second
        num = len(q)
        for _ in range(num):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if tmp_board[nx][ny] in [WALL, ACT]:
                    continue
                elif tmp_board[nx][ny] == BLANK:
                    count_blank -= 1
                tmp_board[nx][ny] = ACT
                q.append((nx, ny))
        if not q:
            return INF

print(sol())