def solution(arr):
    n = len(arr)
    compressed = [[False]*n for _ in range(n)]
    cnt = [0, 0]
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            if compressed[i][j]:
                continue
            size = 2
            while check(i, j, n, size, arr):
                size *= 2
            if size > 2:
                compress(i, j, size//2, compressed)
                cnt[arr[i][j]] += 1
            else:
                for x in range(i, i + 2):
                    for y in range(j, j + 2):
                        cnt[arr[x][y]] += 1
    return cnt

def check(x, y, n, size, arr):
    if x%size != 0 or y%size != 0 or x+size > n or y+size > n:
        return False
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != arr[x][y]:
                return False
    return True

def compress(x, y, size, compressed):
    for i in range(x, x + size, 2):
        for j in range(y, y + size, 2):
            compressed[i][j] = True