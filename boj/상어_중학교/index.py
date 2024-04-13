from sys import stdin
from collections import deque
BLACK = -1; RAINBOW = 0; BLANK = -2;
NULL = -1

readints = lambda : map(int, stdin.readline().split())
n, m = readints()
board = [list(readints()) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def play():
    global board
    score = 0
    while True:
        groups = {}
        visited = [[False]*n for _ in range(n)]
        for sr in range(n):
            for sc in range(n):
                if visited[sr][sc]:
                    continue
                if board[sr][sc] <= 0:
                    continue
                groups[(sr, sc)] = get_group_from(sr, sc, visited)
        blocks = get_target_blocks_from(groups)
        if len(blocks) <= 1:
            return score
        score += len(blocks)**2
        for r, c in blocks:
            board[r][c] = BLANK
        apply_gravity(board)
        board = rotate(board)
        apply_gravity(board)

def get_group_from(sr, sc, visited):
    visited[sr][sc] = True
    color = board[sr][sc]
    q = deque([(sr, sc)])
    blocks = []
    rainbows = []
    while q:
        r, c = q.popleft()
        blocks.append((r, c))
        if board[r][c] == RAINBOW:
            rainbows.append((r, c))
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if (nr<0 or nr>=n or nc<0 or nc>=n) or visited[nr][nc]:
                continue
            if board[nr][nc] != color and board[nr][nc] != RAINBOW:
                continue
            q.append((nr, nc))
            visited[nr][nc] = True
    for r, c in rainbows:
        visited[r][c] = False
    return blocks, len(rainbows)

def get_target_blocks_from(groups):
    max_total_cnt = 0
    max_rainbow_cnt = 0
    target = NULL
    for r, c in groups.keys():
        blocks, rainbow_cnt = groups[(r, c)]
        total_cnt = len(blocks)
        if max_total_cnt < total_cnt:
            max_total_cnt = total_cnt
            max_rainbow_cnt = rainbow_cnt
            target = (r, c)
        elif max_total_cnt == total_cnt and rainbow_cnt >= max_rainbow_cnt:
            max_rainbow_cnt = rainbow_cnt
            target = (r, c)
    if target == NULL:
        return []
    blocks, _ = groups[target]
    return blocks

def apply_gravity(board):
    for i in range(n):
        for r in range(n-i-1):
            for c in range(n):
                if board[r][c] >= 0 and board[r+1][c] == BLANK:
                    board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
    return board

def rotate(board):
    tmp_board = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            tmp_board[n-1-c][r] = board[r][c]
    return tmp_board

print(play())등