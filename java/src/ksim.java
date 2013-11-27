import cern.colt.map.OpenIntIntHashMap;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * @author ekarpov
 */
public class ksim {
    private static class KsimMatrix extends LevMatrix<Integer> {
        private KsimMatrix(String s, String t) throws InterruptedException {
            super(s, t, int.class);
            matrix.setFormatter(new Matrix.CellFormatter<Integer>() {
                public String format(Integer cell) {
                    return String.format("%2d", cell);
                }
            });
        }

        protected int getWeight(char a, char b) {
            return a == b ? 0 : 1;
        }

        protected Integer buildCell(Integer diag, Integer top, Integer left, int x, int y) {
            if (top == null && left == null)
                return 0;
            else if (top == null)
                return left + 1;
            else if (left == null) {
                return y >= 0 ? top + 1 : 0;
            } else {
                int min_weight = diag + getWeight(s.charAt(x), t.charAt(y));
                int top_weight = top + 1;
                if (min_weight > top_weight) {
                    min_weight = top_weight;
                }

                int left_weight = left + 1;
                if (min_weight > left_weight) {
                    min_weight = left_weight;
                }
                return min_weight;
            }
        }

        private final Map<Integer, int[]> cache = new HashMap<Integer, int[]>();

        public int[] find(int x, int y) throws Exception {
            if (x >= 0 && y >= 0) {
                final int index = matrix.index(x + 1, y + 1);
                if (cache.containsKey(index)) {
                    return cache.get(index);
                }
                final int cell = matrix.get(index);
                final int diag = matrix.get(index - matrix.cols - 1);
                final int topCell = matrix.get(index - matrix.cols);
                final int leftCell = matrix.get(index - 1);

                final OpenIntIntHashMap endPoints = new OpenIntIntHashMap();
                if (diag + getWeight(s.charAt(x), t.charAt(y)) == cell) {
                    final int[] diagEndPoints = find(x - 1, y - 1);
                    for (final int endPoint : diagEndPoints) {
                        endPoints.put(endPoint, endPoint);
                    }
                }
                if (cell == topCell + 1) {
                    final int[] topEndPoints = find(x - 1, y);
                    for (final int endPoint : topEndPoints) {
                        endPoints.put(endPoint, endPoint);
                    }
                }
                if (cell == leftCell + 1) {
                    final int[] leftEndPoints = find(x, y - 1);
                    for (final int endPoint : leftEndPoints) {
                        endPoints.put(endPoint, endPoint);
                    }
                }
                final int[] result = endPoints.keys().elements();
                cache.put(index, result);
                return result;
            } else {
                return new int[]{x};
            }
        }
    }

    public static void main(final String[] args) throws Exception {
        final Scanner scanner = new Scanner(System.in);
        final int k = Integer.parseInt(scanner.nextLine());
        final String s = scanner.nextLine();
        final String t = scanner.nextLine();
        final KsimMatrix matrix = new KsimMatrix(t, s);
        matrix.calculateMatrix();
        //System.out.println(matrix);

        final int y = s.length() - 1;
        for (int x = -1; x < t.length(); x++) {
            final Integer weight = matrix.matrix.get(x + 1, y + 1);
            if (weight <= k) {
                final int[] result = matrix.find(x, y);
                for (final int start : result) {
                    System.out.println(String.format("%d %d", start + 2, x - start));
                }
            }
        }
    }
}
