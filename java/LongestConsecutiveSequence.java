public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] num) {
        if (num == null) {
            return 0;
        }

        Set<Integer> set = new HashSet<Integer>();
        for (int n : num) {
            set.add(n);
        }

        int maxl = 1;
        for (int n : num) {
            int low = n - 1;
            int high = n + 1;
            int count = 1;

            while (set.contains(low)) {
                set.remove(low);
                low--;
                count++;
            }

            while (set.contains(high)) {
                set.remove(high);
                high++;
                count++;
            }
            maxl = Math.max(maxl, count);
        }

        return maxl;
    }
}
