from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    OUTER = 0
    OUTLINE = 1
    INNER = 2
    ground = [[OUTER] * 101 for _ in range(101)]
    
    for lx, ly, rx, ry in rectangle:
        for x in range(2*lx, 2*rx+1):
            ground[x][2*ly] = ground[x][2*ry] = OUTLINE
        for y in range(2*ly, 2*ry+1):
            ground[2*lx][y] = ground[2*rx][y] = OUTLINE
    print(ground[6][8])

    for lx, ly, rx, ry in rectangle:
        for x in range(2*lx+1, 2*rx):
            for y in range(2*ly+1, 2*ry):
                ground[x][y] = INNER
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    TARGET = (characterX*2, characterY*2)
    visited = set([TARGET])
    queue = deque([(TARGET[0], TARGET[1], 0)])
    
    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in visited:
                continue
            if not (0 <= nx < 101 and 0 <= ny < 101):
                continue
            if ground[nx][ny] != OUTLINE:
                continue
            if (nx, ny) == TARGET:
                return (d+1) // 2
            visited.add((nx, ny))
            queue.append((nx, ny, d+1))
