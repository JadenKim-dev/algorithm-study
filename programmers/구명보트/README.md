https://programmers. co. kr/learn/courses/30/lessons/42885?language=python3

사용한 자료구조/알고리즘
그리디 알고리즘을 구현했고, queue를 사용했다.  
문제에서 주어진 people = [70, 50, 80, 50], limit = 100의 상황에서는 가장 작은 데이터들을 sum이 limit 이하가 되는 단위로 제거하는 게 각 단계에서 최선의 선택이라고 생각했다.

[50, 50] 제거 -> [70] 제거 -> [50] 제거  
=> answer = 3
그러나 people = [50, 50, 1, 1], limit = 51인 경우, 이 알고리즘은 오작동한다

알고리즘 : [1, 1] 제거 -> [50] 제거 -> [50] 제거 => answer = 3
정답 : [1, 50] 제거 -> [1, 50] 제거 => answer = 2
이러한 경우를 고려했을 때, 우선적으로 가장 큰 값을 하나 고르고, 나머지 무게를 people의 가장 작은 값들로 채워나가는 알고리즘이 적절할 것이라고 판단했다.  
이 때 가장 큰 값과 가장 작은 값을 하나씩 삭제해야 하므로, people을 정렬한 데이터를 queue로 변환하여 사용하는 게 적절하다고 판단했다. 이렇게 해야만 작은 데이터는 popleft(), 큰 데이터는 pop()을 통해 제거하여 각각 O(1)에 처리가 가능하다.

코드

```python
from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    answer = 0
    while True:
        sum = 0
        sum += people.pop()
        while people and sum <= limit:
            curr = people.popleft()
            sum += curr
        answer += 1
        if not people and sum <= limit:
            break
        else:
            people.appendleft(curr)
    return answer
```

코드 개선
동일한 greedy 방식을 사용하면서 연산 속도를 개선시킬 수 있는 방법이 있다.  
people의 양 끝 인덱스에서 시작하는 left와 right 변수를 이용하고, 보트에 포함되는 작은 데이터의 개수를 cnt로 세는 방식이다.  
최종적으로는 people의 데이터 개수에서 cnt를 빼주면 전체 보트의 개수를 구할 수 있다.

```python
def solution(people, limit):
    people.sort()
    cnt = 0
    left, right = 0, len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            cnt += 1
        right -= 1
    return len(people) - cnt
```
