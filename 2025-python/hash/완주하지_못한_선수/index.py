def solution(participant, completion):
    notCompletedCnt = {}
    for p in participant:
        notCompletedCnt[p] = notCompletedCnt[p] + 1 if (p in notCompletedCnt) else 1
    for c in completion:
        notCompletedCnt[c] -= 1
    return list(filter(lambda x: notCompletedCnt[x] > 0 , participant))[0]

# --------------------------------

from collections import Counter

def solution(participant, completion):
    notCompletedCnt = Counter(participant) - Counter(completion)
    return list(notCompletedCnt.keys())[0]

# --------------------------------

from collections import defaultdict

def solution(participant, completion):
    notCompletedCnt = defaultdict(int)
    for p in participant:
        notCompletedCnt[p] += 1
    for c in completion:
        notCompletedCnt[c] -= 1
    return [p for p in notCompletedCnt if notCompletedCnt[p] > 0][0]
