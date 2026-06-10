"""
一元二次方程求解器 — 黑盒测试

测试设计方法：
  - 等价类划分（有效等价类 / 无效等价类）
  - 边界值分析

不关注代码内部实现，仅验证给定输入是否产生正确的输出。
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from quadratic_solver import QuadraticSolver


class TestValidEquivalenceClasses:
    """有效等价类 — 合法的二次方程输入"""

    def test_tc1_two_distinct_real_roots(self):
        """TC1: (1, -5, 6) → Δ>0，两个不同实根 x₁=3, x₂=2"""
        result = QuadraticSolver.solve(1, -5, 6)
        assert result["type"] == "real_distinct"
        assert len(result["roots"]) == 2
        assert result["discriminant"] > 0
        roots_float = [float(r) for r in result["roots"]]
        assert sorted(roots_float) == [2.0, 3.0]

    def test_tc3_two_complex_roots(self):
        """TC3: (1, 2, 5) → Δ<0，共轭虚根"""
        result = QuadraticSolver.solve(1, 2, 5)
        assert result["type"] == "complex"
        assert len(result["roots"]) == 2
        assert result["discriminant"] < 0

    def test_tc5_real_roots_with_c_zero(self):
        """TC5: (2, 0, -8) → c=0，两个不同实根 x₁=2, x₂=-2"""
        result = QuadraticSolver.solve(2, 0, -8)
        assert result["type"] == "real_distinct"
        roots_float = [float(r) for r in result["roots"]]
        assert sorted(roots_float) == [-2.0, 2.0]

    def test_tc8_negative_a_complex_roots(self):
        """TC8: (-1, 2, -3) → a 为负数，共轭虚根"""
        result = QuadraticSolver.solve(-1, 2, -3)
        assert result["type"] == "complex"
        assert result["discriminant"] < 0


class TestBoundaryValueAnalysis:
    """边界值分析 — Δ=0 临界情况"""

    def test_tc2_discriminant_zero(self):
        """TC2: (1, 2, 1) → Δ=0，重根 x=-1"""
        result = QuadraticSolver.solve(1, 2, 1)
        assert result["type"] == "real_equal"
        assert len(result["roots"]) == 1
        assert abs(float(result["roots"][0]) - (-1.0)) < 1e-9

    def test_tc6_discriminant_zero_with_b_c_zero(self):
        """TC6: (1, 0, 0) → Δ=0，重根 x=0"""
        result = QuadraticSolver.solve(1, 0, 0)
        assert result["type"] == "real_equal"
        assert abs(float(result["roots"][0]) - 0.0) < 1e-9

    def test_tc7_pure_imaginary_roots(self):
        """TC7: (1, 0, 1) → Δ<0，纯虚根 ±i"""
        result = QuadraticSolver.solve(1, 0, 1)
        assert result["type"] == "complex"
        for root in result["roots"]:
            assert "i" in root


class TestInvalidEquivalenceClasses:
    """无效等价类 — a=0 非法输入"""

    def test_tc4_a_is_zero_raises_error(self):
        """TC4: (0, 2, 3) → 抛出 ValueError"""
        with pytest.raises(ValueError):
            QuadraticSolver.solve(0, 2, 3)

    def test_a_near_zero_raises_error(self):
        """扩展：a 非常接近 0 也应抛出异常"""
        with pytest.raises(ValueError):
            QuadraticSolver.solve(0.0, 1, 1)
