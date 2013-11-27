import java.lang.reflect.Array;

/**
 * @author ekarpov
 */
@SuppressWarnings("unchecked")
public class Matrix<T> {
    public final int rows;
    public final int cols;
    public final Object matrix;
    private CellFormatter<T> formatter = new DefaultFormatter<T>();

    public interface CellFormatter<X> {
        String format(X cell);
    }

    private static class DefaultFormatter<X> implements CellFormatter<X> {
        public String format(X cell) {
            return cell.toString();
        }
    }

    public static Matrix<Integer> parseIntMatrix(final String... rows) {
        final Matrix<Integer> result = new Matrix<Integer>(rows.length, rows[0].split(" ").length, int.class);
        int idx = 0;
        for (final String row : rows) {
            for (final String cell : row.split(" ")) {
                result.set(idx++, Integer.parseInt(cell));
            }
        }
        return result;
    }

    public Matrix(int rows, int cols, Class<T> c) {
        this.rows = rows;
        this.cols = cols;
        this.matrix = Array.newInstance(c, rows * cols);
    }

    public void setFormatter(CellFormatter<T> formatter) {
        this.formatter = formatter;
    }

    public int index(int x, int y) {
        return x * cols + y;
    }

    public T get(int index) {
        return (T) Array.get(matrix, index);
    }

    public T get(int x, int y) {
        return (T) Array.get(matrix, index(x, y));
    }

    public void set(int index, T value) {
        Array.set(matrix, index, value);
    }

    public String toString() {
        final StringBuilder result = new StringBuilder();
        int idx = 0;
        for (int i = 0; i < rows; i++) {
            if (i > 0) result.append('\n');

            for (int j = 0; j < cols; j++) {
                if (j > 0) result.append(' ');
                result.append(formatter.format(get(idx++)));
            }
        }
        return result.toString();
    }
}
