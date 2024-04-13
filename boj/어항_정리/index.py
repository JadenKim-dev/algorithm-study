from sys import stdin
from math import sqrt, floor
readints = lambda:map(int, stdin.readline().split())
INF = int(1e9); NULL = -1

N, K = readints()
bowls = list(readints())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def mapping_magic1(N):
    bowl_to_arr_map = [NULL]*N
    n = floor(sqrt(N))
    dist = [n-1]
    for i in range(2*n-1, 1, -1):
        dist.append(i//2)

    if n**2 <= N < n**2 + n:
        for i in range(N-1, -1, -1):
            if i >= n**2:
                bowl_to_arr_map[i] = (n-1, n+i-n**2)
            elif i == n**2 - 1:
                now, dist_idx = 1, 0
                r, c, d = n-1, n-1, 3
                bowl_to_arr_map[i] = (r, c)
            else:
                r, c = r+dr[d], c+dc[d]
                bowl_to_arr_map[i] = (r, c)
                now += 1
                if now > dist[dist_idx]:
                    now = 1
                    dist_idx += 1
                    d = (d+1)%4
    elif N >= n**2 + n:
        for i in range(N-1, -1, -1):
            if i >= n**2:
                bowl_to_arr_map[i] = (n, i-n**2)
            elif i == n**2 - 1:
                now, dist_idx = 1, 0
                r, c = n-1, 0
                d = 0
                bowl_to_arr_map[i] = (r, c)
            else:
                r, c = r+dr[d], c+dc[d]
                bowl_to_arr_map[i] = (r, c)
                now += 1
                if now > dist[dist_idx]:
                    now = 1
                    dist_idx += 1
                    d = (d+1)%4
    
    return bowl_to_arr_map

def reverse_mapping_magic1(N):
    n = floor(sqrt(N))
    arr_to_board_map = [NULL]*N
    if n**2 == N:
        for i in range(N):
            arr_to_board_map[i] = (n-1-i%n, i//n)
    elif n**2 < N < n**2+n:
        for i in range(N):
            if i < n**2:
                arr_to_board_map[i] = (n-1-i%n, i//n)
            else:
                arr_to_board_map[i] = (n-1, n+(i-n**2))
    else:
        for i in range(N):
            if i < n**2 + n:
                arr_to_board_map[i] = (n - i%(n+1), i//(n+1))
            else:
                arr_to_board_map[i] = (n, i-n**2)
    return arr_to_board_map

def mapping_magic2(N):
    n = N//4
    bowl_to_arr_map = [NULL]*N
    for i in range(N):
        if i < n:
            bowl_to_arr_map[i] = (2, n-1-i)
        elif i < n*2:
            bowl_to_arr_map[i] = (1, i%n)
        elif i < n*3:
            bowl_to_arr_map[i] = (0, n-1-(i%n))
        else:
            bowl_to_arr_map[i] = (3, i%n)
    return bowl_to_arr_map

def reverse_mapping_magic2(N):
    arr_to_board_map = [NULL]*N
    for i in range(N):
        arr_to_board_map[i] = (3-i%4, i//4)
    return arr_to_board_map

def add_to_min_bowls():
    min_fish, bowl_idxs = INF, []
    for i in range(N):
        if bowls[i] < min_fish:
            min_fish = bowls[i]
            bowl_idxs = [i]
        elif bowls[i] == min_fish:
            bowl_idxs.append(i)
    for idx in bowl_idxs:
        bowls[idx] += 1

def magic1(bowls):
    arr = convert_to_array_magic1(bowls)
    spread(arr)
    return convert_to_bowls_magic1(arr)
    

def convert_to_array_magic1(bowls):
    n = floor(sqrt(N))
    if N < n**2 + n:
        n -= 1

    if N == n**2:
        arr = [[NULL]*n for _ in range(n)]
    else:
        arr = [[NULL]*(N-n**2) for _ in range(n+1)]
    for i in range(N):
        r, c = magic1_bowl_to_array_map[i]
        arr[r][c] = bowls[i]
    return arr

def spread(arr):
    R, C = len(arr), len(arr[0])
    spread_amount = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if nr<0 or nr>=R or nc<0 or nc>=C or arr[nr][nc] == NULL:
                    continue
                if arr[r][c] > arr[nr][nc]:
                    amount = (arr[r][c] - arr[nr][nc]) // 5
                    spread_amount[r][c] -= amount
                    spread_amount[nr][nc] += amount
    for r in range(R):
        for c in range(C):
            arr[r][c] += spread_amount[r][c]
            
def convert_to_bowls_magic1(arr):
    bowls = [NULL]*N
    for i in range(N):
        r, c = magic1_array_to_bowl_map[i]
        bowls[i] = arr[r][c]
    return bowls
                
def magic2(bowls):
    arr = convert_to_array_magic2(bowls)
    spread(arr)
    return convert_to_bowls_magic2(arr)

def convert_to_array_magic2(bowls):
    n = N // 4
    arr = [[NULL]*n for _ in range(4)]
    for i in range(N):
        r, c = magic2_bowl_to_array_map[i]
        arr[r][c] = bowls[i]
    return arr

def convert_to_bowls_magic2(arr):
    bowls = [NULL]*N
    for i in range(N):
        r, c = magic2_array_to_bowl_map[i]
        bowls[i] = arr[r][c]
    return bowls
    
magic1_bowl_to_array_map = mapping_magic1(N)
magic2_bowl_to_array_map = mapping_magic2(N)
magic1_array_to_bowl_map = reverse_mapping_magic1(N)
magic2_array_to_bowl_map = reverse_mapping_magic2(N)

time = 0
while True:
    if max(bowls) - min(bowls) <= K:
        print(time)
        break
    add_to_min_bowls()
    bowls = magic1(bowls)
    bowls = magic2(bowls)
    time += 1