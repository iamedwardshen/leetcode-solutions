public class ClimbingStairs {
    public int climbStairs(int n) {
        if (n <= 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        }
        int total = 0;
        int first = 1;
        int second = 2;
        for (int i = 2; i < n; i++) {
            total = first + second;
            first = second;
            second = total;
        }

        return total;
    }
}
