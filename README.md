# 一元二次方程求解器 — 软件质量与测试课程项目

## 项目简介

本项目实现一元二次方程 ax² + bx + c = 0 的求解功能，分别用 **Python** 和 **Java** 两种语言实现，并包含完整的黑盒测试和白盒测试。

## 项目结构

```
Project1/
├── README.md
├── .gitignore
├── docs/
│   └── test-report.md
├── python/
│   ├── src/quadratic_solver.py
│   ├── tests/
│   │   ├── test_blackbox.py
│   │   └── test_whitebox.py
│   └── requirements.txt
└── java/
    ├── src/main/java/quadratic/QuadraticSolver.java
    ├── src/test/java/quadratic/
    │   ├── BlackBoxTest.java
    │   └── WhiteBoxTest.java
    └── pom.xml
```

## 环境配置

### Python

```bash
cd python
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
pip install -r requirements.txt
pytest -v                    # 运行测试
```

### Java

```bash
cd java
mvn test                     # 运行测试
```

## 团队分工

| 成员 | 职责 |
|------|------|
| 组长 | Python 开发 + 测试 + 项目管理 |
| 成员A | Java 开发 + 测试 |
| 成员B | 代码审查 + 测试报告 |

## 测试用例

详见 `docs/test-report.md`
