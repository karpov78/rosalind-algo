import java.util.Arrays;

/**
 * @author ekarpov
 */
public abstract class LevMatrix<T> {
    public static final int GAP_WEIGHT = -5;
    public static final char GAP_SYMBOL = '-';

    public static final char[] SYMBOLS = {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'};

    public static final Matrix<Integer> BLOSUM62 = Matrix.parseIntMatrix(
            "4 0 -2 -1 -2 0 -2 -1 -1 -1 -1 -2 -1 -1 -1 1 0 0 -3 -2",
            "0 9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2",
            "-2 -3 6 2 -3 -1 -1 -3 -1 -4 -3 1 -1 0 -2 0 -1 -3 -4 -3",
            "-1 -4 2 5 -3 -2 0 -3 1 -3 -2 0 -1 2 0 0 -1 -2 -3 -2",
            "-2 -2 -3 -3 6 -3 -1 0 -3 0 0 -3 -4 -3 -3 -2 -2 -1 1 3",
            "0 -3 -1 -2 -3 6 -2 -4 -2 -4 -3 0 -2 -2 -2 0 -2 -3 -2 -3",
            "-2 -3 -1 0 -1 -2 8 -3 -1 -3 -2 1 -2 0 0 -1 -2 -3 -2 2",
            "-1 -1 -3 -3 0 -4 -3 4 -3 2 1 -3 -3 -3 -3 -2 -1 3 -3 -1",
            "-1 -3 -1 1 -3 -2 -1 -3 5 -2 -1 0 -1 1 2 0 -1 -2 -3 -2",
            "-1 -1 -4 -3 0 -4 -3 2 -2 4 2 -3 -3 -2 -2 -2 -1 1 -2 -1",
            "-1 -1 -3 -2 0 -3 -2 1 -1 2 5 -2 -2 0 -1 -1 -1 1 -1 -1",
            "-2 -3 1 0 -3 0 1 -3 0 -3 -2 6 -2 0 0 1 0 -3 -4 -2",
            "-1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2 7 -1 -2 -1 -1 -2 -4 -3",
            "-1 -3 0 2 -3 -2 0 -3 1 -2 0 0 -1 5 1 0 -1 -2 -2 -1",
            "-1 -3 -2 0 -3 -2 0 -3 2 -2 -1 0 -2 1 5 -1 -1 -3 -3 -2",
            "1 -1 0 0 -2 0 -1 -2 0 -2 -1 1 -1 0 -1 4 1 -2 -3 -2",
            "0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1 0 -1 -1 -1 1 5 0 -2 -2",
            "0 -1 -3 -2 -1 -3 -3 3 -2 1 1 -3 -2 -2 -3 -2 0 4 -3 -1",
            "-3 -2 -4 -3 1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11 2",
            "-2 -2 -3 -2 3 -3 2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1 2 7");

    public static int getBlosumWeight(char a, char b) {
        if (a == GAP_SYMBOL || b == GAP_SYMBOL) {
            return GAP_WEIGHT;
        } else {
            return BLOSUM62.get(Arrays.binarySearch(SYMBOLS, a), Arrays.binarySearch(SYMBOLS, b));
        }
    }

    protected final String s;
    protected final String t;
    protected final Matrix<T> matrix;

    protected LevMatrix(String s, String t) throws InterruptedException {
        this.s = s;
        this.t = t;
        matrix = new Matrix<T>(s.length() + 1, t.length() + 1);
    }

    protected abstract T buildCell(T diag, T top, T left, short x, short y);

    protected void calculateMatrix() throws InterruptedException {
        final int len_s = s.length();

        int current_index = 0;
        int left_index = current_index - 1;
        int top_index = current_index - matrix.cols;
        int diag_index = top_index - 1;

        for (short i = -1; i < len_s; i++) {
            System.out.print(String.format("\r%3d%%", i * 100 / matrix.rows));

            final int t_len = t.length();
            for (short j = -1; j < t_len; j++) {
                final T diag = i >= 0 && j >= 0 ? matrix.get(diag_index) : null;
                final T top = i >= 0 ? matrix.get(top_index) : null;
                final T left = j >= 0 ? matrix.get(left_index) : null;

                matrix.set(current_index, buildCell(diag, top, left, i, j));

                current_index++;
                top_index++;
                left_index++;
                diag_index++;
            }
        }
        System.out.print("\r     \r");
    }

    public String toString() {
        return matrix.toString();
    }
}
