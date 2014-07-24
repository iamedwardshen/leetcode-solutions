public class singleNumber {
    public int singleNumber(int[] A) {
        if (A == null) {
            return 0;
        }
        int result = 0;
        for (int a : A) {
            result ^= a;
        }
        return result;
    }
}
