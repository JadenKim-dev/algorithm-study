from sys import stdin
from collections import defaultdict
INF = int(1e9)

n, m = map(int, stdin.readline().split())
board = [list(stdin.readline()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            bx, by = i, j
        elif board[i][j] == 'R':
            rx, ry = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = INF
history = defaultdict(bool)
history[(bx, by, rx, ry)] = True
def dfs(cnt, bx, by, rx, ry):
    global answer, history
    if cnt >= 10 or board[bx][by] == 'O':
        return
    for i in range(4):
        nbx, nby = bx, by
        nrx, nry = rx, ry
        bcnt, rcnt = 0, 0
        while board[nbx+dx[i]][nby+dy[i]] not in ['#', 'O']:
            nbx += dx[i]; nby += dy[i]
            bcnt += 1
        while board[nrx+dx[i]][nry+dy[i]] not in ['#', 'O']:
            nrx += dx[i]; nry += dy[i]
            rcnt += 1
        if board[nbx+dx[i]][nby+dy[i]] == 'O':
            continue
        if board[nrx+dx[i]][nry+dy[i]] == 'O':
            answer = min(answer, cnt+1)
        if nbx == nrx and nby == nry:
            if rcnt > bcnt:
                nrx -= dx[i]; nry -= dy[i]
            elif rcnt < bcnt:
                nbx -= dx[i]; nby -= dy[i]

        if history[(nbx, nby, nrx, nry)]:
            continue

        history[(nbx, nby, nrx, nry)] = True
        dfs(cnt+1, nbx, nby, nrx, nry)
        history[(nbx, nby, nrx, nry)] = False

dfs(0, bx, by, rx, ry)
print(answer if answer < INF else -1)