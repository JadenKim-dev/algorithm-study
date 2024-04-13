from sys import stdin

n, l = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
rboard = [list(x) for x in list(zip(*board))]

answer = 0
for i in range(n):
    for d in range(2):
        if d == 0:
            line = board[i]
        else:
            line = rboard[i]
        curr, cnt = line[0], 1
        for j in range(1, n+1):
            if j == n:
                break
            x = line[j]
            if curr == x:
                cnt += 1
            elif abs(curr - x) != 1:
                break
            elif curr < x:
                if cnt < l:
                    break
                curr = x
                cnt = 1
            elif curr > x:
                if cnt < 0:
                    break
                cnt = -l + 1
                curr = x
        if j == n and cnt >= 0:
            answer += 1
print(answer)