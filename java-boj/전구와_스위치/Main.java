public class Main {
    // 첫번째 원소에서의 선택
    static int flipZero(int cnt, int[] cur, int[] target){
        if(cur[0] == target[0]) {   // 0번째 전구가 목표 상태와 일치하는 경우
            if(cnt == 0) {
                return 0;    // cnt == 0  →  아무 스위치도 누르지 않음
            }
            else {
                cur[2] = 1 - cur[2];   
                return 2;    //  cnt == 1  →  크기 2 스위치, 크기 3 스위치 둘다 누름
            }
        }
        else{    // 목표 상태와 일치하지 않는 경우
            cur[0] = 1-cur[0];
            cur[1] = 1-cur[1];  // cnt == 0  →  크기 2 스위치 누름
            if(cnt > 0) {
                cur[2] = 1-cur[2];    // cnt == 1  →  크기 3 스위치 누름
            }
            return 1;
        }
    }
    static void flip(int x, int[] cur) {
        cur[x] = 1 - cur[x];
        cur[x+1] = 1 - cur[x+1];
        if(x < cur.length-2) cur[x+2] = 1 - cur[x+2];   // (n-2)번째 스위치는 전구 2개만 변경
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] now = new int[n];
        int[] target = new int[n];
        String s = sc.next();
        for (int i = 0; i < n; i++) {
            now[i] = s.charAt(i) - '0';
        }
        s = sc.next();
        for (int i = 0; i < n; i++) {
            target[i] = s.charAt(i) - '0';
        }

        int[] ans = new int[2];
        for(int c = 0; c<=1; c++) {   // cnt==0, cnt==1 로 2번 순회
            if(c==1 && n==2) {
                ans[1] = -1;     // 전구 수가 2개 이면 cnt==0만 수행후 종료
                break;
            }
            int[] cur = Arrays.copyOf(now, n);
            int result = 0;
            for (int i = 0; i < n - 1; i++) {
                if(i == 0) {
                    result += flipZero(c, cur, target);
                }
                else if(cur[i] != target[i]) {
                    flip(i, cur);
                    result++;
                }
            }
            if(cur[n-1] != target[n-1]) result = -1;
            ans[c] = result;
        }
        if(ans[0] == -1 || ans[1] == -1) {
            if(ans[0] == ans[1]) System.out.println(-1);
            else System.out.println(Math.max(ans[0], ans[1]));
            System.exit(0);
        }
        System.out.println(Math.min(ans[0], ans[1]));
    }
}