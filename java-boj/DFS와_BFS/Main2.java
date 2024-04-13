import java.util.*;

public class Main {
    static int n, m, v;
    static boolean[] check;
    static ArrayList<Integer>[] a;
    static StringBuilder sb1 = new StringBuilder();  // dfs의 결과를 저장
    static StringBuilder sb2 = new StringBuilder();  // bfs의 결과를 저장
    static void dfs(int x) {
        check[x] = true;
        sb1.append(Integer.toString(x) + " ");
        for(int i=0; i<a[x].size(); i++) {
            int y = a[x].get(i);
            if(check[y] == false) {
                dfs(y);
            }
        }
    }
    static void bfs(int v) {
        Queue<Integer> q = new LinkedList();
        q.add(v);
        sb2.append(Integer.toString(v) + " ");
        check[v] = true;
        while(!q.isEmpty()) {
            int x = q.poll();
            for(int i=0; i<a[x].size(); i++) {
                int y = a[x].get(i);
                if(check[y] == false) {
                    check[y] = true;
                    sb2.append(Integer.toString(y) + " ");
                    q.add(y);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        v = sc.nextInt();
        a = new ArrayList[n+1];
        for(int i=1; i<=n; i++) {
            a[i] = new ArrayList<Integer>();
        }

        for(int i=0; i<m; i++) {
            int from = sc.nextInt();
            int to = sc.nextInt();
            a[from].add(to);
            a[to].add(from);
        }
        for(int i=1; i<=n; i++) {
            Collections.sort(a[i]);  // 정점번호가 작은 것부터 방문하기 위해,
        }                            // 각각의 정점에 대한 ArrayList를 정렬했다.
        check = new boolean[n+1];
        dfs(v);
        check = new boolean[n+1];
        bfs(v);
        System.out.println(sb1);
        System.out.println(sb2);
    }
}