from collections import Counter

def solution(people, limit):
    counter = Counter(people)
    weights = sorted(list(counter.keys()), reverse=True)
    answer = 0
    while weights:
        max_weight = weights[0]
        counter[max_weight] -= 1
        if not counter[max_weight]:
            del counter[max_weight]
        weights = sorted(list(counter.keys()), reverse=True)
        answer += 1
        
        if not weights:
            break

        partner = 0
        while partner < len(weights) - 1 and weights[partner] + max_weight > limit:
            partner += 1
        partner_weight = weights[partner]
        if partner_weight + max_weight <= limit:
            counter[partner_weight] -= 1
            if not counter[partner_weight]:
                del counter[partner_weight]
        weights = sorted(list(counter.keys()), reverse=True)

    return answer