https://programmers.co.kr/learn/courses/30/lessons/49994

해당 경로가 방문한 경로인지 확인하기 위해 dictionary를 사용했다.  
defaultdict(bool)을 사용하여 기본값이 False로 저장되게 하고, 해당 경로를 방문한적 있는지를 매 이동시 확인하게 하여 answer를 1씩 증가시킨다.

## 코드 개선 방향

중복을 제거하는데 가장 효과적인 자료구조는 set이다.  
이를 활용하면 코드를 더욱 간단하게 만들 수 있다.
