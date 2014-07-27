import java.util.*;

public class FourSum {
    public List<List<Integer>> fourSum(int[] num, int target) {
        List<List<Integer>> res = new ArrayList<>();
        if (num == null || num.length < 4) return res;
        Arrays.sort(num);

        Set<List<Integer>> set = new HashSet<>();
        for (int i = 0; i < num.length - 3; i++) {
            for (int j = i + 1; j < num.length - 2; j++) {
                int low = j + 1;
                int high = num.length - 1;
                while (low < high) {
                    int sum = num[low] + num[high] + num[i] + num[j];
                    if (sum == target) {
                        List<Integer> sol = new ArrayList<>();
                        sol.addAll(Arrays.asList(num[i], num[j], num[low], num[high]));
                        if (set.add(sol)) res.add(sol);
                        low++;
                        high--;
                    } else if (sum < target) {
                        low++;
                    } else {
                        high--;
                    }
                }
            }
        }

        return res;
    }
}
