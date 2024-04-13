### 사용한 알고리즘/자료구조

문제에서 제시한 조건을 구현하는 시뮬레이션 문제이다.

각 칸에 존재하는 물고기의 수를 저장하기 위해 $4 \times 4 \times 8$ 크기의 fishes 3차원 리스트를 사용했다.  
fishes[r][c][d]는 (r, c) 위치에 있는 d 방향을 바라보고 있는 물고기의 수를 뜻한다.  
물고기는 최대 100만 마리까지 존재할 수 있기 때문에,
물고기를 개별적으로 처리하는 대신, 방향 별로 묶어서 처리해야 한다.

```python
for _ in range(S):
    fishes_prev = fishes
    fishes = fishes_move_from(fishes)

    max_fish_sum, max_route = -1, []
    shark_move(sr, sc, 0, [])
    eat_fishes_at(max_route)
    sr, sc = max_route[-1]

    smell_decrease()

    fishes_copy_from(fishes_prev)
```

fishes_move_from(fishes) 메서드는 fishes에 담긴 물고기가 이동을 마쳤을 때 이동한 결과를 fishes와 동일한 형태로 반환한다.

shark_move(r, c, fish_sum, route) 메서드는 물고기를 가장 많이 잡아먹는 상어의 이동 경로를 찾기 위한 재귀 메서드이다.  
dfs를 사용하고 전역변수인 max_fish_sum을 업데이트 해가며 최적의 경로를 찾게 된다.

eat_fishes_at(route) 메서드는 route에 포함되어 있는 위치를 이동하며 물고기를 잡아먹는 메서드이다.  
fishes에 저장되어 있는 물고기 정보를 삭제하고, 물고기의 냄새를 남긴다.

smell_decrease()는 전체 위치의 냄새를 1씩 감소시킨다.

fishes_copy_from(fishes_prev)는 이동 전의 생선 상태인 fishes_prev를 참고하여, 해당 물고기들을 fishes에 추가하는 메서드이다.
