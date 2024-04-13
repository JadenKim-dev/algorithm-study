public class Main {
    static int n;
    static int[][] sign;
    static int[] ans;
    static boolean check(int index) {
        int sum = 0;
        for (int i=index; i>=0; i--) {
            sum += ans[i];
            if (sign[i][index] == 0) {
                if (sum != 0) return false;
            } else if (sign[i][index] < 0) {
                if (sum >= 0) return false;
            } else if (sign[i][index] > 0) {
                if (sum <= 0) return false;
            }
        }
        return true;
    }
    static boolean go(int index) {
        if (index == n) {
            return true;
        }
        if (sign[index][index] == 0) {
            ans[index] = 0;
            return check(index) && go(index+1);
        }
        for (int i=1; i<=10; i++) {
            ans[index] = sign[index][index]*i;
            if (check(index) && go(index+1)) {
                return true;
                       // check(index)와 go(index+1)이 
                       // 모두 true가 아니면 계속 루프를 돈다
            } 
        }
        return false;
    }
}