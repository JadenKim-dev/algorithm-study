from collections import defaultdict

def solution(dirs):
    visited = defaultdict(bool)
    dx = {'L':0, 'R':0, 'U':1, 'D':-1}
    dy = {'L':-1, 'R':1, 'U':0, 'D':0}
    x, y, answer = 5, 5, 0
    for dir in dirs:
        nx, ny = x+dx[dir], y+dy[dir]
        if nx<0 or nx>10 or ny<0 or ny>10:
            continue
        if not visited[(x, y, nx, ny)] and not visited[(nx, ny, x, y)]:
            answer += 1
        visited[(x, y, nx, ny)] = True
        x, y = nx, ny
    return answer