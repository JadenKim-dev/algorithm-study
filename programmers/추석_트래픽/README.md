### 사용한 알고리즘/자료구조

문제에서 제시한 조건을 구현하는 문제이다.

날짜를 파싱해야 하기 때문에, datetime 라이브러리를 사용했다.  
datetime. strptime(time, "format") 은 format 형태로 작성된 time이라는 문자열을 datetime으로 파싱하는 메서드이다.  
날짜는 모든 데이터가 동일하기 때문에, 시/분/초 부분만 파싱하도록 작성했다.

또한 datetime에 시간을 더하거나 빼는 등의 연산을 하기 위해서 datetime.timedelta를 사용했다.
