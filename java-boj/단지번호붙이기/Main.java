import java.util.*;

public class Main {
    static int n;
    static boolean[][] check;
    static int[][] house;
    static int count;
    static void dfs(int x, int y) {
        if(check[x][y]) return;
        check[x][y] = true;
        count++;
        if(x > 0 && house[x-1][y] == 1) {
            dfs(x-1, y);     // 위에 집이 있을 경우
        } if(x < n-1 && house[x+1][y] == 1) {
            dfs(x+1, y);     // 아래에 집이 있을 경우
        } if(y > 0 && house[x][y-1] == 1) {
            dfs(x, y-1);     // 왼쪽에 집이 있을 경우
        } if(y < n-1 && house[x][y+1] == 1) {
            dfs(x, y+1);     // 오른쪽에 집이 있을 경우
        } 
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        house = new int [n][n];
        for(int i=0; i<n; i++) {
            String str = sc.next();
            for(int j=0; j<n; j++) {
                house[i][j] = Character.getNumericValue(str.charAt(j));
            }
        }
        ArrayList<Integer> ans = new ArrayList<>();
        check = new boolean[n][n];
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(check[i][j] == false && house[i][j] == 1) {
                    count = 0;
                    dfs(i, j);
                    ans.add(count);
                }
            }
        }
        Collections.sort(ans);
        System.out.println(ans.size());
        for(int i=0; i<ans.size(); i++) {
            System.out.println(ans.get(i));
        }
    }
}