# logN으로 연산 복잡도를 제한하기 위해 heap을 사용, 정렬 기준은 소요 시간, 요청 시간, 번호 순 !
# 가장 높은 우선순위 잡을 꺼내서, 이전 종료 시점과 비교, !
#  - 이전 종료 시점 이후에 요청 시간일 경우 시작 시점은 요청 시간 !
#  - 이전 종료 시점 이전에 요청 시간일 경우 시작 시점은 이전 종료 시점 !
# 잡 종료 시 종료 시점을 기록, 요청 부터 종료까지 걸린 시간을 정답 배열에 추가 !
# 잡 종료 시 해당 시점 이후에 요청한 잡을 힙에 추가
# 마지막에 정답 배열의 평균을 정수로 계산해서 반환 !
import heapq
from collections import deque

def solution(jobs):
    queue = deque(sorted([(req_time, duration, i) for i, (req_time, duration) in enumerate(jobs)]))
    heap = []

    return_times = []
    now = 0
    while queue or heap:
        while queue and queue[0][0] <= now:
            req_time, duration, i = queue.popleft()
            heapq.heappush(heap, (duration, req_time, i))
        if not heap:
            now = queue[0][0]
            continue
        duration, req_time, _ = heapq.heappop(heap)
        start_time = max(req_time, now)
        now = start_time + duration
        return_times.append(now - req_time)

    return sum(return_times) // len(return_times)