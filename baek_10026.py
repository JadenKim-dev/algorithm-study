from sys import stdin

input = stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1 ,1]

N = int(input())
board = [list(input().strip()) for _ in range(N)]


def get_cnt(is_blind):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            bfs(r, c, is_blind, visited)
            cnt += 1
    return cnt


def bfs(sr, sc, is_blind, visited):
    q = [(sr, sc)]
    color = board[sr][sc]
    while q:
        r, c = q.pop()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] != color:
                if not is_blind:
                    continue
                elif not (color in {'R', 'G'} and board[nr][nc] in {'R', 'G'}):
                    continue
            visited[nr][nc] = True
            q.append((nr, nc))


not_blind_cnt = get_cnt(is_blind=False)
blind_cnt = get_cnt(is_blind=True)

print(not_blind_cnt, blind_cnt)