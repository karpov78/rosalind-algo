import org.apache.commons.lang.StringUtils;

import java.util.Arrays;
import java.util.BitSet;
import java.util.concurrent.Callable;

/**
 * @author ekarpov
 */
public class LevMatrix {
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

    public static class Cell {
        public final int x;
        public final int y;
        public final int weight;
        public final String s_prefix;
        public final String t_prefix;

        public Cell(final int x, final int y, final int weight, final String s, final String t) {
            this(x, y, weight, s, t, null);
        }

        public Cell(final int x, final int y, final int weight, final String s, final String t, final Cell prevCell) {
            this.x = x;
            this.y = y;
            this.weight = weight;

            if (s != null && t != null) {
                if (prevCell == null) {
                    s_prefix = "";
                    t_prefix = "";
                } else if (prevCell.isOnTopOf(this)) {
                    s_prefix = prevCell.s_prefix + s.substring(prevCell.x + 1, x + 1);
                    t_prefix = prevCell.t_prefix + StringUtils.rightPad("", x - prevCell.x, GAP_SYMBOL);
                } else if (prevCell.isLeftTo(this)) {
                    s_prefix = prevCell.s_prefix + StringUtils.rightPad("", y - prevCell.y, GAP_SYMBOL);
                    t_prefix = prevCell.t_prefix + t.substring(prevCell.y + 1, y + 1);
                } else {
                    s_prefix = prevCell.s_prefix + s.charAt(x);
                    t_prefix = prevCell.t_prefix + t.charAt(y);
                }
            } else {
                s_prefix = null;
                t_prefix = null;
            }
        }

        public boolean isOnTopOf(final Cell other) {
            return y == other.y && x < other.x;
        }

        public boolean isLeftTo(final Cell other) {
            return x == other.x && y < other.y;
        }

        public String toString() {
            return Integer.toString(weight);
        }
    }

    protected final String s;
    protected final String t;
    protected final Matrix<Cell> matrix;
    private final boolean cleanup;

    public LevMatrix(String s, String t) throws InterruptedException {
        this(s, t, false);
    }

    protected LevMatrix(String s, String t, boolean cleanup) throws InterruptedException {
        this.s = s;
        this.t = t;
        this.cleanup = cleanup;
        matrix = new Matrix<Cell>(s.length() + 1, t.length() + 1);
        calculateMatrix();
    }

    protected Cell createCell(int x, int y, int weight, Cell prevCell) {
        return new Cell(x, y, weight, s, t, prevCell);
    }

    protected int getWeight(char a, char b) {
        return a == b ? 1 : 0;
    }

    protected Cell calculatePathFromTop(Cell top, int x, int y) {
        return createCell(x, y, top.weight + GAP_WEIGHT, top);
    }

    protected Cell calculatePathFromLeft(Cell left, int x, int y) {
        return createCell(x, y, left.weight + GAP_WEIGHT, left);
    }

    protected Cell buildCell(Cell diag, Cell top, Cell left, int x, int y) {
        if (top == null && left == null) {
            return createCell(x, y, 0, null);
        } else if (top == null) {
            return calculatePathFromLeft(left, x, y);
        } else if (left == null) {
            return calculatePathFromTop(top, x, y);
        } else {
            final Cell pathFromTop = calculatePathFromTop(top, x, y);
            final Cell pathFromLeft = calculatePathFromLeft(left, x, y);
            final Cell diagPath = createCell(x, y, diag.weight + getWeight(s.charAt(x), t.charAt(y)), diag);

            if (pathFromTop.weight >= pathFromLeft.weight && pathFromTop.weight >= diagPath.weight) {
                return pathFromTop;
            } else if (pathFromLeft.weight >= pathFromTop.weight && pathFromLeft.weight >= diagPath.weight) {
                return pathFromLeft;
            } else {
                return diagPath;
            }
        }
    }

    private Cell getCell(int index) {
        synchronized (matrix) {
            try {
                Cell cell;
                while ((cell = matrix.get(index)) == null) {
                    matrix.wait();
                }
                return cell;
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }

    protected void calculateMatrixRow(final int row) {
        int current_index = matrix.index(row + 1, 0);
        System.out.println("calculating row " + row + " - index " + current_index);
        int left_index = current_index - 1;
        int top_index = current_index - matrix.cols;
        int diag_index = top_index - 1;

        final int t_len = t.length();
        for (int j = -1; j < t_len; j++) {
            final Cell diag = row >= 0 && j >= 0 ? getCell(diag_index) : null;
            final Cell top = row >= 0 ? getCell(top_index) : null;
            final Cell left = j >= 0 ? getCell(left_index) : null;

            final Cell cell = buildCell(diag, top, left, row, j);
            synchronized (matrix) {
                matrix.set(current_index, cell);
                matrix.notifyAll();
            }

            if (cleanup && diag_index >= 0) matrix.del(diag_index);
            if (cleanup && j == t_len - 1) matrix.del(top_index);

            current_index++;
            top_index++;
            left_index++;
            diag_index++;
        }
    }

    protected void calculateMatrix() throws InterruptedException {
        final int len_s = s.length();

        final BitSet processedRows = new BitSet(len_s + 1);

        final Thread[] threads = new Thread[4];
        for (int i = 0; i < threads.length; i++) {
            threads[i] = new Thread(new Runnable() {
                public void run() {
                    int row = -1;
                    while (row < len_s) {
                        synchronized (processedRows) {
                            while (processedRows.get(row + 1) && row < len_s) {
                                row++;
                            }
                            if (row == len_s) break;
                            processedRows.set(row + 1);
                        }
                        calculateMatrixRow(row);
                        row++;
                    }
                }
            });
            threads[i].start();
        }
        for (final Thread thread : threads) {
            thread.join();
        }
    }

    public Cell getLastCell() {
        return matrix.get((s.length() + 1) * (t.length() + 1) - 1);
    }

    public int getDistance() {
        return getLastCell().weight;
    }

    public String[] getAlignedStrings() {
        final Cell cell = getLastCell();
        return new String[]{cell.s_prefix, cell.t_prefix};
    }

    public String toString() {
        return matrix.toString();
    }

    private class RowCalculator implements Callable<Object> {
        private int row;

        public RowCalculator(int i) {
            this.row = i;
        }

        public Object call() throws Exception {
            calculateMatrixRow(row);
            return null;
        }
    }
}
