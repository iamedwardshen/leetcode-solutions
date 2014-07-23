public class Atoi {
    public int atoi(String str) {
        if (str == null) {
            return 0;
        }

        str = str.trim();
        if (str.length() == 0) {
            return 0;
        }

        int index = 0;
        boolean negative = false;
        if (str.charAt(index) == '-') {
            negative = true;
            index++;
        } else if (str.charAt(index) == '+') {
            index++;
        }

        long result = 0;
        while (index < str.length() && str.charAt(index) >= '0' && str.charAt(index) <= '9') {
            result = result * 10 + (str.charAt(index) - '0');
            index++;
        }

        if (negative) result = -result;
        if (result >= Integer.MAX_VALUE) {
            return Integer.MAX_VALUE;
        } else if (result <= Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        }

        return (int)result;
    }
}
