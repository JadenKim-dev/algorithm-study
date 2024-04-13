from functools import reduce
OUTER = -1; GROOVE = 0; SWELL = 1


def solution(key, lock):
    M, N = len(key), len(lock)
    groove_cnt = reduce(lambda a, b: a + b.count(GROOVE), lock, 0)
    print(groove_cnt)
    board = [[OUTER]*(N*3) for _ in range(N*3)]
    for r in range(N):
        for c in range(N):
            board[N+r][N+c] = lock[r][c]

    def check_from(key, sr, sc):
        curr_grv_cnt = 0
        for dr in range(M):
            for dc in range(M):
                r, c = sr+dr, sc+dc
                if board[r][c] == OUTER:
                    continue
                if key[dr][dc] == GROOVE and board[r][c] == SWELL:
                    continue
                elif key[dr][dc] == SWELL and board[r][c] == GROOVE:
                    curr_grv_cnt += 1
                    continue
                return False
        if curr_grv_cnt == groove_cnt:
            return True
        return False

    def check_90_rotate(key, sr, sc):
        tmp_key = [[0]*M for _ in range(M)]
        for r in range(M):
            for c in range(M):
                tmp_key[c][M-1-r] = key[r][c]
        return check_from(tmp_key, sr, sc)

    def check_180_rotate(key, sr, sc):
        tmp_key = [[0]*M for _ in range(M)]
        for r in range(M):
            for c in range(M):
                tmp_key[M-1-r][M-1-c] = key[r][c]
        return check_from(tmp_key, sr, sc)

    def check_270_rotate(key, sr, sc):
        tmp_key = [[0]*M for _ in range(M)]
        for r in range(M):
            for c in range(M):
                tmp_key[M-1-c][r] = key[r][c]
        return check_from(tmp_key, sr, sc)

    for sr in range(1, 2*N):
        for sc in range(1, 2*N):
            if check_from(key, sr, sc) or check_90_rotate(key, sr, sc) \
                    or check_180_rotate(key, sr, sc) or check_270_rotate(key, sr, sc):
                return True
    return False