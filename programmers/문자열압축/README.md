틀린 테스트 케이스 :
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa -> 100a

중복된 단위 문자를 발견할 때마다 count를 1씩 증가시켰다.  
따라서 a가 100개 중복된 상황에서 count=99였다.  
이 때 제대로 자리수를 계산하기 위해서는 figure(count+1)로 함수를 호출해야 한다.  
figure(count)로 하게 되면 10, 100, 1000 등 분기점에서 1 낮은 값으로 계산된다.
