import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int max = n > k ? n + 1 : 2*k + 1;
        boolean[] check = new boolean[max];
        int[] dist = new int[max];
        int[] prev = new int[max];
        Queue<Integer> q = new LinkedList<>();
        q.add(n);
        check[n] = true;
        prev[n] = -1;
        while(!q.isEmpty()) {
            int x = q.remove();
            if(x == k) {
                System.out.println(dist[k]);
                int[] route = new int[dist[k] + 1];
                int cur = k;
                for (int i=dist[k]; i >=0 ; i--) {
                    route[i] = cur;
                    cur = prev[cur];
                }
                for (int i = 0; i <= dist[k]; i++) {
                    System.out.print(Integer.toString(route[i]) + " ");
                }
                System.exit(0);
            }
            if(x+1 < max && !check[x+1]) {
                q.add(x+1);
                dist[x+1] = dist[x] + 1;
                prev[x+1] = x;
                check[x+1] = true;
            }
            if(x-1 >= 0 && !check[x-1]) {
                q.add(x-1);
                dist[x-1] = dist[x] + 1;
                prev[x-1] = x;
                check[x-1] = true;
            }
            if(2*x < max && !check[2*x]) {
                q.add(2*x);
                dist[2*x] = dist[x] + 1;
                prev[2*x] = x;
                check[2*x] = true;
            }
        }
    }
}