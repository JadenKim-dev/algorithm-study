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