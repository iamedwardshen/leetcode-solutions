import java.util.*;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] num) {
        List<List<Integer>> res = new ArrayList<>();
        if (num == null || num.length < 3) return res;

        Arrays.sort(num);
        Set<List<Integer>> set = new HashSet<>();
        for (int i = 0; i < num.length - 2; i++) {
            int low = i + 1;
            int high = num.length - 1;
            int target = -num[i];
            while (low < high) {
                if (num[low] + num[high] == target) {
                    List<Integer> sol = new ArrayList<>();
                    sol.addAll(Arrays.asList(num[i], num[low], num[high]));
                    if (set.add(sol)) res.add(sol);
                    low++;
                    high--;
                } else if (num[low] + num[high] < target) {
                    low++;
                } else {
                    high--;
                }
            }
        }

        return res;
    }
}
