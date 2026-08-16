from loguru import logger
from calculator.basic import add, subtract, multiply, divide

logger.add("analysis/math_operations.log", rotation="500 KB")

def run_operations():
    logger.info("Starting math operations")

    result1 = add(10, 5)
    logger.info(f"Addition: {result1}")

    result2 = subtract(10, 5)
    logger.info(f"Subtraction: {result2}")

    result3 = multiply(10, 5)
    logger.info(f"Multiplication: {result3}")

    result4 = divide(10, 5)
    logger.info(f"Division: {result4}")

    logger.info("Math operations completed")

if __name__ == "__main__":
    run_operations()