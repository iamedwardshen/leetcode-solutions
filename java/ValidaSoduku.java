public class ValidSudoku {
    private boolean check(char ch, boolean[] used) {
        if (ch == '.') return true;

        int index = ch - '1';
        if (used[index]) {
            return false;
        }
        used[index] = true;

        return true;
    }

    public boolean isValidSudoku(char[][] board) {
        boolean[] used = new boolean[9];
        for (int i = 0; i < 9; i++) {
            Arrays.fill(used, false);
            for (int j = 0; j < 9; j++) {
                if (!check(board[i][j], used)) {
                    return false;
                }
            }

            Arrays.fill(used, false);
            for (int j = 0; j < 9; j++) {
                if (!check(board[j][i], used)) {
                    return false;
                }
            }
        }

        for (int r = 0; r < 3; r++) {
            for (int c = 0; c < 3; c++) {
                Arrays.fill(used, false);
                for (int i = r * 3; i < r * 3 + 3; i++) {
                    for (int j = c * 3; j < c * 3 + 3; j++) {
                        if (!check(board[i][j], used)) {
                            return false;
                        }
                    }
                }
            }
        }

        return true;
    }
}
