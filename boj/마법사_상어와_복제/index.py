from sys import stdin
readints = lambda : map(int, stdin.readline().split())

M, S = readints()
fishes = [[[0]*8 for _ in range(4)] for _ in range(4)]
for _ in range(M):
    r, c, d = readints()
    fishes[r-1][c-1][d-1] += 1
sr, sc = readints()
sr, sc = sr-1, sc-1
smells = [[0]*4 for _ in range(4)]

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

def fishes_move_from(fishes):
    fishes_tmp = [[[0]*8 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for d in range(8):
                if fishes[r][c][d] == 0:
                    continue
                is_moved = False
                for i in range(8):
                    dd = (d-i)%8
                    nr, nc = r+dr[dd], c+dc[dd]
                    if nr<0 or nr>=4 or nc<0 or nc>=4:
                        continue
                    if smells[nr][nc] > 0 or (nr,nc)==(sr,sc):
                        continue
                    fishes_tmp[nr][nc][dd] += fishes[r][c][d]
                    is_moved = True
                    break
                if not is_moved:
                    fishes_tmp[r][c][d] += fishes[r][c][d]
    return fishes_tmp

def shark_move(r, c, fish_sum, route):
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    global max_fish_sum, max_route
    if len(route) == 3:
        if max_fish_sum < fish_sum:
            max_fish_sum = fish_sum
            max_route = route
        return
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if nr<0 or nr>=4 or nc<0 or nc>=4:
            continue
        curr_route = route + [(nr, nc)]
        if (nr, nc) in route:
            shark_move(nr, nc, fish_sum, curr_route)
        else:
            curr_sum = fish_sum + sum(fishes[nr][nc])
            shark_move(nr, nc, curr_sum, curr_route)

def eat_fishes_at(route):
    for r, c in route:
        if sum(fishes[r][c]) > 0:
            for d in range(8):
                fishes[r][c][d] = 0
            smells[r][c] = 3

def smell_decrease():
    for r in range(4):
        for c in range(4):
            smells[r][c] = max(0, smells[r][c]-1)

def fishes_copy_from(fishes_prev):
    for r in range(4):
        for c in range(4):
            for d in range(8):
                fishes[r][c][d] += fishes_prev[r][c][d]

for _ in range(S):
    fishes_prev = fishes
    fishes = fishes_move_from(fishes)
    
    max_fish_sum, max_route = -1, []
    shark_move(sr, sc, 0, [])    
    eat_fishes_at(max_route)
    sr, sc = max_route[-1]

    smell_decrease()
    
    fishes_copy_from(fishes_prev)

result = 0
for r in range(4):
    for c in range(4):
        result += sum(fishes[r][c])
print(result)