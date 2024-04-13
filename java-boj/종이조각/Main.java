import java.io.IOException;
import java.util.Scanner;

public class Main {
    static int n;
    static int m;
    static int[][] a;
    static int[] direction;  // 0, 1로 가로방향인지 세로방향인지 기록
    static boolean[] check;

    /** 가로방향의 데이터를 만났을 때, 해당 조각의 sum을 구함 */
    static int getHorizontalSum(int index) {
        int row = index / m;
        int col = index % m;
        int sum = 0;
        int count = 0;
        for(int i=col; i<m; i++) {
            if(check[index] || direction[index] == 1) break;
            count += 1;
            check[index] = true;
            index++;
        }
        for(int i=count-1; i>=0; i--) {
            sum += Math.pow(10, i) * a[row][col];
            col++;
        }
        return sum;
    }

    /** 세로방향의 데이터를 만났을 때, 해당 조각의 sum을 구함 */
    static int getVerticalSum(int index) {
        int row = index / m;
        int col = index % m;
        int sum = 0;
        int count = 0;
        for(int i=row; i<n; i++) {
            if(check[index] || direction[index] == 0) break;
            count += 1;
            check[index] = true;
            index += m;
        }
        for(int i=count-1; i>=0; i--) {
            sum += Math.pow(10, i) * a[row][col];
            row++;
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        a = new int[n][m];
        for (int i = 0; i < n; i++) {
            String tmp = sc.next();
            for (int j = 0; j < m; j++) {
                a[i][j] = Character.getNumericValue(tmp.charAt(j));
            }
        }
        int ans = 0;
        direction = new int[n * m];
        for (int i = 0; i < (1 << n * m); i++) {
            for(int j=1; j<=n*m; j++) {
                if((i & (1<<(j-1))) == 0) direction[j-1] = 0;  // 0: 가로방향
                else direction[j-1] = 1;  // 1: 세로방향
            }
            // check: 이미 sum에 사용한 데이터를 기록하는 배열
            check = new boolean[n * m]; 
            int sum = 0;
            for(int j=0; j<n*m; j++) {
                if(check[j] == true) continue;
                if(direction[j] == 0) sum += getHorizontalSum(j);
                else sum += getVerticalSum(j);
            }
            if(ans < sum) ans = sum;
        }
        System.out.println(ans);
    }
}