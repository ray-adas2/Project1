"""
一元二次方程求解器 — 白盒测试

测试设计方法：
  - 语句覆盖：所有代码行至少执行一次
  - 分支覆盖：每个 if/else 分支均被覆盖
  - 路径覆盖：Δ>0、Δ=0、Δ<0、a=0 四条路径全覆盖

直接测试内部方法，验证代码内部逻辑的正确性。
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from quadratic_solver import QuadraticSolver


class TestValidateA:
    """白盒：测试 _validate_a 内部方法"""

    def test_valid_a_passes(self):
        """正常 a 值不抛异常"""
        assert QuadraticSolver._validate_a(1.0) is None
        assert QuadraticSolver._validate_a(-1.0) is None
        assert QuadraticSolver._validate_a(0.1) is None

    def test_a_zero_raises(self):
        """a=0 抛出 ValueError"""
        with pytest.raises(ValueError):
            QuadraticSolver._validate_a(0.0)

    def test_a_near_zero_raises(self):
        """a 极其接近 0 也抛出（浮点容差）"""
        with pytest.raises(ValueError):
            QuadraticSolver._validate_a(1e-15)


class TestCalculateDiscriminant:
    """白盒：测试 _calculate_discriminant 内部方法"""

    def test_delta_positive(self):
        assert QuadraticSolver._calculate_discriminant(1, -5, 6) == 1.0

    def test_delta_zero(self):
        assert QuadraticSolver._calculate_discriminant(1, 2, 1) == 0.0

    def test_delta_negative(self):
        assert QuadraticSolver._calculate_discriminant(1, 2, 5) == -16.0

    def test_negative_coefficients(self):
        """负系数的判别式"""
        assert QuadraticSolver._calculate_discriminant(-1, 2, -3) == -8.0


class TestSolveRealDistinct:
    """白盒：测试 _solve_real_distinct（Δ>0 分支）"""

    def test_two_distinct_roots(self):
        result = QuadraticSolver._solve_real_distinct(1, -5, 1)
        assert result["type"] == "real_distinct"
        assert len(result["roots"]) == 2


class TestSolveRealEqual:
    """白盒：测试 _solve_real_equal（Δ=0 分支）"""

    def test_single_repeated_root(self):
        result = QuadraticSolver._solve_real_equal(1, -4)
        assert result["type"] == "real_equal"
        assert len(result["roots"]) == 1
        assert abs(float(result["roots"][0]) - 2.0) < 1e-9
        assert result["discriminant"] == 0.0


class TestSolveComplex:
    """白盒：测试 _solve_complex（Δ<0 分支）"""

    def test_conjugate_complex_roots(self):
        result = QuadraticSolver._solve_complex(1, 2, -16)
        assert result["type"] == "complex"
        assert len(result["roots"]) == 2
        for root in result["roots"]:
            assert "i" in root

    def test_pure_imaginary(self):
        """实部为 0 的纯虚根"""
        result = QuadraticSolver._solve_complex(1, 0, -4)
        assert result["type"] == "complex"
        assert len(result["roots"]) == 2


class TestBranchCoverage:
    """白盒：验证 solve() 所有分支"""

    def test_branch_delta_positive(self):
        """Δ > EPSILON → _solve_real_distinct"""
        result = QuadraticSolver.solve(1, -5, 6)
        assert result["type"] == "real_distinct"

    def test_branch_delta_zero(self):
        """|Δ| <= EPSILON → _solve_real_equal"""
        result = QuadraticSolver.solve(1, 2, 1)
        assert result["type"] == "real_equal"

    def test_branch_delta_negative(self):
        """else → _solve_complex"""
        result = QuadraticSolver.solve(1, 2, 5)
        assert result["type"] == "complex"

    def test_branch_a_zero(self):
        """a == 0 → ValueError"""
        with pytest.raises(ValueError):
            QuadraticSolver.solve(0, 2, 3)


class TestPathCoverage:
    """白盒：验证所有 4 条执行路径"""

    def test_path_real_distinct(self):
        """路径1: 校验通过 → Δ>0 → 实根"""
        result = QuadraticSolver.solve(1, -3, 2)
        assert result["type"] == "real_distinct"

    def test_path_real_equal(self):
        """路径2: 校验通过 → Δ=0 → 重根"""
        result = QuadraticSolver.solve(1, -2, 1)
        assert result["type"] == "real_equal"

    def test_path_complex(self):
        """路径3: 校验通过 → Δ<0 → 虚根"""
        result = QuadraticSolver.solve(1, 1, 1)
        assert result["type"] == "complex"

    def test_path_invalid(self):
        """路径4: 校验失败 → 抛异常"""
        with pytest.raises(ValueError):
            QuadraticSolver.solve(0, 1, 1)
