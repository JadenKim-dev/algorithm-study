from sys import stdin, exit
WHITE = 0; RED = 1; BLUE = 2

readline = lambda : map(int, stdin.readline().split())
n, k = readline()
colors = [list(readline()) for _ in range(n)]
pieces = []
board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    r, c, d = readline()
    pieces.append([r-1, c-1, d-1])
    board[r-1][c-1].append(i)

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
            
def go(p_idx):
    r, c, d = pieces[p_idx]
    nr, nc = r+dr[d], c+dc[d]
    if (nr<0 or nr>=n or nc<0 or nc>=n) or colors[nr][nc] == BLUE:
        blue_from(p_idx, r, c, d)
    elif colors[nr][nc] == RED:
        move_from_to(p_idx, r, c, nr, nc, is_red_type=True)
    elif colors[nr][nc] == WHITE:
        move_from_to(p_idx, r, c, nr, nc, is_red_type=False)

def blue_from(p_idx, r, c, d):
    d = 1-d if d < 2 else 5-d
    pieces[p_idx][2] = d
    nr, nc = r+dr[d], c+dc[d]
    if 0<=nr<n and 0<=nc<n and colors[nr][nc] != BLUE:
        go(p_idx)

def move_from_to(p_idx, r, c, nr, nc, is_red_type):
    in_cell_idx = board[r][c].index(p_idx)
    to_be_moved = board[r][c][in_cell_idx:]
    if is_red_type:
        to_be_moved.reverse()
    board[nr][nc] += to_be_moved
    board[r][c] = board[r][c][:in_cell_idx]
    for piece in to_be_moved:
        pieces[piece][0], pieces[piece][1] = nr, nc
    end_if_over(nr, nc)

def end_if_over(nr, nc):
    if len(board[nr][nc]) >= 4:
        print(time)
        exit()

for time in range(1, 1000):
    for p_idx in range(k):
        go(p_idx)
print(-1)