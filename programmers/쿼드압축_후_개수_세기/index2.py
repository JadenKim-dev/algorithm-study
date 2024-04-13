def solution(arr):
    cnt = [0, 0]
    def check(size, x, y):
        if size > 1:  
            for dx in range(size):
                for dy in range(size):
                    if arr[x+dx][y+dy] != arr[x][y]:
                        check(size//2, x, y)
                        check(size//2, x + size//2, y)
                        check(size//2, x, y + size//2)
                        check(size//2, x + size//2, y + size//2)
                        return
        cnt[arr[x][y]] += 1
    check(len(arr), 0, 0)
    return cnt