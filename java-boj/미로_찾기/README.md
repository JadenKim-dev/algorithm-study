# 백준 2178번 - 미로찾기

[https://www.acmicpc.net/problem/2178](https://www.acmicpc.net/problem/2178)

## 로직

최단거리로 도달할 수 있는 거리를 구하는 문제이다.  
처음에는 dfs를 통해 코드를 작성했으나, 시간초과로 실패했다  
(dfs는 재귀함수를 사용해야 하기 때문에 시간과 메모리가 더 많이 필요하다)

결국 bfs방법으로 코드를 작성했다. int의 배열 count[][]를 사용했는데,  
방문하지 않은 점이면 0, 방문한 점이면 해당 점까지의 거리를 저장했다.  
각 점에서 주변의 점들을 탐색하며, count를 1씩 증가시켜 나갔고,  
최종적으로 count[n-1][m-1]값을 출력했다.

## 1) bfs 사용 코드

```java
import java.util.*;

class Point {
    int x, y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static final int[] dx = {0, 0, -1, 1};
    static final int[] dy = {-1, 1, 0, 0};
    static int n, m;
    static int[][] a;
    static int[][] count;  // 아직 탐색하지 않은 곳이면 0, 탐색한 곳이면 (0, 0)으로부터의 거리 입력
    static void dfs() {
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(0, 0));
        count[0][0] = 1;
        while(!q.isEmpty()) {
            Point p = q.poll();
            int x = p.x;
            int y = p.y;
            int cur = count[x][y];
            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if(a[nx][ny] == 1 && count[nx][ny] == 0) {
                        count[nx][ny] = cur + 1;
                        q.add(new Point(nx, ny));
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        a = new int[n][m];
        for(int i=0; i<n; i++) {
            String str = sc.next();
            for(int j=0; j<m; j++) {
                a[i][j] = str.charAt(j) - '0';
            }
        }
        count = new int [n][m];
        dfs();
        System.out.println(count[n-1][m-1]);  // 정답 출력
    }
}
```

## 2) dfs 사용시 코드 - 시간초과

```java
import java.util.*;

public class Main {
    static final int[] dx = {0, 0, -1, 1};
    static final int[] dy = {-1, 1, 0, 0};
    static int n, m;
    static int[][] a;
    static boolean[][] check;
    static int ans = Integer.MAX_VALUE;
    static int cur = 0;
    static void dfs(int x, int y) {
        cur++;
        if(x == n-1 && y == m-1) {
            if(ans > cur) ans = cur;   // 마지막 점에 도착했을 때, ans와 비교하여 값 업데이트
            return;
        }
        check[x][y] = true;
        for(int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (a[nx][ny] == 1 && check[nx][ny] == false) {
                    dfs(nx, ny);
                    check[nx][ny] = false;  // dfs(nx, ny)로 인해 변한 값 복원
                    cur--;  // dfs(nx, ny)로 인해 변한 값 복원
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        a = new int[n][m];
        for(int i=0; i<n; i++) {
            String str = sc.next();
            for(int j=0; j<m; j++) {
                a[i][j] = str.charAt(j) - '0';
            }
        }
        check = new boolean[n][m];
        dfs(0, 0);
        System.out.println(ans);
    }
}
```
