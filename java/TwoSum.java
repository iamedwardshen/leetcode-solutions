import java.util.*;

public class TwoSum {
    public int[] twoSum(int[] numbers, int target) {
        int[] result = new int[2];
        if (numbers == null || numbers.length <= 1) {
            return result;
        }

        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < numbers.length; i++) {
            if (!map.containsKey(numbers[i])) {
                map.put(target - numbers[i], i);
            } else {
                result[0] = map.get(numbers[i]) + 1;
                result[1] = i + 1;
            }
        }

        Arrays.sort(result);
        return result;
    }
}
