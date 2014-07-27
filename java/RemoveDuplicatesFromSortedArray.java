public class RemoveDuplicatesFromSortedArray {
    /**
     * Solution: Iterate through the list and compare nested element.
     * Analysis: Time Complexity - O(N), where N means the elements in the array.
     *           Space Complexity - O(1), no additional space is required.
     */
    public static int removeDuplicates(int[] A) {
        if (A == null || A.length == 0) return 0;

        int occur = 2 - 1;
        int index = occur;
        for (int i = occur; i < A.length; i++) {
            if (A[i] != A[index]) A[index++] = A[i];
        }

        return index;
    }
}
