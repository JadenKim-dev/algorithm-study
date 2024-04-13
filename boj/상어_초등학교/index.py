from sys import stdin
EMPTY = 0; NULL = -1

n = int(stdin.readline())
board = [[EMPTY]*n for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

likeness_list = [NULL] * (n**2 + 1)
for _ in range(n**2):
    data = list(map(int, stdin.readline().split()))
    number, likes = data[0], data[1:]
    likeness_list[number] = likes
    
    dest = (NULL, NULL)
    max_adj_empty = -1
    max_adj_like = -1
    for r in range(n):
        for c in range(n):
            if board[r][c] != EMPTY:
                continue
            adj_empty = 0
            adj_like = 0
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if nr<0 or nr>=n or nc<0 or nc>=n:
                    continue
                if board[nr][nc] == EMPTY:
                    adj_empty += 1
                elif board[nr][nc] in likes:
                    adj_like += 1
            if adj_like > max_adj_like:
                max_adj_like = adj_like
                max_adj_empty = adj_empty
                dest = (r, c)
            elif adj_like == max_adj_like and adj_empty > max_adj_empty:
                max_adj_empty = adj_empty
                dest = (r, c)
    dest_r, dest_c = dest
    board[dest_r][dest_c] = number

total_satisfaction = 0
satisfac_list = [0, 1, 10, 100, 1000]
for r in range(n):
    for c in range(n):
        likes = likeness_list[board[r][c]]
        like_cnt = 0
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=n or nc<0 or nc>=n:
                continue
            if board[nr][nc] in likes:
                like_cnt += 1
                
        total_satisfaction += satisfac_list[like_cnt]
        
print(total_satisfaction)