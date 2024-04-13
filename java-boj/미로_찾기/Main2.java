import java.util.*;

public class Main2 {
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