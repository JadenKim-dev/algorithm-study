import java.util.*;

class Data {
    int x;
    int cb;
    public Data(int x, int cb) {
        this.x = x;
        this.cb = cb;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int MAX = 2 * s + 1;
        int[][] dist= new int [MAX][MAX];   // [x][cb]

        int ans = Integer.MAX_VALUE;
        Queue<Data> q = new LinkedList<>();
        q.add(new Data(1,0));
        while(!q.isEmpty()) {
            Data d = q.remove();
            int x = d.x;
            int cb = d.cb;
            if(x == s) {
                System.out.println(dist[x][cb]);
                System.exit(0);
            }
            if(dist[x][x]==0) {
                dist[x][x] = dist[x][cb] + 1;
                q.add(new Data(x,x));
            }
            if(x+cb < MAX && dist[x + cb][cb] == 0){
                dist[x + cb][cb] = dist[x][cb] + 1;
                q.add(new Data(x + cb, cb));
            }
            if(x-1 >= 0 && dist[x - 1][cb] == 0) {
                dist[x - 1][cb] = dist[x][cb] + 1;
                q.add(new Data(x - 1, cb));
            }
        }
    }
}