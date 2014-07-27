public class public class RemoveDuplicatesFromSortedArrayII {
    public int removeDuplicates(int[] A) {
        if (A == null) return 0;
        if (A.length <= 2) return A.length;

        int occur = 3 - 1;
        int index = occur;
        for (int i = occur; i < A.length; i++) {
            if (A[i] != A[index - occur]) A[index++] = A[i];
        }

        return index;
    }
}
