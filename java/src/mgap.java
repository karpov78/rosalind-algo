import java.util.Scanner;

/**
 * @author ekarpov
 */
public class mgap {
    private static class MaxGapMatrix extends LevMatrix {
        private class MaxGapCell extends Cell {
            private int gaps;

            private MaxGapCell(int x, int y, int weight, MaxGapCell prevCell) {
                super(x, y, weight, null, null, prevCell);
                gaps = prevCell != null ? prevCell.gaps + (prevCell.isLeftTo(this) || prevCell.isOnTopOf(this) ? 1 : 0) : 0;
            }
        }

        private MaxGapMatrix(String s, String t) throws InterruptedException {
            super(s, t);
        }

        protected Cell createCell(int x, int y, int weight, Cell prevCell) {
            return new MaxGapCell(x, y, weight, (MaxGapCell) prevCell);
        }

        protected Cell buildCell(Cell diag, Cell top, Cell left, int x, int y) {
            if (top == null && left == null) return createCell(x, y, 0, null);
            else if (top == null) return createCell(x, y, left.weight + getWeight(GAP_SYMBOL, ' '), left);
            else if (left == null) return createCell(x, y, top.weight + getWeight(GAP_SYMBOL, ' '), top);
            else {
                final int topWeight = top.weight + getWeight(GAP_SYMBOL, ' ');
                final int leftWeight = left.weight + getWeight(GAP_SYMBOL, ' ');
                final int diagWeight = diag.weight + getWeight(s.charAt(x), t.charAt(y));

                if (diagWeight > leftWeight && diagWeight > topWeight)
                    return createCell(x, y, diagWeight, diag);
                else if (leftWeight == topWeight) {
                    if (((MaxGapCell) left).gaps > ((MaxGapCell) top).gaps) {
                        return createCell(x, y, leftWeight, left);
                    } else {
                        return createCell(x, y, topWeight, top);
                    }
                } else if (leftWeight > topWeight) {
                    return createCell(x, y, leftWeight, left);
                } else {
                    return createCell(x, y, topWeight, top);
                }
            }
        }
    }

    public static void main(final String[] args) throws InterruptedException {
        final Scanner scanner = new Scanner(System.in);
        final String s = scanner.nextLine();
        final String t = scanner.nextLine();
        final MaxGapMatrix matrix = new MaxGapMatrix(s, t);
        System.out.println(((MaxGapMatrix.MaxGapCell) matrix.getLastCell()).gaps);
    }
}
