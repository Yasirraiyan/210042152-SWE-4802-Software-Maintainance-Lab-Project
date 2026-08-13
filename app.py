from flask import Flask, render_template, request

from calculator.basic import add, subtract, multiply, divide
from calculator.advanced import (
    square_root,
    cube_root,
    power,
    factorial,
    percentage
)
from calculator.validator import validate_number


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        operation = request.form.get("operation")

        try:
            if operation in [
                "add",
                "subtract",
                "multiply",
                "divide",
                "power",
                "percentage"
            ]:
                a = validate_number(request.form.get("number1"))
                b = validate_number(request.form.get("number2"))

                if operation == "add":
                    result = add(a, b)

                elif operation == "subtract":
                    result = subtract(a, b)

                elif operation == "multiply":
                    result = multiply(a, b)

                elif operation == "divide":
                    result = divide(a, b)

                elif operation == "power":
                    result = power(a, b)

                elif operation == "percentage":
                    result = percentage(a, b)

            elif operation == "square_root":
                a = validate_number(request.form.get("number1"))
                result = square_root(a)

            elif operation == "cube_root":
                a = validate_number(request.form.get("number1"))
                result = cube_root(a)

            elif operation == "factorial":
                a = validate_number(request.form.get("number1"))
                result = factorial(a)

        except ValueError as e:
            error = str(e)

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)