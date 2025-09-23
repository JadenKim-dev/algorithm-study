# 가능한 시간 소요 구간에서, 최소한의 시간을 찾는 이분 탐색을 수행
# mid 시간에서 처리 가능한 최대 인원수를 계산하고, 이를 기준으로 left / right를 좁혀나감
# left >= right가 될 경우 종료
# 최대 처리 가능 인원이 n 보다 크거나 같을 경우, 더 적은 시간으로 처리 가능한지 확인 필요, 따라서 right를 mid로 낮춰야 함
# 최대 처리 가능 인원이 n 보다 작을 경우, 더 큰 시간을 탐색해야 함, 따라서 left를 mid + 1 로 높임

def solution(n, times):
    left = 1
    right = max(times) * n

    while left < right:
        mid = (left + right) // 2
        max_complete = sum([mid // t for t in times])
        if max_complete >= n:
            right = mid
        else:
            left = mid + 1
    
    return left