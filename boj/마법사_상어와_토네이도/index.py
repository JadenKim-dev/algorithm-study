from sys import stdin

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

r = c = n//2
d = 0
dist_list = []
for i in range(1, n):
    dist_list.append(i)
    dist_list.append(i)
dist_list.append(n-1)

def is_in_board(r, c):
    return 0<=r<n and 0<=c<n

def move_sand_from(r, c, d):
    global out_of_board_sand
    total_sand = rest_sand = board[r][c]
    def move_to(r, c, amount):
        global out_of_board_sand
        moving_sand = int(total_sand*amount)
        if is_in_board(r, c):
            board[r][c] += moving_sand
        else:
            out_of_board_sand += moving_sand
        return moving_sand
    pd, nd = (d-1)%4, (d+1)%4
    rest_sand -= move_to(r+dr[d]*2, c+dc[d]*2, 0.05)
    rest_sand -= move_to(r+dr[d]+dr[pd], c+dc[d]+dc[pd], 0.1)
    rest_sand -= move_to(r+dr[d]+dr[nd], c+dc[d]+dc[nd], 0.1)
    rest_sand -= move_to(r+dr[pd]*2, c+dc[pd]*2, 0.02)
    rest_sand -= move_to(r+dr[nd]*2, c+dc[nd]*2, 0.02)
    rest_sand -= move_to(r+dr[pd], c+dc[pd], 0.07)
    rest_sand -= move_to(r+dr[nd], c+dc[nd], 0.07)
    rest_sand -= move_to(r-dr[d]+dr[pd], c-dc[d]+dc[pd], 0.01)
    rest_sand -= move_to(r-dr[d]+dr[nd], c-dc[d]+dc[nd], 0.01)
    
    if is_in_board(r+dr[d], c+dc[d]):
        board[r+dr[d]][c+dc[d]] += rest_sand
    else:
        out_of_board_sand += rest_sand
    board[r][c] = 0
    
out_of_board_sand = 0
for dist in dist_list:
    for i in range(dist):
        r, c = r+dr[d], c+dc[d]
        move_sand_from(r, c, d)

    d = (d+1) % 4

print(out_of_board_sand)
