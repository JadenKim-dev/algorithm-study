# dp를 사용해서, 각 아이템을 처리할 때 B의 합이 x 일 때 A의 합의 최소값을 누적해가는 식으로 계산
# 새로운 아이템에서는 기존의 dp 원소들에 대해서 값을 A / B 각각 추가할 때 최소값이 어떻게 되는지를 계산
# dp의 크기는 B의 합계 제한 값으로 설정하고, B의 합이 제한 값을 넘어가는 경우는 기록하지 않음
# A의 합의 값을 계산할 때에도, 합 계산 값이 A의 제한을 넘어갈 경우 기록하지 않음

# 이렇게 구성함으로써 A/B의 합 제한을 초과하는 케이스는 자연스럽게 무시하게 됨
# 또한 같은 B의 합을 만드는 케이스에 대해서는 최소의 A 합을 만드는 케이스만 고려하면 됨

def solution(info, n, m):
    INF = int(1e9)
    dp = [INF] * m
    dp[0] = 0
    for a, b in info:
        prev_dp = dp
        dp = [INF] * m
        for i in range(0, m):
            if prev_dp[i] == INF:
                continue
            if i + b < m:
                dp[i + b] = min(dp[i + b], prev_dp[i])
            if prev_dp[i] + a < n:
                dp[i] = min(dp[i], prev_dp[i] + a)
    answer = min(dp)
    return answer if answer != INF else -1
