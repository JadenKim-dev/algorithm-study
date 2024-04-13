from sys import stdin
NULL = 0
IMPOSSIBLE = -1
MAX = 1000

readints = lambda: map(int, stdin.readline().split())
n, m, k = readints()
board = [list(readints()) for _ in range(n)]
sharks = {}
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            sharks[board[i][j]] = (i, j)
            board[i][j] = (board[i][j], 0)
dirs = [NULL] + list(readints())
priorities = [NULL]
for i in range(1, m+1):
    priorities.append([NULL] + [list(readints()) for _ in range(4)])
is_conquered = [False]*(m+1)

dx = [NULL, -1, 1, 0, 0]
dy = [NULL, 0, 0, -1, 1]
def get_conquest_time():
    for second in range(1, MAX+1):
        destinations = [NULL] * (m+1)
        for s_idx in range(1, m+1):
            if is_conquered[s_idx]:
                continue
            dir = dirs[s_idx]
            priority = priorities[s_idx][dir]
            x, y = sharks[s_idx]
            is_moved = False
            my_smell_dir = NULL
            for i in range(4):
                j = priority[i]
                nx, ny = x+dx[j], y+dy[j]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if board[nx][ny] == 0 or board[nx][ny][1] < second-k:         
                    destinations[s_idx] = (nx, ny, j)
                    is_moved = True
                    break
                elif my_smell_dir == NULL and board[nx][ny][0] == s_idx:
                    my_smell_dir = j

            if not is_moved:
                nx, ny = x+dx[my_smell_dir], y+dy[my_smell_dir]
                destinations[s_idx] = (nx, ny, my_smell_dir)
        for s_idx in range(1, m+1):
            if is_conquered[s_idx]:
                continue
            nx, ny, d = destinations[s_idx]
            sharks[s_idx] = (nx, ny)
            board[nx][ny] = (s_idx, second)
            dirs[s_idx] = d
            for s_idx2 in range(s_idx+1, m+1):
                if is_conquered[s_idx2]:
                    continue
                nx2, ny2, _ = destinations[s_idx2]
                if nx == nx2 and ny == ny2:
                    is_conquered[s_idx2] = True
        if sum(is_conquered) == m-1:
            return second
            
    return IMPOSSIBLE

print(get_conquest_time())