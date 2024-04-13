import java.util.*;

class Point {
    int x, y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
public class Main {
    static final int[] dx = {1, 1, 2, 2, -1, -1, -2, -2};
    static final int[] dy = {2, -2, 1, -1, 2, -2, 1, -1};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int t = sc.nextInt();
        while(t-- > 0) {
            int n = sc.nextInt();    // 체스판의 한 변의 길이
            int x = sc.nextInt();    // 시작점 x 좌표
            int y = sc.nextInt();    // 시작점 y 좌표
            int tx = sc.nextInt();   // 목표점 x 좌표
            int ty = sc.nextInt();   // 목표점 y 좌표
            int[][] dist = new int [n][n];
            Queue<Point> q = new LinkedList<>();
            q.add(new Point(x, y));
            while(!q.isEmpty()) {
                Point p = q.poll();
                x = p.x;
                y = p.y;
                if(x==tx && y==ty) break;   // 목표점에 도달했을 경우 탐색 종료
                for(int i=0; i<8; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                        if(dist[nx][ny] == 0) {
                            dist[nx][ny] = dist[x][y] + 1;   // 이전 점에 비해 거리 1 증가
                            q.add(new Point(nx,ny));
                        }
                    }
                }
            }
            sb.append(dist[tx][ty] + "\n");
        }
        System.out.println(sb);
    }
}