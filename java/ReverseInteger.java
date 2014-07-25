public class ReverseInteger {
    public int reverse(int x) {
        int res = 0;

        while (Math.abs(x) != 0) {
            res = res * 10 + x % 10;
            x = x / 10;
        }

        return res;
    }
}
