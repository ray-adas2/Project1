"""
一元二次方程求解器

求解标准形式 ax² + bx + c = 0 的根，支持实根和虚根。
"""

import math


class QuadraticSolver:
    """一元二次方程求解器"""

    EPSILON = 1e-10

    @staticmethod
    def solve(a: float, b: float, c: float) -> dict:
        """
        求解一元二次方程 ax² + bx + c = 0

        Args:
            a: 二次项系数（不能为0）
            b: 一次项系数
            c: 常数项

        Returns:
            dict: {
                "type": "real_distinct" | "real_equal" | "complex",
                "roots": [str, str] 或 [str],
                "discriminant": float
            }

        Raises:
            ValueError: 当 a == 0 时
        """
        QuadraticSolver._validate_a(a)
        discriminant = QuadraticSolver._calculate_discriminant(a, b, c)

        if discriminant > QuadraticSolver.EPSILON:
            return QuadraticSolver._solve_real_distinct(a, b, discriminant)
        elif abs(discriminant) <= QuadraticSolver.EPSILON:
            return QuadraticSolver._solve_real_equal(a, b)
        else:
            return QuadraticSolver._solve_complex(a, b, discriminant)

    @staticmethod
    def _validate_a(a: float) -> None:
        """校验二次项系数 a 不为 0"""
        if abs(a) < QuadraticSolver.EPSILON:
            raise ValueError(
                f"参数 a 不能为 0，当前 a = {a}，方程退化为一次方程"
            )

    @staticmethod
    def _calculate_discriminant(a: float, b: float, c: float) -> float:
        """计算判别式 Δ = b² - 4ac"""
        return b * b - 4 * a * c

    @staticmethod
    def _solve_real_distinct(a: float, b: float, discriminant: float) -> dict:
        """求解 Δ > 0 时的两个不等实根"""
        sqrt_delta = math.sqrt(discriminant)
        root1 = (-b + sqrt_delta) / (2 * a)
        root2 = (-b - sqrt_delta) / (2 * a)
        return {
            "type": "real_distinct",
            "roots": [str(root1), str(root2)],
            "discriminant": discriminant,
        }

    @staticmethod
    def _solve_real_equal(a: float, b: float) -> dict:
        """求解 Δ = 0 时的重根"""
        root = -b / (2 * a)
        return {
            "type": "real_equal",
            "roots": [str(root)],
            "discriminant": 0.0,
        }

    @staticmethod
    def _solve_complex(a: float, b: float, discriminant: float) -> dict:
        """求解 Δ < 0 时的共轭虚根"""
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-discriminant) / (2 * a)

        # 格式化虚部
        if abs(imag_part - 1.0) < QuadraticSolver.EPSILON:
            imag_str = "i"
        else:
            imag_str = f"{imag_part}i"

        # 格式化实部
        if abs(real_part) < QuadraticSolver.EPSILON:
            root1 = imag_str
            root2 = f"-{imag_str}" if imag_str != "i" else "-i"
        else:
            root1 = f"{real_part}+{imag_part}i"
            root2 = f"{real_part}-{imag_part}i"

        return {
            "type": "complex",
            "roots": [root1, root2],
            "discriminant": discriminant,
        }
