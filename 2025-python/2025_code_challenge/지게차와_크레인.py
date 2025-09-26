# 모든 행/열을 순회하면서 진행해도 `50*50*100=250,000` 으로 순회 회수가 작기 때문에, 브루트 포스로 진행
# 단 requests를 순회할 때에는 매번 storage를 깊은 복사해서, 이번 회차에 지게차 제거를 수행한 결과가 다음 셀의 제거 여부에 영향을 주지 않도록 해야 함
# 크레인 요청일 때에는 복사 안 해도 괜찮을 듯
from collections import deque

def solution(storage, requests):
    OUTER = 'OUT'
    BLANK = 'BLK'
    DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n = len(storage)
    m = len(storage[0])
    containers = [[''] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            containers[i][j] = storage[i][j]
    
    def isOuterCell(x, y, board):
        for dx, dy in DIRECTION:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                return True
            if board[nx][ny] == OUTER:
                return True
        return False

    def makeOuter(fx, fy, board):
        board[fx][fy] = OUTER
        queue = deque([(fx, fy)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTION:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if board[nx][ny] == BLANK:
                    board[nx][ny] = OUTER
                    queue.append((nx, ny))

    for request in requests:
        isCraneReq = len(request) == 2
        target = request[0]
        prev_containers = [containers[i][:] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if containers[i][j] != target:
                    continue
                if isOuterCell(i, j, prev_containers):
                    makeOuter(i, j, containers)
                elif isCraneReq:
                    # 이전 기준으로는 아니지만, 현재 작업중인 기준으로는 outer인 경우를 처리
                    if isOuterCell(i, j, containers):
                        makeOuter(i, j, containers)
                    else:
                        containers[i][j] = BLANK

    answer = 0
    for i in range(n):
        for j in range(m):
            answer += 1 if containers[i][j] != BLANK and containers[i][j] != OUTER else 0
    return answer
  
# ---

from collections import deque

def solution(storage, requests):
    OUTER = 'OUT'
    BLANK = 'BLK'
    DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n = len(storage)
    m = len(storage[0])
    containers = [list(row) for row in storage]
    
    def isOuterCell(x, y, board):
        for dx, dy in DIRECTION:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                return True
            if board[nx][ny] == OUTER:
                return True
        return False

    def makeOuter(fx, fy, board):
        board[fx][fy] = OUTER
        queue = deque([(fx, fy)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTION:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if board[nx][ny] == BLANK:
                    board[nx][ny] = OUTER
                    queue.append((nx, ny))

    for request in requests:
        isCraneReq = len(request) == 2
        target = request[0]
        prev_containers = [containers[i][:] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if containers[i][j] != target:
                    continue
                if isOuterCell(i, j, prev_containers):
                    makeOuter(i, j, containers)
                elif isCraneReq:
                    # 이전 기준으로는 아니지만, 현재 작업중인 기준으로는 outer인 경우를 처리
                    if isOuterCell(i, j, containers):
                        makeOuter(i, j, containers)
                    else:
                        containers[i][j] = BLANK

    return sum([col != BLANK and col != OUTER for row in board for col in row])