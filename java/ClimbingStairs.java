public class ClimbingStairs {
    public int clibmStaris(int n) {
        if (n == 0) return 0;

        int prev = 0;
        int curr = 1;
        for (int i = 1; i < n; i++) {
            int tmp += curr;
            curr += prev;
            prev = tmp;
        }
        return curr;
    }
}
