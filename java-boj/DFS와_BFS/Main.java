import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
public class Main {
    static int n, m, v;
    static boolean[] check;
    static int[][] a;
    static StringBuilder sb1 = new StringBuilder();  // dfs의 결과를 저장
    static StringBuilder sb2 = new StringBuilder();  // bfs의 결과를 저장

    static void dfs(int x) {
        check[x] = true;
        sb1.append(Integer.toString(x) + " ");
        for(int i=1; i<=n; i++) {
            if(a[x][i] == 1 && check[i] == false) {
                dfs(i);
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
            for(int i=1; i<=n; i++) {
                if(a[x][i] == 1 && check[i] == false) {
                    q.add(i);
                    check[i] = true;
                    sb2.append(Integer.toString(i) + " ");
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        v = sc.nextInt();
        a = new int[n+1][n+1];  // 간선은 1 ~ n이므로, 이에 맞게 저장하기 위해 (n+1) X (n+1)행렬 이용 

        for(int i=0; i<m; i++) {
            int from = sc.nextInt();
            int to = sc.nextInt();
            a[from][to] = 1;
            a[to][from] = 1;
        }
        check = new boolean[n+1];
        dfs(v);
        check = new boolean[n+1];
        bfs(v);
        System.out.println(sb1);
        System.out.println(sb2);
    }
}