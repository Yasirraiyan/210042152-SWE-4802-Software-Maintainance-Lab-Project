# Math Problem Solver — Software Maintenance Project

## 1. Project Overview

**Math Problem Solver** is a Python-based mathematical calculation application developed as a Software Maintenance project.

The project initially provides mathematical operations through a command-line interface and is gradually improved through different types of software maintenance activities.

The project demonstrates the four major categories of software maintenance:

1. **Corrective Maintenance**
2. **Adaptive Maintenance**
3. **Preventive Maintenance**
4. **Perfective Maintenance**

The project also demonstrates the practical use of four software transformation, debugging, tracing, logging, and performance-analysis tools:

1. **Loguru**
2. **PySnooper**
3. **VizTracer**
4. **SnakeViz**

These tools were applied to the project to understand program behavior, execution flow, debugging information, logging, and performance characteristics.

---

# 2. Project Objectives

The main objectives of this project are:

- **To develop and maintain a mathematical calculation application.**
- **To demonstrate different types of software maintenance.**
- **To identify and correct software defects.**
- **To adapt the application to a web-based environment.**
- **To improve code quality and maintainability.**
- **To add new mathematical features.**
- **To use software analysis and transformation tools in a real project.**
- **To understand program execution and performance.**
- **To perform automated testing after maintenance activities.**

---

# 3. Technologies Used

The project uses the following technologies and tools:

10. Perfective Maintenance
10.1 Definition

Perfective maintenance improves existing software by adding useful features or improving functionality.

10.2 Perfective Maintenance in This Project

Additional mathematical operations were added to improve the functionality of the application.

The final system supports:

Addition
Subtraction
Multiplication
Division
Power
Square Root
Cube Root
Factorial
Percentage
10.3 Benefits

The new functionality makes the application more useful and provides users with a wider range of mathematical calculations.

10.4 Testing

After adding the new features, the complete test suite was executed.

V1.1
 ↓
Adaptive Maintenance
 ↓
V1.2

| Technology / Tool | Purpose |
|---|---|
| **Python** | Main programming language |
| **Flask** | Web-based adaptation |
| **unittest** | Automated testing |
| **Loguru** | Application logging |
| **PySnooper** | Debugging and execution tracing |
| **VizTracer** | Program execution tracing |
| **cProfile** | Python performance profiling |
| **SnakeViz** | Visualization of profiling results |
| **Git** | Version control |
| **GitHub** | Source-code repository |
| **VS Code** | Development environment |

---

# 4. Initial System — V1 Baseline

The initial version of the application provides mathematical calculation functionality.

The baseline system includes:

- **Basic arithmetic operations**
- **Advanced mathematical operations**
- **Input validation**
- **Result calculation**
- **Logging**
- **Unit testing**
- **Integration testing**

The project was initially developed as a command-line application.

---

# 5. Project Structure

The project is organized into separate modules for calculations, testing, analysis, and application functionality.
Math-Problem-Solver/
│
├── app.py
├── main.py
│
├── calculator/
│   ├── basic.py
│   ├── advanced.py
│   └── validator.py
│
├── utils/
│   ├── logger.py
│   └── formatter.py
│
├── tests/
│   ├── test_basic.py
│   ├── test_advanced.py
│   ├── test_validator.py
│   └── test_integration.py
│
├── analysis/
│   ├── logging_demo.py
│   ├── pysnooper_demo.py
│   ├── viztrace_demo.py
│   └── profile_demo.py
│
├── templates/
│   └── index.html
│
├── requirements.txt
└── README.md

6. Software Maintenance Activities

The project demonstrates four major types of software maintenance.

                    Math Problem Solver
                           |
                           v
                       V1 Baseline
                           |
                           v
                  Corrective Maintenance
                           |
                           v
                          V1.1
                           |
                           v
                   Adaptive Maintenance
                           |
                           v
                          V1.2
                           |
                           v
                  Preventive Maintenance
                           |
                           v
                          V1.3
                           |
                           v
                   Perfective Maintenance
                           |
                           v
                          V2.0


7. Corrective Maintenance
7.1 Definition

Corrective maintenance is performed to identify and fix defects or errors found in existing software.

7.2 Corrective Maintenance in This Project

During the development of the Math Problem Solver, a problem was identified in the division functionality.

If the user attempted to divide a number by zero, the program could produce a ZeroDivisionError.

The problem was corrected by adding validation.

Example:

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

    7.3 Result

The application now handles division-by-zero situations more safely instead of allowing the program to terminate unexpectedly.

7.4 Testing

Before corrective maintenance:

Ran 10 tests
OK

After corrective maintenance:
Ran 11 tests
OK

Therefore, the corrective maintenance was verified using automated tests.

7.5 Version Evolution

V1
 ↓
Corrective Maintenance
 ↓
V1.1

8. Adaptive Maintenance
8.1 Definition

Adaptive maintenance modifies software so that it can work in a changed environment or support new requirements.

8.2 Adaptive Maintenance in This Project

The original application was primarily command-line based.

To adapt the application to a web-based environment, a Flask-based web interface was introduced.

The application can therefore be accessed through a browser instead of depending only on command-line interaction.

Example:
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

    8.3 Benefits

The adaptive maintenance provides:

Browser-based access
Improved user interaction
Web-based interface
Better accessibility
Adaptation to a new execution environment
8.4 Version Evolution

9. Preventive Maintenance
9.1 Definition

Preventive maintenance improves the internal quality of software to reduce the possibility of future failures.

9.2 Preventive Maintenance in This Project

The project was improved through:

Better input validation
Type hints
Improved error handling
Cleaner code organization
Improved maintainability

Example:

def add(a: float, b: float) -> float:
    return a + b

    Type hints make the expected input and output types clearer.

9.3 Benefits

Preventive maintenance helps:

Reduce future errors
Improve code readability
Improve maintainability
Make debugging easier
Improve software reliability
9.4 Version Evolution

V1.2
 ↓
Preventive Maintenance
 ↓
V1.3

................
----------------------------------------------------------------------
Ran 16 tests in 0.002s

OK

This confirms that all 16 automated tests passed successfully.

10.5 Version Evolution

V1.3
 ↓
Perfective Maintenance
 ↓
V2.0
