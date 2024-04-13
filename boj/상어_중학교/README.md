### 사용한 알고리즘/자료구조

문제에서 제시한 조건을 구현하는 시뮬레이션 문제이다.  
각 칸의 블록 종류를 2차원 배열로 저장하는 board를 사용했으며,
key로 각 집합의 시작점을 저장하고, value로 해당 집합에 속하는 블록들의 리스트 + 레인보우 블록의 개수를 저장하는 groups 딕셔너리를 사용했다.

get_group_from(sr, sc, visited)는 (sr, sc)를 시작점으로 하는 블록 그룹의 정보를 구하는 메서드이다.  
이를 통해 groups에 저장할 value 값을 구하게 된다.

get_target_blocks_from(groups)은 groups 내에서 이번에 삭제될 그룹을 찾아서, 해당 그룹 안의 블록 리스트를 반환하는 함수이다.  
이를 통해 구한 블록들을 board에서 BLANK로 처리하게 된다.

apply_gravity(board)는 board에 중력을 적용해서 블럭들을 떨어트리는 메서드이다.  
rotate(board) board를 시계 반대방향으로 한 바퀴 회전시킨 블록을 메서드이다.
