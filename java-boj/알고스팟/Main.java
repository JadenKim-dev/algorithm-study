import java.util.*;

class Point {
    int x;
    int y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] a = new int[m][n];
        int[][] brk = new int[m][n];
        for (int i = 0; i < m; i++) {
            String str = sc.next();
            for (int j = 0; j < n; j++) {
                a[i][j] = str.charAt(j) - '0';
            }
        }
        for (int i = 0; i < m; i++) {
            Arrays.fill(brk[i], -1);
        }
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(0, 0));
        brk[0][0] = 0;
        while(!q.isEmpty()) {
            Point p = q.remove();
            int x = p.x;
            int y = p.y;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                    if(a[nx][ny] == 1) {
                        if(brk[nx][ny] == -1 || brk[nx][ny] > brk[x][y] + 1) {
                            brk[nx][ny] = brk[x][y] + 1;
                            q.add(new Point(nx, ny));
                        }
                    }
                    if(a[nx][ny] == 0) {
                        if(brk[nx][ny] == -1 || brk[nx][ny] > brk[x][y]) {
                            brk[nx][ny] = brk[x][y];
                            q.add(new Point(nx, ny));
                        }
                    }
                }
            }
        }
        System.out.println(brk[m-1][n-1]);
    }
}