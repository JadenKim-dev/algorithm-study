from itertools import combinations as comb
from collections import defaultdict

def solution(infos, queries):
    dict = defaultdict(list)
    for info in infos:
        info = info.split()
        dict_key = info[:-1]
        dict_value = int(info[-1])
        for i in range(5):
            for c in comb(dict_key, i):
                dict[''.join(c)].append(dict_value)
    for key in dict.keys():
        dict[key].sort()
    answer = []
    for q in queries:
        q = [x for x in q.split(" and ")]
        q += q.pop().split()
        target_key = [x for x in q[:-1] if x != '-']
        target = dict[''.join(target_key)]
        if target:
            idx = search(target, int(q[-1]))
            answer.append(len(target) - idx)
        else:
            answer.append(0)
    return answer

def search(array, target):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return mid if array[mid] >= target else mid + 1