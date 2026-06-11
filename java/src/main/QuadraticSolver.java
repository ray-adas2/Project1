package quadratic;

public class QuadraticSolver {

    private static final double EPSILON = 1e-10;

    public static Solution solve(double a, double b, double c) {
        validateA(a);
        double discriminant = calculateDiscriminant(a, b, c);

        if (discriminant > EPSILON) {
            return solveRealDistinct(a, b, discriminant);
        } else if (Math.abs(discriminant) <= EPSILON) {
            return solveRealEqual(a, b);
        } else {
            return solveComplex(a, b, discriminant);
        }
    }

    private static void validateA(double a) {
        if (Math.abs(a) < EPSILON) {
            throw new IllegalArgumentException(
                "参数 a 不能为 0，当前 a = " + a + "，方程退化为一次方程"
            );
        }
    }

    private static double calculateDiscriminant(double a, double b, double c) {
        return b * b - 4 * a * c;
    }

    private static Solution solveRealDistinct(double a, double b, double discriminant) {
        double sqrtDelta = Math.sqrt(discriminant);
        double root1 = (-b + sqrtDelta) / (2 * a);
        double root2 = (-b - sqrtDelta) / (2 * a);
        return new Solution(RootType.REAL_DISTINCT,
                new String[]{String.valueOf(root1), String.valueOf(root2)},
                discriminant);
    }

    private static Solution solveRealEqual(double a, double b) {
        double root = -b / (2 * a);
        return new Solution(RootType.REAL_EQUAL,
                new String[]{String.valueOf(root)}, 0.0);
    }

    private static Solution solveComplex(double a, double b, double discriminant) {
        double realPart = -b / (2 * a);
        double imagPart = Math.sqrt(-discriminant) / (2 * a);

        String root1, root2;
        if (Math.abs(realPart) < EPSILON) {
            root1 = imagPart + "i";
            root2 = "-" + imagPart + "i";
        } else {
            root1 = realPart + "+" + imagPart + "i";
            root2 = realPart + "-" + imagPart + "i";
        }

        return new Solution(RootType.COMPLEX,
                new String[]{root1, root2}, discriminant);
    }

    public enum RootType {
        REAL_DISTINCT, REAL_EQUAL, COMPLEX
    }

    public static class Solution {
        public final RootType type;
        public final String[] roots;
        public final double discriminant;

        public Solution(RootType type, String[] roots, double discriminant) {
            this.type = type;
            this.roots = roots;
            this.discriminant = discriminant;
        }
    }
}