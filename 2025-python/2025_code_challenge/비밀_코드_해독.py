# 최대 30인 경우에서 5개를 뽑는 케이스는 17100720 보다 작기  때문에, 전체 케이스를 순회 가능
# 5개를 뽑는 경우를 모두 순회하면서, q와 ans를 순회하면서 모든 경우에 조건을 만족하는지 확인
# 조건을 만족하면 answer를 하나씩 추가하고, 만족하지 않으면 continue
from itertools import combinations

def solution(n, q, ans):
    candidates = list(range(1, n + 1))
    m = len(q)

    answer = 0
    for c in combinations(candidates, r = 5):
        inputs = set(c)

        is_matched = True
        for trys, result in zip(q, ans):
            eq_qnt = 0
            for n in trys:
                if n in inputs:
                    eq_qnt += 1
            if eq_qnt != result:
                is_matched = False
                break
        if is_matched:
            answer += 1
            
    return answer