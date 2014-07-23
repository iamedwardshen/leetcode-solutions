public class SetMatrixZeroes {
    public void setZeroes(int[][] matrix) {
        if (matrix == null) {
            return;
        }

        int M = matrix.length;
        int N = matrix[0].length;
        boolean[] rows = new boolean[M];
        boolean[] cols = new boolean[N];
        for (int r = 0; r < M; r++) {
            for (int c = 0; c < N; c++) {
                if (matrix[r][c] == 0) {
                    rows[r] = true;
                    cols[c] = true;
                }
            }
        }

        for (int r = 0; r < M; r++) {
            for (int c = 0; c < N; c++) {
                if (rows[r]|| cols[c]) {
                    matrix[r][c] = 0;
                }
            }
        }
    }
}
