from sys import stdin
from copy import deepcopy
BLANK = 0; SHARK = -1
MAX = 4

fishes = [BLANK]*17
board = [[BLANK]*4 for _ in range(4)]
for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, stdin.readline().split())
    fishes[a1] = (i, 0, b1-1)
    board[i][0] = a1
    fishes[a2] = (i, 1, b2-1)
    board[i][1] = a2
    fishes[a3] = (i, 2, b3-1)
    board[i][2] = a3
    fishes[a4] = (i, 3, b4-1)
    board[i][3] = a4

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def play(fishes, board, sx, sy, sd, eat_sum):
    global max_eat_sum
    for f_idx in range(1, 17):
        if fishes[f_idx] == BLANK:
            continue
        fx, fy, fd = fishes[f_idx]
        for i in range(8):
            nd = (fd+i) % 8
            nx, ny = fx+dx[nd], fy+dy[nd]
            if nx<0 or nx>=MAX or ny<0 or ny>=MAX:
                continue
            elif board[nx][ny] == SHARK:
                continue
            elif board[nx][ny] == BLANK:
                fishes[f_idx] = (nx, ny, nd)
                board[nx][ny] = f_idx
                board[fx][fy] = BLANK
                break
            else:
                f_idx2 = board[nx][ny]
                _, _, fd2 = fishes[f_idx2]
                fishes[f_idx] = (nx, ny, nd)
                fishes[f_idx2] = (fx, fy, fd2)
                board[nx][ny] = f_idx
                board[fx][fy] = f_idx2
                break

    is_fish_eaten = False
    for i in range(1, 4):
        nx, ny = sx+dx[sd]*i, sy+dy[sd]*i
        if nx<0 or nx>=MAX or ny<0 or ny>=MAX:
            break
        if board[nx][ny] != BLANK:
            board_copy = deepcopy(board)
            fishes_copy = deepcopy(fishes)
            
            target_fish = board[nx][ny]
            _, _, d = fishes[target_fish]
            board_copy[sx][sy] = BLANK
            board_copy[nx][ny] = SHARK
            fishes_copy[target_fish] = BLANK

            play(fishes_copy, board_copy, nx, ny, d, eat_sum + target_fish)
            is_fish_eaten = True
            
    if not is_fish_eaten:
        max_eat_sum = max(max_eat_sum, eat_sum)
                
init_fish = board[0][0]
_, _, d = fishes[init_fish]
sx, sy, sd = 0, 0, d
eat_sum = init_fish
board[0][0] = SHARK
fishes[init_fish] = BLANK

max_eat_sum = 0
play(fishes, board, sx, sy, sd, eat_sum)
print(max_eat_sum)