package quadratic;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BlackBoxTest {

    @Test
    void testTc1_twoDistinctRealRoots() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, -5, 6);
        assertEquals(QuadraticSolver.RootType.REAL_DISTINCT, result.type);
        assertEquals(2, result.roots.length);
        double r1 = Double.parseDouble(result.roots[0]);
        double r2 = Double.parseDouble(result.roots[1]);
        assertTrue(Math.abs(r1 - 3.0) < 1e-9 || Math.abs(r1 - 2.0) < 1e-9);
        assertTrue(Math.abs(r2 - 3.0) < 1e-9 || Math.abs(r2 - 2.0) < 1e-9);
    }

    @Test
    void testTc3_twoComplexRoots() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, 2, 5);
        assertEquals(QuadraticSolver.RootType.COMPLEX, result.type);
        assertEquals(2, result.roots.length);
        assertTrue(result.discriminant < 0);
    }

    @Test
    void testTc5_realRootsWithCZero() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(2, 0, -8);
        assertEquals(QuadraticSolver.RootType.REAL_DISTINCT, result.type);
        double r1 = Double.parseDouble(result.roots[0]);
        double r2 = Double.parseDouble(result.roots[1]);
        assertTrue(Math.abs(r1 - 2.0) < 1e-9 || Math.abs(r1 + 2.0) < 1e-9);
        assertTrue(Math.abs(r2 - 2.0) < 1e-9 || Math.abs(r2 + 2.0) < 1e-9);
    }

    @Test
    void testTc8_negativeAComplexRoots() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(-1, 2, -3);
        assertEquals(QuadraticSolver.RootType.COMPLEX, result.type);
    }

    @Test
    void testTc2_discriminantZero() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, 2, 1);
        assertEquals(QuadraticSolver.RootType.REAL_EQUAL, result.type);
        assertEquals(1, result.roots.length);
        assertTrue(Math.abs(Double.parseDouble(result.roots[0]) - (-1.0)) < 1e-9);
    }

    @Test
    void testTc6_discriminantZeroWithBCZero() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, 0, 0);
        assertEquals(QuadraticSolver.RootType.REAL_EQUAL, result.type);
        assertTrue(Math.abs(Double.parseDouble(result.roots[0]) - 0.0) < 1e-9);
    }

    @Test
    void testTc7_pureImaginaryRoots() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, 0, 1);
        assertEquals(QuadraticSolver.RootType.COMPLEX, result.type);
        for (String root : result.roots) {
            assertTrue(root.contains("i"));
        }
    }

    @Test
    void testTc4_aIsZeroThrowsException() {
        assertThrows(IllegalArgumentException.class, () -> {
            QuadraticSolver.solve(0, 2, 3);
        });
    }

    @Test
    void testANearZeroThrowsException() {
        assertThrows(IllegalArgumentException.class, () -> {
            QuadraticSolver.solve(0.0, 1, 1);
        });
    }
}