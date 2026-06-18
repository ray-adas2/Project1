package quadratic;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.lang.reflect.Method;

class WhiteBoxTest {

    @Test
    void testValidateANonZero() throws Exception {
        Method method = QuadraticSolver.class.getDeclaredMethod("validateA", double.class);
        method.setAccessible(true);
        method.invoke(null, 1.0);
        method.invoke(null, -1.0);
        method.invoke(null, 0.1);
    }

    @Test
    void testValidateAZero() throws Exception {
        Method method = QuadraticSolver.class.getDeclaredMethod("validateA", double.class);
        method.setAccessible(true);
        try {
            method.invoke(null, 0.0);
            fail("应该抛异常");
        } catch (Exception e) {
            assertTrue(e.getCause() instanceof IllegalArgumentException);
        }
    }

    @Test
    void testDeltaPositive() throws Exception {
        Method method = QuadraticSolver.class.getDeclaredMethod(
                "calculateDiscriminant", double.class, double.class, double.class);
        method.setAccessible(true);
        double delta = (double) method.invoke(null, 1, -5, 6);
        assertEquals(1.0, delta, 1e-9);
    }

    @Test
    void testDeltaZero() throws Exception {
        Method method = QuadraticSolver.class.getDeclaredMethod(
                "calculateDiscriminant", double.class, double.class, double.class);
        method.setAccessible(true);
        double delta = (double) method.invoke(null, 1, 2, 1);
        assertEquals(0.0, delta, 1e-9);
    }

    @Test
    void testDeltaNegative() throws Exception {
        Method method = QuadraticSolver.class.getDeclaredMethod(
                "calculateDiscriminant", double.class, double.class, double.class);
        method.setAccessible(true);
        double delta = (double) method.invoke(null, 1, 2, 5);
        assertEquals(-16.0, delta, 1e-9);
    }

    @Test
    void testBranchDeltaPositive() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, -5, 6);
        assertEquals(QuadraticSolver.RootType.REAL_DISTINCT, result.type);
    }

    @Test
    void testBranchDeltaZero() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, 2, 1);
        assertEquals(QuadraticSolver.RootType.REAL_EQUAL, result.type);
    }

    @Test
    void testBranchDeltaNegative() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, 2, 5);
        assertEquals(QuadraticSolver.RootType.COMPLEX, result.type);
    }

    @Test
    void testBranchAZero() {
        assertThrows(IllegalArgumentException.class, () -> {
            QuadraticSolver.solve(0, 2, 3);
        });
    }

    @Test
    void testPathRealDistinct() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, -3, 2);
        assertEquals(QuadraticSolver.RootType.REAL_DISTINCT, result.type);
    }

    @Test
    void testPathRealEqual() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, -2, 1);
        assertEquals(QuadraticSolver.RootType.REAL_EQUAL, result.type);
    }

    @Test
    void testPathComplex() {
        QuadraticSolver.Solution result = QuadraticSolver.solve(1, 1, 1);
        assertEquals(QuadraticSolver.RootType.COMPLEX, result.type);
    }

    @Test
    void testPathInvalid() {
        assertThrows(IllegalArgumentException.class, () -> {
            QuadraticSolver.solve(0, 1, 1);
        });
    }
}
