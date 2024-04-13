https://programmers.co.kr/learn/courses/30/lessons/17686

## 사용한 알고리즘/자료구조

문제에서 제시한 조건을 구현하는 문제이다.  
주어진 문자열을 조건에 맞게 파싱하고, sorting에 cmp_to_key를 사용하여 comparator 함수를 지정했다.  
이를 통해 복잡한 정렬 규칙을 지정할 수 있다.

## 코드 개선 방향

문자열을 파싱하는데 있어 정규표현식을 사용하면 더 간결하게 코드를 작성할 수 있다.  
re.findall()은 조건에 맞는 문자열을 모두 찾아서 리스트로 반환하고,  
re.split()은 조건의 문자열을 기준으로 target 문자열을 분할한다.
