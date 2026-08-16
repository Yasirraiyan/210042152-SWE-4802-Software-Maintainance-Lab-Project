1. Project Overview

Math Problem Solver is a Python-based mathematical calculation application. The project initially provides basic and advanced mathematical operations through a command-line interface and is later adapted and improved through different software maintenance activities.

The project demonstrates the four major categories of software maintenance:

Corrective Maintenance
Adaptive Maintenance
Preventive Maintenance
Perfective Maintenance

The project also demonstrates the practical use of four software transformation and analysis tools:

Loguru
PySnooper
VizTracer
SnakeViz

These tools were applied to understand program behavior, execution flow, debugging information, logging, and performance characteristics.

2. Initial System — V1 Baseline

The initial version of the application provides:

Basic arithmetic operations
Advanced mathematical operations
Input validation
Result formatting
Logging
Unit testing
Integration testing
Initial Project Structure
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
3. Corrective Maintenance
3.1 Purpose

Corrective maintenance is performed to identify and fix defects discovered after the software has been developed.

In this project, a defect was identified in the mathematical calculation functionality. The application could produce a ZeroDivisionError when the user attempted to divide a number by zero.

3.2 Correction

Validation was added to prevent division by zero.

Example:

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

This prevents the application from unexpectedly crashing.

3.3 Testing

Before corrective maintenance:

Ran 10 tests
OK

After corrective maintenance:

Ran 11 tests
OK

Therefore, the corrective change was verified using automated testing.

3.4 Version Change
V1
 ↓
Corrective Maintenance
 ↓
V1.1
4. Adaptive Maintenance
4.1 Purpose

Adaptive maintenance modifies software so that it can work in a changed environment or support new requirements.

The original application was primarily command-line based. To make the application accessible through a web browser, a Flask-based web interface was introduced.

4.2 Implementation

The application was adapted to provide a web interface.

The Flask application allows users to interact with the mathematical operations through a browser instead of using only the command line.

Example:

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
4.3 Benefit

The adaptive maintenance provides:

Browser-based access
Improved user interaction
A graphical interface
Better accessibility
Compatibility with a web-based environment
4.4 Version Change
V1.1
 ↓
Adaptive Maintenance
 ↓
V1.2
5. Preventive Maintenance
5.1 Purpose

Preventive maintenance improves the internal quality of software to reduce the possibility of future problems.

The following improvements were introduced:

Better input validation
Type hints
Improved error handling
Cleaner code structure
More maintainable functions

Example:

def add(a: float, b: float) -> float:
    return a + b

Type hints make the expected input and output clearer.

5.2 Validation

Input validation was improved to prevent invalid data from reaching the calculation functions.

This helps reduce future errors and makes the software easier to maintain.

5.3 Version Change
V1.2
 ↓
Preventive Maintenance
 ↓
V1.3
6. Perfective Maintenance
6.1 Purpose

Perfective maintenance improves existing software by adding useful functionality or improving the user experience.

Additional mathematical operations were introduced:

Factorial
Percentage
Square root
Cube root
Power

The final application therefore supports a wider range of mathematical operations.

6.2 Final Functionality
Addition
Subtraction
Multiplication
Division
Power
Square Root
Cube Root
Factorial
Percentage
6.3 Testing

After the improvements, the complete test suite was executed.

Ran 16 tests
OK

This confirms that the implemented functionality was tested successfully.

6.4 Version Change
V1.3
 ↓
Perfective Maintenance
 ↓
V2.0
7. Transformation and Analysis Tools

The project also uses four tools for software analysis and maintenance:

Loguru
PySnooper
VizTracer
SnakeViz

These tools provide different types of information about the application.

8. Loguru
8.1 Introduction

Loguru is a Python logging library that provides a simple and convenient way to generate application logs.

In this project, Loguru was used to monitor mathematical operations.

Example:

from loguru import logger


logger.add("logs/math_solver.log")


logger.info("Starting mathematical calculation")


result = add(4, 3)


logger.info(f"Addition result: {result}")
8.2 Usage in the Project

Loguru was used to record:

Operation execution
Calculation results
Errors
Program activities
Debugging information

For example:

[INFO] Starting mathematical calculation
[INFO] Addition operation performed
[INFO] Addition result: 7
8.3 Insight from Output

The Loguru output provides a chronological record of what happened during program execution.

For example:

[LOG] Addition operation performed
Addition result: 7.0

This tells us that:

The addition operation was executed.
The operation completed successfully.
The calculated result was 7.0.

If an error occurs, the log can help identify where the problem occurred.

8.4 Maintenance Use

Loguru is useful for corrective maintenance.

For example, if users report that division is not working, developers can inspect the log to determine whether:

The division function was called.
Invalid input was received.
Division by zero occurred.
The calculation returned an unexpected value.
9. PySnooper
9.1 Introduction

PySnooper is a debugging and tracing tool for Python.

It automatically records the execution of a function, including:

Function entry
Variable values
Line execution
Function return values
9.2 Usage in the Project

PySnooper was used to trace mathematical calculations.

Example:

import pysnooper


@pysnooper.snoop()
def calculate(a, b):
    result = a + b
    return result

When the function executes, PySnooper generates a trace showing how the variables change.

9.3 Insight from Output

A PySnooper trace can show information such as:

Starting var: a = 4
Starting var: b = 3
New var: result = 7
Return value: 7

This helps the developer understand the internal execution flow.

9.4 Maintenance Use

PySnooper can be used during corrective maintenance when a calculation produces an unexpected result.

Instead of adding many print() statements manually, PySnooper automatically records the execution details.

10. VizTracer
10.1 Introduction

VizTracer is a Python execution tracing tool that records program execution and produces a trace that can be visualized.

It can help developers understand:

Function calls
Execution sequence
Execution duration
Program behavior
Performance-related information
10.2 Usage in the Project

VizTracer was used to trace the Math Problem Solver application.

Example command:

viztracer analysis/viztrace_demo.py

The tool generates a trace file such as:

result.json

The generated trace can then be opened and inspected using the VizTracer viewer.

10.3 Insight from Output

The trace provides a visual representation of program execution.

It can help identify:

Which functions were executed
The order in which functions were called
Functions that take comparatively longer
Repeated function calls
The overall execution flow

For example:

main()
  ↓
add()
  ↓
result
  ↓
logger

This provides a clearer understanding of how different parts of the application interact.

10.4 Maintenance Use

VizTracer can support preventive and corrective maintenance.

If a future version becomes slower, the trace can help developers identify functions that require optimization.

11. SnakeViz
11.1 Introduction

SnakeViz is a visualization tool for Python profiling data generated by cProfile.

It provides a graphical representation of function execution and performance.

11.2 Usage in the Project

The project was profiled using Python's cProfile.

Example:

python -m cProfile -o profile.prof analysis/profile_demo.py

Then SnakeViz was used:

snakeviz profile.prof
11.3 Insight from Output

SnakeViz provides a visual representation of profiling information.

The visualization can show:

Function calls
Number of calls
Total execution time
Cumulative execution time
Functions consuming more execution time

For example, if a function appears as a major portion of the visualization, it may be a candidate for optimization.

11.4 Maintenance Use

SnakeViz is especially useful for preventive and perfective maintenance.

For example, if the application becomes slow after adding new mathematical operations, profiling can help identify performance bottlenecks.

Developers can then optimize the relevant functions.

12. Comparison of the Four Tools
Tool	Main Purpose	Project Usage
Loguru	Logging	Recorded application events and errors
PySnooper	Debugging/tracing	Traced variables and function execution
VizTracer	Execution tracing	Visualized program execution
SnakeViz	Performance profiling	Visualized profiling information

Each tool provides different information.

Loguru focuses on logging, PySnooper focuses on detailed execution tracing, VizTracer focuses on visual execution traces, and SnakeViz focuses on profiling and performance analysis.

13. Alternative Tools

There are several alternative tools that can provide similar functionality.

13.1 Alternatives to Loguru
Python logging
Structlog
Logbook

Python's built-in logging module is widely used and does not require an external dependency.

13.2 Alternatives to PySnooper
Python debugger (pdb)
VS Code Debugger
breakpoint()

The VS Code debugger is particularly useful because it provides breakpoints, variable inspection, and step-by-step execution.

13.3 Alternatives to VizTracer
Pyinstrument
cProfile
Yappi

These tools can provide different forms of execution and performance analysis.

13.4 Alternatives to SnakeViz
Py-Spy
Pyinstrument
Tuna
cProfile with other visualization tools
14. Preferred Tools

For this project, the preferred tools would be:

Loguru

Loguru is preferred for application logging because it provides a simple syntax and readable log output.

VS Code Debugger

For debugging, the VS Code debugger would be preferred because it allows developers to:

Set breakpoints
Inspect variables
Step through code
Identify errors interactively
VizTracer

VizTracer is useful when a detailed view of program execution is required.

SnakeViz

SnakeViz is useful for quickly understanding profiling results and identifying performance bottlenecks.

15. Transformation Tools in Software Maintenance

The four tools can be applied to different maintenance activities.

Maintenance Type	Tool	Example
Corrective	Loguru	Find errors from application logs
Corrective	PySnooper	Trace incorrect calculations
Preventive	VizTracer	Analyze execution flow
Preventive	SnakeViz	Identify performance bottlenecks
Perfective	SnakeViz	Optimize newly added features
Adaptive	Loguru	Monitor new web-based functionality

Therefore, these tools help developers understand the existing system before making maintenance changes.

16. Overall Maintenance Evolution

The complete evolution of the project can be represented as:

                    Math Problem Solver
                           │
                           ▼
                       V1 Baseline
                           │
                           ▼
                  Corrective Maintenance
                           │
                           ▼
                          V1.1
                           │
                           ▼
                   Adaptive Maintenance
                           │
                           ▼
                          V1.2
                           │
                           ▼
                  Preventive Maintenance
                           │
                           ▼
                          V1.3
                           │
                           ▼
                   Perfective Maintenance
                           │
                           ▼
                          V2.0
                           │
                           ▼
              Analysis & Transformation Tools
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       Loguru          PySnooper        VizTracer
                                             │
                                             ▼
                                         SnakeViz
17. Testing Result

The final project was tested using the Python unittest framework.

Command:

python -m unittest discover -s tests -p "test_*.py"

Final result:

................
----------------------------------------------------------------------
Ran 16 tests in 0.002s


OK

This demonstrates that all 16 automated tests passed successfully.

18. Conclusion

The Math Problem Solver project demonstrates how software can evolve through different software maintenance activities.

Corrective maintenance was used to fix defects such as division-by-zero problems. Adaptive maintenance introduced a web-based environment using Flask. Preventive maintenance improved validation, type hints, error handling, and code quality. Perfective maintenance introduced additional mathematical functionality such as factorial and percentage calculations.

The project also demonstrates the practical use of Loguru, PySnooper, VizTracer, and SnakeViz. Loguru provides application logs, PySnooper helps trace program execution and variables, VizTracer provides detailed execution traces, and SnakeViz helps visualize profiling information.

Together, these tools provide useful information for debugging, understanding program behavior, identifying performance problems, and supporting future software maintenance.

The final system successfully passed 16 automated tests, demonstrating that the maintenance changes and additional functionality were verified through testing.
