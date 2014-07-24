import java.util.*;

public class Anagrams {
    private String sorted(String str) {
        char[] content = str.toCharArray();
        Arrays.sort(content);
        return new String(content);
    }

    public List<String> anagrams(String[] strs) {
        List<String> result = new ArrayList<String>();
        if (strs == null) {
            return result;
        }
        Map<String, ArrayList<String> map = new HashMap<String, ArrayList<String>>()
        for (String str : strs) {
            String sorted = sorted(str);
            if (!map.containsKey(sorted)) {
                map.put(sorted, new ArrayList<String>());
            }
            map.get(sorted).add(str);
        }

        for (ArrayList<String> value : map.values()) {
            if (value.size() > 1) result.addAll(value);
        }

        return result;
    }
}
