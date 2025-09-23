# 우선순위 힙을 두 개 활용 -> 하나는 최소 정렬 / 하나는 최대 정렬
# 포함된 원소를 관리하기 위한 별도의 counter 관리
# 원소 삽입 시 -> 두 개의 힙에 원소 추가, counter에 값 추가
# 최대값 제거 시 -> 최대 힙에서 원소 하나 제거, counter에서 값 감소
# 최소값 제거 시 -> 최소 힙에서 원소 하나 제거, counter에서 값 감소
# 마지막에는 counter를 기준으로 최대 / 최소 값 확인

from collections import defaultdict
import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    counter = defaultdict(int)

    for operation in operations:
        op, val = operation.split(' ')
        val = int(val)
        if op == 'I':
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
            counter[val] += 1
        elif op == 'D':
            if val == 1:
                if not max_heap:
                    continue
                num = heapq.heappop(max_heap)
                num = num * -1
                while max_heap and counter[num] == 0:
                    num = heapq.heappop(max_heap)
                    num = num * -1
                if counter[num] > 0:
                    counter[num] -= 1
            else:
                if not min_heap:
                    continue
                num = heapq.heappop(min_heap)
                while min_heap and counter[num] == 0:
                    num = heapq.heappop(min_heap)
                if counter[num] > 0:
                    counter[num] -= 1
    rest_values = [num for num, cnt in counter.items() if cnt > 0]
    min_value = min(rest_values) if len(rest_values) > 0 else 0
    max_value = max(rest_values) if len(rest_values) > 0 else 0
    return [max_value, min_value]
                                
# print(solution(["I 16"]))
# print(solution(["D 1", "D 1"]))
# print(solution(["D -1", "D -1"]))
# print(solution(["D -1", "D 1"]))
# print(solution(["I 16", "I -16", "I 16", "I -16", "D 1", "D 1"]))       
# print(solution(["I 16", "I -16", "I 16", "I -16", "D 1", "D -1"]))
# print(solution(["I 16", "I -16", "I 16", "I -16", "D 1", "D 1", "D 1", "D 1"]))
