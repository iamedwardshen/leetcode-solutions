public class RemoveElement {
    public int removeElement(int[] A, int elem) {
        if (A == null || A.length < 1) return 0;

        int index = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] != elem) A[index++] = A[i];
        }

        return index;
    }
}
