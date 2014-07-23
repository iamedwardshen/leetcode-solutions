import java.util.*;

public class ThreeSum {
    public static List<List<Integer>> threeSum(int[] num) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (num == null || num.length < 3) {
            return result;
        }

        Arrays.sort(num);
        Set<List<Integer>> set = new HashSet<List<Integer>>(); // skip duplicates.
        for (int i = 0; i < num.length - 2; i++) {
            int low = i + 1;
            int high = num.length - 1;
            int target = -num[i];
            while (low < high) {
                if (num[low] + num[high] == target) {
                    List<Integer> solution = new ArrayList<Integer>();
                    solution.add(num[i]);
                    solution.add(num[low]);
                    solution.add(num[high]);
                    if (set.add(solution)) result.add(solution);
                    low++;
                    high--;
                } else if (num[low] + num[high] < target) {
                    low++;
                } else {
                    high--;
                }
            }
        }

        return result;
    }
}
