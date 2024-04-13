from sys import stdin
EMPTY = 0; WALL = 1
RIGHT = 0; UP = 1; LEFT = 2; DOWN = 3
readints = lambda : map(int, stdin.readline().split())

R, C, K = readints()
board = [list(readints()) for _ in range(R)]
walls = [[[EMPTY]*4 for _ in range(C)]for _ in range(R)]
W = int(stdin.readline())
for _ in range(W):
    r, c, t = readints()
    r, c = r-1, c-1
    if t == 0:
        walls[r][c][UP] = walls[r-1][c][DOWN] = WALL
    elif t == 1:
        walls[r][c][RIGHT] = walls[r][c+1][LEFT] = WALL

heaters, targets = [], []
for r in range(R):
    for c in range(C):
        if board[r][c] == 1:
            heaters.append((r, c, RIGHT))
        elif board[r][c] == 2:
            heaters.append((r, c, LEFT))
        elif board[r][c] == 3:
            heaters.append((r, c, UP))
        elif board[r][c] == 4:
            heaters.append((r, c, DOWN))
        elif board[r][c] == 5:
            targets.append((r, c))
        board[r][c] = 0

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def sol():
    heat_amount = get_heat_amount_from(heaters)
    for chocolate in range(1, 101):
        for r in range(R):
            for c in range(C):
                board[r][c] += heat_amount[r][c]
        spread()
        decrease_outer()
        if is_over():
            return chocolate
    return 101

def get_heat_amount_from(heaters):
    heat_amount = [[0]*C for _ in range(R)]
    for hr, hc, d in heaters:
        heat(hr, hc, d, heat_amount)
    return heat_amount

def heat(hr, hc, d, heat_amount):
    sr, sc = hr+dr[d], hc+dc[d]
    heat_amount[sr][sc] += 5
    curr = {(sr, sc)}
    temparature = 4
    pd, nd = (d-1)%4, (d+1)%4
    
    while temparature > 0:
        next = set()
        for r, c in curr:
            if is_valid(r, c, d):
                nr1, nc1 = r+dr[d], c+dc[d]
                if (nr1, nc1) not in next:
                    next.add((nr1, nc1))
                    heat_amount[nr1][nc1] += temparature
                    
            if is_valid(r, c, pd):
                nr2, nc2 = r+dr[pd], c+dc[pd]
                nrr2, ncc2 = nr2+dr[d], nc2+dc[d]
                if is_valid(nr2, nc2, d) and (nrr2, ncc2) not in next:
                    next.add((nrr2, ncc2))
                    heat_amount[nrr2][ncc2] += temparature

            if is_valid(r, c, nd):
                nr3, nc3 = r+dr[nd], c+dc[nd]
                nrr3, ncc3 = nr3+dr[d], nc3+dc[d]
                if is_valid(nr3, nc3, d) and (nrr3, ncc3) not in next:
                    next.add((nrr3, ncc3))
                    heat_amount[nrr3][ncc3] += temparature

        if not next:
            break

        curr = next
        temparature -= 1

def is_valid(r, c, d):
    nr, nc = r+dr[d], c+dc[d]
    return 0 <= nr < R and 0 <= nc < C and walls[r][c][d] == EMPTY

def spread():
    spread_board = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            spread_sum = 0
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if is_valid(r, c, i) and board[nr][nc] < board[r][c]:
                    amount = (board[r][c] - board[nr][nc]) // 4
                    spread_board[nr][nc] += amount
                    spread_sum += amount
            spread_board[r][c] -= spread_sum
    for r in range(R):
        for c in range(C):
            board[r][c] += spread_board[r][c]

def decrease_outer():
    for r in range(R):
        board[r][0] = max(board[r][0]-1, 0)
        board[r][C-1] = max(board[r][C-1]-1, 0)
    for c in range(1, C-1):
        board[0][c] = max(board[0][c]-1, 0)
        board[R-1][c] = max(board[R-1][c]-1, 0)

def is_over():
    for r, c in targets:
        if board[r][c] < K:
            return False
    return True

print(sol())
