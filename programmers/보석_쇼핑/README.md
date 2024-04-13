### 사용한 알고리즘/자료구조

모든 보석 종류를 포함하면서 가장 짧은 연속된 구간을 찾아내는 구현 문제이다.  
먼저 문제의 시작 부분에서 전체 보석 종류의 개수 n을 len(set(gems))로 구했다.  
모든 보석종류가 포함되었는지 확인할 떄에는 해당 개수가 n과 일치하는지 확인하면 된다.

처음에는 각 위치에서 시작하여, 길이를 점점 늘려가면서 set을 만들어가고 이를 확인하는 식으로 작성했다.  
이 경우에는 모든 효율성 테스트를 통과하지 못했다.

```python
def solution(gems):
    n = len(set(gems))
    min_left, min_right, min_len = -1, -1, INF
    left = 0
    for left in range(len(gems)-n+1):
        curr_gems = set()
        for right in range(left, len(gems)):
            if right-left+1 >= min_len:
                break
            curr_gems.add(gems[right])
            if len(curr_gems) == n:
                min_left, min_right, min_len = left, right, right-left+1
    return [min_left+1, min_right+1]
```

해당 코드의 문제점은, 각 인덱스의 시작 위치에서 매번 새롭게 집합을 만들어가고 있다는 것이었다.  
0번째부터 시작하는 집합과 1번째부터 시작하는 집합은, 0번째 원소의 존재 유무밖에 차이가 나지 않는다.  
따라서 보석의 집합을 재활용할 수 있는 방법을 찾아야 한다.

이를 위해, **앞에 있는 보석을 제거**하고, 이에 해당하는 보석을 **메꾸기 위해 뒤에 있는 보석을 추가**하면서 답을 찾는 아이디어를 떠올렸다.

이 때, 길이를 최단으로 유지하기 위해서는 **앞쪽에 불필요한 보석이 없음이 보장되어야 한다**.  
즉, 뒤에 나온 보석 종류가 맨앞에 등장해 있는 경우가 없어야 한다.  
이를 확인하기 위해서는 **해당 보석이 몇 번 등장했는지의 정보**가 필요했고,  
**defaultdict(int)**를 사용하여 해당 정보를 유지 및 업데이트했다.

```python
from collections import defaultdict


def solution(gems):
    n = len(set(gems))
    left, right = 0, 0
    curr_gems = defaultdict(int)

    for right in range(len(gems)):
        curr_gems[gems[right]] += 1
        if len(curr_gems.keys()) == n:
            break
    left = delete_unnecessary_of(curr_gems, left, gems)

    min_left, min_right, min_len = left, right, right-left+1

    while right < len(gems)-1:
        del curr_gems[gems[left]]
        left += 1

        while len(curr_gems.keys()) < n:
            curr_gems[gems[right+1]] += 1
            right += 1
            if right >= len(gems)-1:
                break

        if len(curr_gems.keys()) == n:
            left = delete_unnecessary_of(curr_gems, left, gems)
            if right-left+1 < min_len:
                min_left, min_right, min_len = left, right, right-left+1

    return [min_left+1, min_right+1]


def delete_unnecessary_of(curr_gems, left, gems):
    while curr_gems[gems[left]] > 1:
        curr_gems[gems[left]] -= 1
        left += 1
    return left
```
