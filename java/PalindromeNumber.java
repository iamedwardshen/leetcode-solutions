public class PalindromeNumber {
    private boolean isValid(char c) {
        return Character.isLetter(c) || Character.isDigit(c);
    }

    public boolean isPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return true;
        }

        int low = 0;
        int high = s.length() - 1;
        while (low < high) {
            char left = s.charAt(low);
            char right = s.charAt(high);
            if (!isValid(left)) low++;
            else if (!isValid(right)) high--;
            else if (Character.toLowerCase(left) != Character.toLowerCase(right)) return false;
            else {
                low++;
                high--;
            }
        }

        return true;
    }
}
