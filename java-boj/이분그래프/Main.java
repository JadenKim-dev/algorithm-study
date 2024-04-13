import java.util.*;

public class Main {
    static int n, m; 
    static int[] group;  // 아직 그룹에 포함되어 있지 않으면 0, 각 이분그래프 그룹은 1, -1
    static ArrayList<Integer>[] a;
    static boolean bfs(int start) {
        group[start] = 1;
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        while(!q.isEmpty()) {
            int x = q.poll();
            for(int i=0; i<a[x].size(); i++){
                int y = a[x].get(i);
                if(group[y] == 0) {
                    group[y] = -1 * group[x];  // x와 y를 다른 이분그래프 그룹에 넣음
                    q.add(y);
                }
                else if(group[y] == group[x]) return false;  // x와 y의 그룹이 일치하면 false 반환
            }
        }
        return true;  // 탐색 과정에서 이상이 발견되지 않았으면 true 반환
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        while(k-- > 0) {
            n = sc.nextInt();
            m = sc.nextInt();
            a = new ArrayList[n + 1];
            for(int i=1; i<=n; i++) {
                a[i] = new ArrayList<Integer>();
            }
            group = new int[n+1];
            for(int i=0; i<m; i++) {
                int from = sc.nextInt();
                int to = sc.nextInt();
                a[from].add(to);
                a[to].add(from);
            }
            boolean ans = true;
            for(int i=1; i<=n; i++) {
                if(group[i] == 0) ans = ans && bfs(i);
            }  // 각 연결요소에 대해서 너비우선탐색 시행, 모든 연결요소에서 true가 반환되어야 ans==true가 됨 
            if(ans) sb.append("YES\n");
            else sb.append("NO\n");
        }
        System.out.println(sb);
    }
}