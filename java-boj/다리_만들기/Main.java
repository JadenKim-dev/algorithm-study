import java.util.*;

public class Main {
    static final int[] dx = {1, -1, 0, 0};
    static final int[] dy = {0, 0, 1, -1};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] a = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = sc.nextInt();
            }
        }
        int[][] dist = new int[n][n];
        int[][] name = new int[n][n];
        int ans = Integer.MAX_VALUE;

        // 섬 나누기
        Queue<Integer> q = new LinkedList<>();
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(a[i][j] == 0 || name[i][j] > 0) continue;
                cnt += 1;
                q.add(i); q.add(j);
                name[i][j] = cnt;
                while(!q.isEmpty()) {
                    int x = q.remove();
                    int y = q.remove();
                    for (int k = 0; k < 4; k++) {
                        int nx = x + dx[k];
                        int ny = y + dy[k];
                        if(0 <= nx && nx < n && 0 <= ny && ny < n) {
                            if(a[nx][ny] == 1 && name[nx][ny] == 0) {
                                name[nx][ny] = cnt;
                                q.add(nx); q.add(ny);
                            }
                        }
                    }
                }
            }
        }

        // 섬에 해당하는 점을 모두 q에 넣음
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(a[i][j] == 0) continue;
                q.add(i); q.add(j);
            }
        }

        while(!q.isEmpty()) {
            int x = q.remove();
            int y = q.remove();
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if(0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if(a[nx][ny] == 0){
                        if(dist[nx][ny] > 0) {   // 이미 방문한 바다를 탐색하는 경우
                            if(name[x][y] != name[nx][ny]){   // 다른 섬에서 온 경우
                                ans = ans > dist[x][y] + dist[nx][ny] ? dist[x][y] + dist[nx][ny] : ans;
                            }
                        } else {    // 아직 방문하지 않은 바다를 탐색하는 경우
                            name[nx][ny] = name[x][y];
                            dist[nx][ny] = dist[x][y] + 1;
                            q.add(nx); q.add(ny);
                        }
                    }
                }
            }
        }
        System.out.println(ans);
    }
}