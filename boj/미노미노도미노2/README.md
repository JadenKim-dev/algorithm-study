### 사용한 알고리즘/자료구조

문제에서 제시한 조건을 구현하는 문제이다.  
각각의 board의 경우에는 green은 각 열을 stack의 형태로 저장하고, blue는 각 행을 stack의 형태로 저장한다.  
stack의 앞 인덱스는 바닥 부분(board의 경계선)이고, 뒷 인덱스는 천장 부분(연한 부분에 가까운 쪽)이다.

총 3개의 메서드를 정의해서 사용했다.  
delete_line_if_full(board, idx)은 idx번째 줄이 block으로 꽉 찼는지를 확인하고, 찼을 경우 해당 라인을 제거한다.  
delete_innermost_line(board, num)은 연한 부분에 블럭이 침범할 경우 호출되는 메서드로, num 개수만큼 가장 바닥쪽의 라인을 제거한다
clear_board(board)는 해당 board(blue/green)을 정리하는 메서드이다.  
천장 부분의 block이 delete_line_if_full에 의해서 사라졌을 때 그 아래에 있는 빈칸들을 제거한다.

한 줄이 block으로 꽉 차거나, 연한 부분에 block이 침범하는 경우는 새롭게 block이 추가된 부분에서만 발생할 수 있다.  
해당 부분만 검사가 이루어지도록 delete_line_if_full, delete_innermost_line를 사용하면 된다.
