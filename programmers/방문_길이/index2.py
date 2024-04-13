def solution(dirs):
    visited = set()
    dx = {'L':0, 'R':0, 'U':1, 'D':-1}
    dy = {'L':-1, 'R':1, 'U':0, 'D':0}
    x, y = 0, 0
    for dir in dirs:
        nx, ny = x+dx[dir], y+dy[dir]
        if nx<-5 or nx>5 or ny<-5 or ny>5:
            continue
        visited.add((x, y, nx, ny))
        visited.add((nx, ny, x, y))
        x, y = nx, ny
    return len(visited) // 2