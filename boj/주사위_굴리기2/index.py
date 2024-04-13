from sys import stdin
from collections import deque

readints = lambda : map(int, stdin.readline().split())
n, m, k = readints()
board = [list(readints()) for _ in range(n)]

def count_block(sr, sc, is_done):
    q = deque([(sr, sc)])
    visited = [[False]*m for _ in range(n)]
    visited[sr][sc] = True
    blocks = [(sr, sc)]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=n or nc<0 or nc>=m or visited[nr][nc]:
                continue
            if board[nr][nc] == board[sr][sc]:
                blocks.append((nr, nc))
                q.append((nr, nc))
            visited[nr][nc] = True
    for r, c in blocks:
        scores[r][c] = len(blocks)*board[sr][sc]
        is_done[r][c] = True

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

scores = [[0]*m for _ in range(n)]
is_done = [[False]*m for _ in range(n)]
for r in range(n):
    for c in range(m):
        if is_done[r][c]:
            continue
        count_block(r, c, is_done)

r, c, d = 0, 0, 0
score = 0
east, south, bottom = 3, 2, 6
for _ in range(k):
    nr, nc = r+dr[d], c+dc[d]
    if nr<0 or nr>=n or nc<0 or nc>=m:
        d = (d+2)%4
        nr, nc = r+dr[d], c+dc[d]
    r, c = nr, nc
    score += scores[r][c]
    
    if d == 0:
        bottom, east = east, 7-bottom
    elif d == 1:
        bottom, south = 7-south, bottom
    elif d == 2:
        bottom, east = 7-east, bottom
    elif d == 3:
        bottom, south = south, 7-bottom

    if bottom > board[r][c]:
        d = (d+1)%4
    elif bottom < board[r][c]:
        d = (d-1)%4
print(score)