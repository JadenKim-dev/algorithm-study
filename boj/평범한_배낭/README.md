https://www.acmicpc.net/problem/12865

분류: DP

사용한 알고리즘/자료구조
가장 가치있게 가방을 꾸릴수 있는 물건의 조합을 구하는 문제이다.  
무게를 점점 늘려가면서 결과를 누적시키는 식으로 dynamic programming을 사용하는 것이 적절하다.

backpack[weight][idx]는 최대 weight만큼의 물건을 가방에 채우는데 1 ~ idx까지의 물건만을 사용하여 얻을 수 있는 최대의 무게를 저장한다.  
outer loop에서는 weight를 1에서 k까지 증가시키고, inner loop에서는 idx를 1에서 n까지 증가시키며 결과를 누적한다.

```python
backpack[weight][idx] = max(v + backpack[weight-w][idx-1], backpack[weight][idx-1])
```

위 코드는 idx에 해당하는 물건을 새롭게 추가시킨 경우의 합계 가치와,  
포함하지 않고 idx-1까지의 물건으로만 가방을 꾸렸을 때의 최대 합계 가치를 비교하여,  
더 큰 합계가치를 저장한다.
