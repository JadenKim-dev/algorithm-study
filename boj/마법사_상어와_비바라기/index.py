from sys import stdin
from functools import reduce

readints = lambda : map(int, stdin.readline().split())
n, m = readints()
board = [list(readints()) for _ in range(n)]
moves = [list(readints()) for _ in range(m)]

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
clouds = {(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)}
for d, s in moves:
    clouds = [( (r+dr[d-1]*s)%n, (c+dc[d-1]*s)%n ) for r, c in clouds]
    for r, c in clouds:
        board[r][c] += 1
    for r, c in clouds:
        for i in range(1, 8, 2):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=n or nc<0 or nc>=n:
                continue
            board[r][c] += (board[nr][nc] > 0)
    new_clouds = set()
    for r in range(n):
        for c in range(n):
            if (r, c) in clouds:
                continue
            if board[r][c] >= 2:
                board[r][c] -= 2
                new_clouds.add((r, c))
    clouds = new_clouds
    
print(reduce(lambda a,b : a+sum(b), board, 0))