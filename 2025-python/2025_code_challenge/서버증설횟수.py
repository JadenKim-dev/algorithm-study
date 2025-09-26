# players를 하나씩 순회하면서 시뮬레이션
# 현재 보유 수량과 각 자원의 만료 시간을 관리
  # 각 시간에 증설한 서버 수, 만료 시간을 큐에 넣어서 관리
  # 각 시간마다 큐의 맨 앞의 증설 서버의 만료 시간을 체크, 만료되었으면 전체 개수에서 빼기
# 만료된 서버 반납 처리 후, 현재 서버로 사용자를 감당 가능한지 체크하고, 불가능하면 증설 (큐에 추가)
from collections import deque

def solution(players, m, k):
    queue = deque()
    servers = 0
    answer = 0
    for time in range(len(players)):
        if queue:
            n, deadline = queue[0]
            if deadline <= time:
                queue.popleft()
                servers -= n
        if players[time] >= (servers + 1) * m:
            diff = players[time] // m - servers
            queue.append((diff, time + k))
            servers += diff
            answer += diff
    return answer
