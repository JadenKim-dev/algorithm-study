class Pair implements Comparable<Pair>{
    int v, d;
    public Pair(int v, int d)  {
        this.v = v;
        this.d = d;
    }
    public int compareTo(Pair that) {
        if(this.v > that.v) return -1;       // 날짜 기준 내림차순
        else if(this.v == that.v) return 0;
        else return 1;
    }
}

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer>[] a = new ArrayList[10001];
        for (int i = 1; i < 10001; i++) {
            a[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            int v = sc.nextInt();
            int d = sc.nextInt();
            a[d].add(v);    // arrayList에 입력
        }
        int cur = 10000;   // cur==10000부터 순회
        long ans = 0;
        PriorityQueue<Integer> q = new PriorityQueue<>();
        while(cur > 0) {
            if(!a[cur].isEmpty()) {
                for (Integer x : a[cur]) {
                    q.add(-x);   // 오늘부터 강의가 가능한 강연들의 강연료 저장
                }
            }
            if(!q.isEmpty()) {
                ans += -q.remove();   // 오늘 할 수 있는 최고가의 강의를 구함
            }
            cur--;
        }
        System.out.println(ans);
    }
}