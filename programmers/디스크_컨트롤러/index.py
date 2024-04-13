import heapq
from collections import deque

def solution(jobs):
    jobs_q = deque(sorted(jobs))
    heap = []
    now, response_time_sum = 0, 0
    while True:
        while jobs_q and jobs_q[0][0] <= now:
            heapq.heappush(heap, jobs_q.popleft()[::-1])
        if not heap:
            if not jobs_q:
                break
            start, duration = jobs_q.popleft()
            now = start
            heapq.heappush(heap, [duration, start])
        
        duration, start = heapq.heappop(heap)
        now += duration
        response_time_sum += (now - start)
    return process_time_sum // len(jobs)