from sys import stdin
from collections import deque

BLANK = 0; WALL = 1; PERSON = 2; DEST = 3
IMPOSSIBLE = -1
INF = int(1e9)

intline = lambda : map(int, stdin.readline().split())
n, m, oil = intline()
board = [list(intline()) for _ in range(n)]
x, y = intline()
start_end_dict = {}
for _ in range(m):
    sx, sy, ex, ey = intline()
    board[sx-1][sy-1] = PERSON
    start_end_dict[(sx-1, sy-1)] = (ex-1, ey-1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def get_rest_oil(oil, x, y):
    for _ in range(m):
        sx, sy, min_dist = get_closest_person_from(x, y)
        if min_dist == IMPOSSIBLE:
            return -1
        oil -= min_dist
        board[sx][sy] = BLANK
        if oil <= 0:
            return -1
        
        ex, ey = start_end_dict[(sx, sy)]
        dist = get_dist_from_to(sx, sy, ex, ey)
        if dist == IMPOSSIBLE:
            return -1
        if oil-dist < 0:
            return -1
        oil += dist
        x, y = ex, ey
        del start_end_dict[(sx, sy)]
    return oil

def get_closest_person_from(x, y):
    candidates = []
    min_dist = INF
    q = deque([(x, y, 0)])
    visited = [[False]*n for _ in range(n)]
    while q:
        x, y, d = q.popleft()
        if candidates and d > min_dist:
            break
        if board[x][y] == PERSON:
            min_dist = d
            candidates.append((x, y))
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if board[nx][ny] == WALL:
                continue
            if visited[nx][ny]:
                continue
            q.append((nx, ny, d+1))
            visited[nx][ny] = True
    if not candidates:
        return IMPOSSIBLE, IMPOSSIBLE, IMPOSSIBLE
    sx, sy = sorted(candidates)[0]
    return sx, sy, min_dist

def get_dist_from_to(sx, sy, ex, ey):
    board[ex][ey] = DEST
    q = deque([(sx, sy, 0)])
    visited = [[False]*n for _ in range(n)]
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if board[nx][ny] == WALL:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == DEST:
                board[ex][ey] = PERSON if (ex, ey) in start_end_dict else BLANK
                return d+1
            q.append((nx, ny, d+1))
            visited[nx][ny] = True
    return IMPOSSIBLE

print(get_rest_oil(oil, x-1, y-1))