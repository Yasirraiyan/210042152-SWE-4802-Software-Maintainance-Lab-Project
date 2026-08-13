from calculator.basic import add, subtract, multiply, divide
from calculator.advanced import square_root, cube_root, power
from calculator.validator import validate_number
from utils.formatter import format_result
from utils.logger import log


def main():
    print("===== Math Problem Solver =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Cube Root")
    print("7. Power")

    choice = input("Enter your choice: ")

    if choice in ["1", "2", "3", "4", "7"]:
        a = validate_number(input("Enter first number: "))
        b = validate_number(input("Enter second number: "))

        if choice == "1":
            result = add(a, b)
            operation = "Addition"

        elif choice == "2":
            result = subtract(a, b)
            operation = "Subtraction"

        elif choice == "3":
            result = multiply(a, b)
            operation = "Multiplication"

        elif choice == "4":
            result = divide(a, b)
            operation = "Division"

        else:
            result = power(a, b)
            operation = "Power"

    elif choice == "5":
        n = validate_number(input("Enter a number: "))
        result = square_root(n)
        operation = "Square Root"

    elif choice == "6":
        n = validate_number(input("Enter a number: "))
        result = cube_root(n)
        operation = "Cube Root"

    else:
        print("Invalid choice.")
        return

    log(f"{operation} operation performed")
    print(format_result(operation, result))


if __name__ == "__main__":
    main()