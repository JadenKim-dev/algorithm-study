# 백준 알고리즘 1248번(맞춰봐) 문제풀이

재귀문을 활용하여, 전체 경우의 수를 확인하는 부르트 포스 문제이다.

이 문제에서는 (i번째 수 ~ j번째 수의 합)의 부호가 주어진다.  
즉 +, -, 0 중의 하나의 기호가 주어진다.  
이 입력값을 n X n 행렬에 저장하는데, +인 경우 1을, -인 경우 -1을, 0인 경우 0을 저장한다.  
(이렇게 저장하면, 1 ~ 10까지만 루프를 돌고, 이 행렬의 값을 곱하는 식의 간결한 표현이 가능하다!)

풀이에는 2개의 함수를 이용한다 - go(int index), check(int index)

`check(int index)`: idx 0 ~ idx index 까지 부분합들이 부호에 맞는지 검사하는 함수이다.  
ans의 해당 index에 적절한 값이 들어갔는지를 확인할 수 있다.

`go(int index)`: index를 0에서 n까지 늘려가며 각 index의 ans 값을 완성시켜 나가는 함수이다.
이 때 각 index에 대해서 1부터 10까지의 값을 순회 돌면서 검사하게 된다.
오답인 경우 계속 false가 반환되며,
정답이 나와서 check(0) ~ check(10) 모두 true가 반환될 때 까지 계속 순회를 돌게 된다.

```java
for (int i=1; i<=10; i++) {
    ans[index] = sign[index][index]*i;
    if (check(index) && go(index+1)) {
        return true;
      // check(index)와 go(index+1)이 모두 true가 아니면 계속 루프를 돈다
    }
}
```

이 때 check(index) && go(index+1)의 조건으로 인해,  
check(index)와 go(index + 1)이 둘 다 true가 될 때까지 루프를 돌게 된다.  
check(0) && go(1)
go(1) -> check(1) && go(2)  
go(2) -> check(2) && go(3)  
go(3) -> check(3) && go(4)  
위와 같이 재귀문이 엮어 있기 때문에, 모든 index에 대해서 check를 통과한 경우에만  
true가 반환되어 재귀문이 끝날 수 있다.

최종 코드는 아래와 같다.
