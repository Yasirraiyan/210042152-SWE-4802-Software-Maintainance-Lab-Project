import math


def square_root(n: float) -> float:
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(n)


def cube_root(n: float) -> float:
    return n ** (1 / 3)


def power(a: float, b: float) -> float:
    return a ** b


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if not float(n).is_integer():
        raise ValueError("Factorial requires a whole number.")

    return math.factorial(int(n))


def percentage(value: float, percent: float) -> float:
    return (value * percent) / 100
