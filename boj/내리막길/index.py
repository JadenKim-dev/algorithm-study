from sys import stdin
input = stdin.readline
UNVISITED = -1
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
board_cnt = [[UNVISITED]*N for _ in range(M)]

def dfs(r, c):
    if r == M-1 and c == N-1:
        return 1
    if board_cnt[r][c] != UNVISITED:
        return board_cnt[r][c]
    board_cnt[r][c] = 0
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if nr<0 or nr>=M or nc<0 or nc>=N:
            continue
        if board[nr][nc] >= board[r][c]:
            continue
        board_cnt[r][c] += dfs(nr, nc)
    return board_cnt[r][c]

print(dfs(0, 0))