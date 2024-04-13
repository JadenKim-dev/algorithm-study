import java.util.*;

public class Main {
    static int n;
    static ArrayList<Integer>[] a;
    static boolean[] check;
    static Deque<Integer> q;
    static boolean[] isCycle;
    static int[] dist;
    static boolean getCycle(int x, int prev) {
        if(check[x]) {    // 한바퀴 돌아서 원래 점으로 돌아왔을 경우 -> 사이클을 찾은 것
            boolean cycle = false;
            while(!q.isEmpty()) {
                int k = q.removeFirst();
                if(!cycle) {
                    if(k == x) {   // x부터는 사이클 시작
                        cycle = true;
                        isCycle[k] = true;
                    }
                } else {
                    isCycle[k] = true;
                }
            }
            return true;
        }
        check[x] = true;
        q.addLast(x);
        for(int i=0; i<a[x].size(); i++) {
            int next = a[x].get(i);
            if(next == prev) continue;
            if(getCycle(next, x)) {
                return true;
            }
            check[next] = false;   // 다른 점을 순회하는데 앞서
            q.removeLast();        // getCycle(next, x)로 인한 side effect를 원복
        }
        return false;
    }

    static void getDist(int x, int prev, int cnt) {
        dist[x] = cnt;
        for (int i = 0; i < a[x].size(); i++) {
            int next = a[x].get(i);
            if(!isCycle[next] && next != prev) {
                getDist(next, x, cnt+1);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        n = sc.nextInt();
        a = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            a[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < n; i++) {
            int from = sc.nextInt();
            int to = sc.nextInt();
            a[from-1].add(to-1);
            a[to-1].add(from-1);
        }
        q = new ArrayDeque<>();
        check = new boolean[n];
        isCycle = new boolean[n];
        for (int i = 0; i < n; i++) {
            if(getCycle(i,-1)) break;
            q = new LinkedList<>();
            check = new boolean[n];
        }
        dist = new int[n];
        for (int i = 0; i < n; i++) {
            if(isCycle[i]) {
                getDist(i, -1, 0);
            }
        }
        for (int i = 0; i < n; i++) {
            sb.append(Integer.toString(dist[i]) + " ");
        }
        System.out.println(sb);
    }
}