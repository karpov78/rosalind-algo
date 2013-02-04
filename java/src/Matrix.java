/**
 * @author ekarpov
 */
@SuppressWarnings("unchecked")
public class Matrix<T> {
    public final int rows;
    public final int cols;
    public final Object[] matrix;

    public static Matrix<Integer> parseIntMatrix(final String... rows) {
        final Matrix<Integer> result = new Matrix<Integer>(rows.length, rows[0].split(" ").length);
        int idx = 0;
        for (final String row : rows) {
            for (final String cell : row.split(" ")) {
                result.set(idx++, Integer.parseInt(cell));
            }
        }
        return result;
    }

    public Matrix(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
        this.matrix = new Object[rows * cols];
    }

    public int index(int x, int y) {
        return x * cols + y;
    }

    public int[] decode(int index) {
        final int x = index / cols;
        return new int[]{x, index - x * cols};
    }

    public T get(int index) {
        return (T) matrix[index];
    }

    public T get(int x, int y) {
        return (T) matrix[index(x, y)];
    }

    public void set(int index, T value) {
        matrix[index] = value;
    }

    public void set(int x, int y, T value) {
        matrix[index(x, y)] = value;
    }

    public void del(int index) {
        matrix[index] = null;
    }

    public void del(int x, int y) {
        matrix[index(x, y)] = null;
    }

    public String toString() {
        final StringBuilder result = new StringBuilder();
        int idx = 0;
        for (int i = 0; i < rows; i++) {
            if (i > 0) result.append('\n');

            for (int j = 0; j < cols; j++) {
                if (j > 0) result.append(' ');
                result.append(matrix[idx++]);
            }
        }
        return result.toString();
    }
}
