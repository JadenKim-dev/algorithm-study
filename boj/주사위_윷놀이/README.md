### 사용한 알고리즘/자료구조

문제에서 제시한 조건을 구현하는 문제이다.  
각 말의 위치 정보를 담는 pieces 배열과 각 말이 도착 칸에 도달했는지를 저장하는 is_goal_in 배열을 사용했다.  
재귀함수를 통해 가능한 모든 경우를 확인하게 했다.

10, 20, 30에 도달할 경우 이동하게 되는 루트를 routes에 각각 작성했다.  
해당 값에 도달할 경우 route를 갈아타면 된다.

change_route_if_necessary(blue, red)는 루트를 바꿀 경우 이를 변환한 인덱스를, 그렇지 않을 경우 원래의 인덱스를 반환한다.  
side effect가 존재하지 않게 설계하여, pieces에 해당 함수의 반환 값을 적용하는 코드는 재귀함수 play()에 작성했다.

is_already_exists_destination(blue, red, p_idx, pieces, is_goal_in)은 p_idx, pieces, is_goal_in의 정보를 확인하여 blue, red 위치에 이미 말이 있는지를 확인하는 메서드이다.
