import java.util.Arrays;
import java.util.Scanner;

import static java.lang.String.format;

/**
 * @author ekarpov
 */
public class laff {
    private static class LaffMatrix extends LevMatrix<short[]> {
        private static final int WEIGHT = 0;
        private static final int GAP_TOP = 1;
        private static final int GAP_LEFT = 2;

        private short leftGapOpen(short[] left) {
            if (left == null) {
                return -12;
            }
            short w = (short) (left[WEIGHT] - 12);
            short w2 = (short) (left[GAP_LEFT] - 1);
            return w > w2 ? w : w2;
        }

        private short topGapOpen(short[] top) {
            if (top == null) {
                return -12;
            }
            short w = (short) (top[WEIGHT] - 12);
            short w2 = (short) (top[GAP_TOP] - 1);
            return w > w2 ? w : w2;
        }

        private int maxWeight = -1;
        private int maxX;
        private int maxY;

        private LaffMatrix(String s, String t) throws InterruptedException {
            super(s, t, short[].class);
            matrix.setFormatter(new Matrix.CellFormatter<short[]>() {
                public String format(short[] cell) {
                    return String.format("%2d(%2d,%2d)", cell[WEIGHT], cell[GAP_TOP], cell[GAP_LEFT]);
                }
            });
        }

        protected int getWeight(char a, char b) {
            return getBlosumWeight(a, b);
        }

        protected short[] buildCell(short[] diag, short[] top, short[] left, int x, int y) {
            if (top == null && left == null)
                return createCell((short) 0, null, null);
            else if (top == null)
                return createCell((short) 0, null, left);
            else if (left == null)
                return createCell((short) 0, top, null);
            else {
                short max_weight = (short) (diag[WEIGHT] + getWeight(s.charAt(x), t.charAt(y)));
                short top_weight = topGapOpen(top);
                if (max_weight < top_weight) {
                    max_weight = top_weight;
                }

                short left_weight = leftGapOpen(left);
                if (left_weight > max_weight) {
                    max_weight = left_weight;
                }

                if (this.maxWeight < max_weight) {
                    this.maxWeight = max_weight;
                    this.maxX = x;
                    this.maxY = y;
                }
                return createCell(max_weight, top, left);
            }
        }

        protected short[] createCell(short weight, short[] top, short[] left) {
            if (weight < 0) {
                return new short[]{0, topGapOpen(null), leftGapOpen(null)};
            }
            return new short[]{weight, topGapOpen(top), leftGapOpen(left)};
        }

        private String padGap(int len) {
            char[] p = new char[len];
            Arrays.fill(p, GAP_SYMBOL);
            return new String(p);
        }

        public String[] getAlignedStrings(int x, int y) throws Exception {
            final StringBuilder se = new StringBuilder();
            final StringBuilder st = new StringBuilder();

            short[] cell = matrix.get(x + 1, y + 1);
            while (x >= 0 && y >= 0 && cell[WEIGHT] > 0) {
                short[] diag = matrix.get(x, y);
                if (diag[WEIGHT] + getBlosumWeight(s.charAt(x), t.charAt(y)) == cell[WEIGHT]) {
//                    System.out.println(format("%s (%d) -> %s (%d) - %d", s.charAt(x), x, t.charAt(y), y, cell[WEIGHT]));
                    se.insert(0, s.charAt(x));
                    st.insert(0, t.charAt(y));
                    x = x - 1;
                    y = y - 1;
                } else if (cell[WEIGHT] == cell[GAP_TOP]) {
                    for (int dx = x - 1; dx >= 0; dx--) {
                        short[] topCell = matrix.get(dx + 1, y + 1);
                        if (topCell[WEIGHT] - 11 - (x - dx) == cell[WEIGHT]) {
                            final String pad = padGap(x - dx);
//                            System.out
//                                  .println(format("%s (%d) -> %s (%d) - %d", s.substring(dx + 1, x + 1), x, pad, y, cell[WEIGHT]));
                            se.insert(0, s.substring(dx + 1, x + 1));
                            st.insert(0, pad);
                            x = dx;
                            break;
                        }
                    }
                } else if (cell[WEIGHT] == cell[GAP_LEFT]) {
                    for (int dy = y - 1; dy >= 0; dy--) {
                        short[] leftCell = matrix.get(x + 1, dy + 1);
                        if (leftCell[WEIGHT] - 11 - (y - dy) == cell[WEIGHT]) {
                            final String pad = padGap(y - dy);
//                            System.out
//                                  .println(format("%s (%d) -> %s (%d) - %d", pad, x, t.substring(dy + 1, y + 1), y, cell[WEIGHT]));
                            se.insert(0, pad);
                            st.insert(0, t.substring(dy + 1, y + 1));
                            y = dy;
                            break;
                        }
                    }
                } else {
                    throw new Exception(format("Inconsistent weights: %d, %d, %d", cell[WEIGHT], cell[GAP_TOP], cell[GAP_LEFT]));
                }
                cell = matrix.get(x + 1, y + 1);
            }
            return new String[]{se.toString(), st.toString()};
        }
    }

    private static void _validate(int d, String s, String t) throws Exception {
        if (s.length() != t.length()) {
            throw new Exception("Inconsistent lengths");
        }
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            final char s_ch = s.charAt(i);
            final char t_ch = t.charAt(i);
            if (i > 0 && s_ch == LevMatrix.GAP_SYMBOL && s.charAt(i - 1) == LevMatrix.GAP_SYMBOL) {
                count--;
            } else if (i > 0 && t_ch == LevMatrix.GAP_SYMBOL && t.charAt(i - 1) == LevMatrix.GAP_SYMBOL) {
                count -= 1;
            } else if (s_ch == LevMatrix.GAP_SYMBOL || t_ch == LevMatrix.GAP_SYMBOL) {
                count -= 12;
            } else {
                count += LevMatrix.getBlosumWeight(s_ch, t_ch);
            }
        }
        if (d != count) {
            throw new Exception(format("Invalid transformation: expected distance - %d, but was - %d", d, count));
        }
    }


    public static void main(final String[] args) throws Exception {
        final Scanner scanner = new Scanner(System.in);
        final String s = scanner.nextLine();
        final String t = scanner.nextLine();
        final LaffMatrix matrix = new LaffMatrix(s, t);
        matrix.calculateMatrix();
        System.out.println(matrix.maxWeight);
        final String[] edited = matrix.getAlignedStrings(matrix.maxX, matrix.maxY);
        _validate(matrix.maxWeight, edited[0], edited[1]);

        final String s1 = edited[0].replaceAll("-", "");
        final String t1 = edited[1].replaceAll("-", "");
        System.out.println(s1);
        System.out.println(t1);

        final LaffMatrix testMatrix = new LaffMatrix(s1, t1);
        testMatrix.calculateMatrix();
        if (testMatrix.maxWeight != matrix.maxWeight) {
            final String[] sub_edited = testMatrix.getAlignedStrings(testMatrix.maxX, testMatrix.maxY);
            System.out.println("=====================================================================");
            System.out.println(testMatrix);
            System.out.println("=====================================================================");
            throw new Exception(format("Validation failed: substrings alignment differ: %d\n%s\n%s", testMatrix.maxWeight, sub_edited[0], sub_edited[1]));
        }
    }
}
