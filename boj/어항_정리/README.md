### 사용한 알고리즘/자료구조

문제에서 제시한 조건을 구현하는 시뮬레이션 문제이다.
각각의 어항에 담긴 물고기 수를 저장하는 bowls 리스트를 사용했다.

```python
magic1_bowl_to_array_map = mapping_magic1(N)
magic2_bowl_to_array_map = mapping_magic2(N)
magic1_array_to_bowl_map = reverse_mapping_magic1(N)
magic2_array_to_bowl_map = reverse_mapping_magic2(N)
```

풀이에 앞서 첫번째 마법, 두번째 마법에 의해서 일어나는 변화를 매핑으로 저장했다.
bowl_to_array_map은 공중 부양에 의해서 bowls의 어항들이 2차원 리스트로 어떻게 매핑되는지를 저장한다.
array_to_bowl_map은 어항 간 물고기 이동이 끝난후 어항을 바닥에 되돌려 놓을 때 bowls의 어항 위치가 2차원 리스트의 어느 위치에 매핑되는지를 저장한다.
이들을 구하기 위한 메서드를 각각 정의했다.
이 때 마법에 의해 매핑되는 정보는 어항의 개수 N에 의해 정해진다.
따라서 처음에 한 번만 계산하고 저장해서 사용하면 된다.

mapping_magic1(N)은 어항의 개수가 N개일 때의 첫번째 공중부양의 매핑을 구한다.
이 때 경우의 수를 2개로 나누어야 한다.
$n = \sqrt N$ 일 때, $n^2 <= N <n^2+n$인 경우에는 정사각형 모양에 마지막 행에서 일부 칸이 튀어나온 형태로 매핑된다.
ex) N = 40
![](https://images.velog.io/images/jadenkim5179/post/55ccccbf-79c6-48c6-83fb-be6f0cc8ceb9/40%20%EC%98%88%EC%8B%9C.png)
이와 달리, $N<=n^2+n$인 경우에는 정사각형 밑에 한 행이 추가되는 형태로 매핑된다.
ex) N = 44
![](https://images.velog.io/images/jadenkim5179/post/5a43a8ce-8f60-42ab-b2b6-8dc2baff0258/44%EC%98%88%EC%8B%9C.png)

이러한 특성을 고려하여 인덱싱하면 된다.

```python
def mapping_magic1(N):
    bowl_to_arr_map = [NULL]*N
    n = floor(sqrt(N))
    dist = [n-1]
    for i in range(2*n-1, 1, -1):
        dist.append(i//2)

    if n**2 <= N < n**2 + n:
        for i in range(N-1, -1, -1):
            if i >= n**2:
                bowl_to_arr_map[i] = (n-1, n+i-n**2)
            elif i == n**2 - 1:
                now, dist_idx = 1, 0
                r, c, d = n-1, n-1, 3
                bowl_to_arr_map[i] = (r, c)
            else:
                r, c = r+dr[d], c+dc[d]
                bowl_to_arr_map[i] = (r, c)
                now += 1
                if now > dist[dist_idx]:
                    now = 1
                    dist_idx += 1
                    d = (d+1)%4
    elif N >= n**2 + n:
        for i in range(N-1, -1, -1):
            if i >= n**2:
                bowl_to_arr_map[i] = (n, i-n**2)
            elif i == n**2 - 1:
                now, dist_idx = 1, 0
                r, c = n-1, 0
                d = 0
                bowl_to_arr_map[i] = (r, c)
            else:
                r, c = r+dr[d], c+dc[d]
                bowl_to_arr_map[i] = (r, c)
                now += 1
                if now > dist[dist_idx]:
                    now = 1
                    dist_idx += 1
                    d = (d+1)%4

    return bowl_to_arr_map
```

매핑 한 이후에는 이를 이용하여 문제의 조건대로 적용시키면 된다.

```python
time = 0
while True:
    if max(bowls) - min(bowls) <= K:
        print(time)
        break
    add_to_min_bowls()
    bowls = magic1(bowls)
    bowls = magic2(bowls)
    time += 1
```
