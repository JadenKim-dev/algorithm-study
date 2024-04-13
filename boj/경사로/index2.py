from sys import stdin

n, l = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

def is_valid(line):
    cnt = 1
    for i in range(n-1):
        if line[i] == line[i+1]:
            cnt += 1
        elif line[i]+1 == line[i+1]:
            if cnt < l:
                return False
            cnt = 1
        elif line[i]-1 == line[i+1]:
            if cnt < 0:
                return False
            cnt = -l + 1
        else:
            return False
    return False if cnt < 0 else True

print(sum(map(is_valid, board + list(zip(*board)))))