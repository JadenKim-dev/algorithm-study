from sys import stdin

R, C, m = map(int, stdin.readline().split())
board = [[0]*C for _ in range(R)]
sharks = {}
for i in range(m):
    x, y, s, d, z = map(int, stdin.readline().split())
    sharks[z] = [x-1, y-1, s, d-1]
    board[x-1][y-1] = z

def sol():
    global board
    total_size = 0
    for man in range(C):
        total_size += find_closest_shark(man)
        curr_sharks = list(sharks.keys())
        tmp_board = [[0]*C for _ in range(R)]
        for size in curr_sharks:
            if size not in sharks:
                continue
            x, y, speed, d = sharks[size]
            nx, ny = get_destination(x, y, speed, d)
            move(tmp_board, size, x, y, nx, ny)
        board = tmp_board
    return total_size
    
def find_closest_shark(col):
    for i in range(R):
        if board[i][col] > 0:
            shark = board[i][col]
            del sharks[shark]
            board[i][col] = 0
            return shark
    return 0

first_wall = [0, R-1, C-1, 0]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]     
def get_destination(x, y, speed, d):
    initial = x if d < 2 else y
    limit = R-1 if d < 2 else C-1
    dist = abs(initial - first_wall[d])
    def rotate(x, y):
        sharks[board[x][y]][3] = 1-d if d < 2 else 5-d

    if speed <= dist:
        return x + dx[d]*speed, y + dy[d]*speed
    if speed > dist:
        speed -= dist
        rotate_cnt = speed // limit
        if rotate_cnt % 2 == 0:
            dest = abs(first_wall[d] - (speed % limit))
            rotate(x, y)    
        else:
            dest = limit - abs(first_wall[d] - (speed % limit))
        return (dest, y) if d < 2 else (x, dest)

def move(board, size, x, y, nx, ny):
    if board[nx][ny] < size:
        if board[nx][ny] > 0:
            del sharks[board[nx][ny]]
        board[nx][ny] = size
        sharks[size][0], sharks[size][1] = nx, ny
    elif size < board[nx][ny]:
        del sharks[size]

print(sol())