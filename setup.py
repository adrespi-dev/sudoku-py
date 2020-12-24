from setuptools import find_packages, setup

setup(
    name="sudoku-validator",
    version="1.0.0",
    author="Lemontech S.A",
    author_email="aespinoza@lemontech.com",
    packages=find_packages(),
    test_suite="test",
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "pytest",
        "pytest-timeout",
    ],
)
