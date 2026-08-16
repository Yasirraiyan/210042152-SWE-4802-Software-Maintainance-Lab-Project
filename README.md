# Math Problem Solver — Software Maintenance Project

## 1. Project Overview

Math Problem Solver is a Python-based mathematical calculation application. The project initially provides basic and advanced mathematical operations through a command-line interface and is later adapted and improved through different software maintenance activities.

The project demonstrates the four major categories of software maintenance:

1. Corrective Maintenance
2. Adaptive Maintenance
3. Preventive Maintenance
4. Perfective Maintenance

The project also demonstrates the practical use of four software transformation and analysis tools:

1. Loguru
2. PySnooper
3. VizTracer
4. SnakeViz

These tools were applied to understand program behavior, execution flow, debugging information, logging, and performance characteristics.

---

# 2. Initial System — V1 Baseline

The initial version of the application provides:

- Basic arithmetic operations
- Advanced mathematical operations
- Input validation
- Result formatting
- Logging
- Unit testing
- Integration testing

## Initial Project Structure

```text
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


Baseline Testing

The initial version successfully passed:

Ran 10 tests
OK
3. Corrective Maintenance
Scenario

A defect was identified in the division operation. When the denominator was zero, the application produced a ZeroDivisionError.

Change ID

CM-001

3.1 Program Comprehension

The existing calculation flow was analyzed:

User
  ↓
main.py
  ↓
calculator/basic.py
  ↓
divide(a, b)
  ↓
a / b

The divide() function was identified as the source of the problem.

3.2 Change Management
Problem

Division by zero caused the application to crash.

Requested Change

Prevent division by zero and provide a meaningful error message.

Change Implemented

The divide() function was modified to validate the denominator before performing the calculation.

3.3 Impact Analysis

Affected components:

calculator/basic.py  → Direct impact
main.py              → Indirect impact
tests/test_basic.py  → Regression test
3.4 Reverse Engineering

The original execution flow was reconstructed:

User
  ↓
Select Division
  ↓
main.py
  ↓
divide(a, b)
  ↓
Denominator = 0
  ↓
ZeroDivisionError
3.5 Refactoring

The division function was changed to:

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

A regression test was added:

def test_divide_by_zero(self):
    with self.assertRaises(ValueError):
        divide(10, 0)
Testing Result
Ran 11 tests
OK
Version
V1
 ↓
Corrective Maintenance
 ↓
V1.1
4. Adaptive Maintenance
Scenario

The original application was command-line based. The system needed to be adapted so that users could access it through a web browser.

Change ID

CM-002

4.1 Program Comprehension

The existing architecture was analyzed:

User
  ↓
main.py
  ↓
Calculator Modules
  ↓
Result

The calculation modules were already separated from the main application logic and could therefore be reused.

4.2 Change Management
Requirement

Adapt the existing command-line application to a web-based environment.

Change Implemented

A Flask web interface was introduced while reusing the existing calculator modules.

Technology Added
Flask
HTML
Web interface
4.3 Impact Analysis

Affected components:

app.py                → Web application
requirements.txt      → Flask dependency
templates/index.html  → Web interface

Reused components:

calculator/basic.py
calculator/advanced.py
calculator/validator.py
4.4 Reverse Engineering

Existing flow:

CLI
 ↓
main.py
 ↓
Validation
 ↓
Calculator Function
 ↓
Result

Adapted flow:

Browser
 ↓
index.html
 ↓
app.py
 ↓
Validation
 ↓
Calculator Function
 ↓
Result
 ↓
Browser
4.5 Refactoring

A Flask web interface was added without rewriting the existing calculator logic.

Browser
  ↓
Flask app.py
  ↓
calculator/
 ├── basic.py
 ├── advanced.py
 └── validator.py
  ↓
Result

The Math Problem Solver can now be accessed through a web browser.

Version
V1.1
 ↓
Adaptive Maintenance
 ↓
V1.2
5. Preventive Maintenance
Scenario

The application was working correctly, but improvements were required to prevent future defects and make the system easier to maintain.

Change ID

CM-003

5.1 Program Comprehension

The existing project structure and dependencies were analyzed.

The following areas were identified for improvement:

Input validation
Error handling
Code readability
Type information
Test coverage
5.2 Change Management
Objective

Improve the maintainability, reliability, and readability of the system.

Changes Implemented
Improved input validation
Added type hints
Improved error handling
Added mathematical input validation
Added additional tests
5.3 Impact Analysis

Affected components:

calculator/validator.py → High impact
calculator/basic.py     → Medium impact
calculator/advanced.py  → Medium impact
tests/test_validator.py → High impact
tests/test_advanced.py  → High impact

The intended functionality of the calculator was preserved.

5.4 Reverse Engineering

The validation flow was analyzed:

User Input
  ↓
validate_number()
  ↓
Convert to number
  ↓
Calculator
  ↓
Result

Potential invalid inputs were identified before they could cause unexpected behavior.

5.5 Refactoring

The validation function was improved with type hints and better exception handling:

def validate_number(value: str) -> float:
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(
            "Invalid number. Please enter a valid number."
        )

The advanced calculator was also improved to handle invalid square-root and factorial inputs.

Additional validation tests were added.

Result

The software became easier to understand, maintain, and extend while preserving its existing behavior.

Version
V1.2
 ↓
Preventive Maintenance
 ↓
V1.3
6. Perfective Maintenance
Scenario

Users requested additional mathematical functionality and an improved web experience.

Change ID

CM-004

6.1 Program Comprehension

The existing advanced calculator and web application were analyzed to determine where the new features should be integrated.

Browser
  ↓
app.py
  ↓
Calculator Module
  ↓
Result
6.2 Change Management
User Requirements

Users requested:

Percentage calculation
Factorial calculation
Improved operation selection
Objective

Improve the functionality and user experience of the application.

6.3 Impact Analysis

Affected components:

calculator/advanced.py
app.py
templates/index.html
tests/test_advanced.py

Existing basic calculator functionality remained unchanged.

6.4 Reverse Engineering

The existing feature flow was analyzed:

Browser
  ↓
app.py
  ↓
Operation Selection
  ↓
Calculator Function
  ↓
Result

The new features were integrated into the existing architecture.

6.5 Refactoring

Two new mathematical operations were added.

Factorial
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError(
            "Factorial is not defined for negative numbers."
        )


    if not float(n).is_integer():
        raise ValueError(
            "Factorial requires a whole number."
        )


    return math.factorial(int(n))
Percentage
def percentage(value: float, percent: float) -> float:
    return (value * percent) / 100

The web interface was updated to allow users to select the new operations.

Result

The application now supports:

Addition
Subtraction
Multiplication
Division
Power
Square Root
Cube Root
Factorial
Percentage
Testing Result
Ran 16 tests
OK
Version
V1.3
 ↓
Perfective Maintenance
 ↓
V2.0
7. Overall Maintenance History
Initial V1 Baseline
        ↓
Corrective Maintenance
Fix division by zero
        ↓
V1.1
        ↓
Adaptive Maintenance
Add Flask web interface
        ↓
V1.2
        ↓
Preventive Maintenance
Improve validation and code quality
        ↓
V1.3
        ↓
Perfective Maintenance
Add percentage and factorial
        ↓
V2.0
8. Testing Results
Stage	Result
Initial V1 Baseline	10 tests passed
Corrective Maintenance	11 tests passed
Preventive Maintenance	Tests passed
Perfective Maintenance	16 tests passed
Final Test Command
python -m unittest discover -s tests -p "test_*.py"
Final Result
................
----------------------------------------------------------------------
Ran 16 tests in 0.002s


OK
9. Transformation and Software Analysis Tools

Four transformation and software analysis tools were applied to the Math Problem Solver project:

Loguru
PySnooper
VizTracer
SnakeViz

These tools were used to understand:

Program behavior
Execution flow
Debugging information
Logging
Performance characteristics
10. Loguru
10.1 Purpose

Loguru is a Python logging library used to record important events during program execution.

10.2 Usage in the Project

Loguru was integrated into the Math Problem Solver to record mathematical operations performed by the application.

For example, when the user performs an addition operation:

[LOG] Addition operation performed
Addition result: 7.0
10.3 Output Insight

The Loguru output confirms that:

The application received the requested operation.
The corresponding calculator function was executed.
A log message was generated.
The calculation completed successfully.
Figure 1: Loguru Execution Output

Insert your Loguru screenshot here.

[Add your screenshot]
10.4 Maintenance Use

Loguru is useful during corrective maintenance because developers can inspect application logs when users report unexpected behavior.

For example, if a calculation fails, the log can help identify which operation was executed before the failure.

11. PySnooper
11.1 Purpose

PySnooper is a debugging and execution-tracing tool that shows what happens inside Python functions while they are running.

11.2 Usage in the Project

PySnooper was applied to the mathematical functions of the Math Problem Solver.

It was used to observe:

Function calls
Input values
Variable changes
Executed statements
Return values

Example:

Function call
     ↓
Input values
     ↓
Variable changes
     ↓
Calculation
     ↓
Return value
11.3 Output Insight

The PySnooper output provides a detailed view of the internal execution flow.

It helps developers understand how input values move through the calculation function and how the final result is produced.

Figure 2: PySnooper Execution Trace

Insert your PySnooper screenshot here.

[Add your screenshot]
11.4 Maintenance Use

PySnooper can be used during corrective maintenance when a function produces an unexpected result.

It can help investigate problems in:

divide()
square_root()
cube_root()
factorial()
percentage()
12. VizTracer
12.1 Purpose

VizTracer is an execution-tracing and performance-analysis tool for Python applications.

12.2 Usage in the Project

VizTracer was used to trace the execution of the Math Problem Solver application.

The application was executed through VizTracer, and the generated trace was opened using the VizTracer viewer.

The trace provides information about:

Function calls
Execution sequence
Function duration
Program execution flow
Performance behavior
12.3 Output Insight

The VizTracer visualization provides a timeline of program execution.

It allows developers to see:

Which functions were called
When functions were called
How long different parts of the program took
How execution progressed
Figure 3: VizTracer Execution Timeline

Insert your VizTracer screenshot here.

[Add your screenshot]
12.4 Maintenance Use

VizTracer is useful for performance-related maintenance.

For example, if a new feature causes the Math Problem Solver to become slower, VizTracer can help identify the functions responsible for the increased execution time.

It can support:

Performance optimization
Identifying slow functions
Understanding complex execution flows
Comparing execution behavior before and after modifications
13. SnakeViz
13.1 Purpose

SnakeViz is a graphical visualization tool for Python profiling data generated using cProfile.

13.2 Usage in the Project

The Math Problem Solver was profiled using Python's cProfile.

The profiling process generated information about:

Function calls
Number of calls
Execution time

The generated profiling data was then visualized using SnakeViz.

13.3 Output Insight

The SnakeViz visualization helps identify:

Frequently executed functions
Function execution time
Number of function calls
Functions consuming more processing time
Potential performance bottlenecks
Figure 4: SnakeViz Profiling Visualization

Insert your SnakeViz screenshot here.

[Add your screenshot]
13.4 Maintenance Use

SnakeViz can be used during performance-oriented maintenance.

For example, after adding new functionality such as factorial and percentage calculations, developers can profile the application to determine whether any function introduces unnecessary execution overhead.

14. Comparison of Transformation Tools
Tool	Main Purpose	Main Output	Maintenance Use
Loguru	Logging	Log messages	Error monitoring and debugging
PySnooper	Execution tracing	Line-by-line trace	Debugging functions
VizTracer	Execution/performance tracing	Timeline visualization	Performance analysis
SnakeViz	Profiling visualization	Graphical profile	Finding performance bottlenecks
15. Alternative Tools

There are several alternatives to the tools used in this project.

Used Tool	Alternative Tools
Loguru	Python logging, Structlog
PySnooper	pdb, debugpy
VizTracer	Pyinstrument, cProfile
SnakeViz	Py-Spy, Tuna
16. Preferred Tools

For a real software project, Loguru would be preferred for application logging because it provides simple and readable logging.

For performance analysis, VizTracer would be preferred because its timeline visualization makes it easier to understand function execution and identify performance problems.

For debugging, PySnooper is useful when a developer needs to understand the internal execution of a particular function.

For profiling, SnakeViz is useful when a graphical representation of profiling data is required.

17. Overall Insight from the Tools

The four tools provide different perspectives of the same Math Problem Solver application.

                 Math Problem Solver
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       Loguru        PySnooper       Profiling
          │              │              │
         Logs       Line-by-line        │
                       Trace       ┌────┴─────┐
                                  │          │
                              VizTracer   SnakeViz
                              Timeline      Profile

The tools provide different types of information:

Loguru
   ↓
What happened?


PySnooper
   ↓
How did the function execute?


VizTracer
   ↓
How did execution progress over time?


SnakeViz
   ↓
Where did the program spend its processing time?

Together, these tools provide useful information for software maintenance.

They help developers:

Understand program behavior
Debug problems
Trace execution
Monitor application events
Analyze performance
Identify bottlenecks
Maintain existing software
Evaluate the impact of modifications
18. Example of Transformation Tools in Maintenance

Consider the following maintenance scenario.

Suppose the factorial feature introduced during perfective maintenance becomes slow for a particular input.

The developer can use the tools as follows:

Step 1 — Loguru

Check the application log:

[LOG] Factorial operation performed

This confirms that the factorial operation was requested.

Step 2 — PySnooper

Trace the factorial function to understand the internal execution.

Function call
     ↓
Input
     ↓
Validation
     ↓
Calculation
     ↓
Return
Step 3 — VizTracer

Run the application with VizTracer to identify the execution timeline and determine which function consumes more time.

Step 4 — SnakeViz

Generate profiling information using cProfile and open it with SnakeViz.

This helps identify functions with high execution time or excessive calls.

Maintenance Decision

Based on the results, the developer can:

Refactor the function
Reduce unnecessary calculations
Improve validation
Optimize expensive operations
Add regression tests

Therefore, the tools can be used together during software maintenance rather than independently.

19. Git Maintenance History

The project maintenance was organized into separate Git commits:

Initial V1 baseline
        ↓
Corrective maintenance:
fix division by zero
        ↓
Adaptive maintenance:
add Flask web interface
        ↓
Preventive maintenance:
improve validation and code quality
        ↓
Perfective maintenance:
add percentage and factorial
        ↓
Transformation tools:
Loguru + PySnooper + VizTracer + SnakeViz
        ↓
Complete software maintenance documentation
20. Final Conclusion

The Math Problem Solver project was successfully used to demonstrate the four major categories of software maintenance:

Corrective Maintenance
Adaptive Maintenance
Preventive Maintenance
Perfective Maintenance

Corrective maintenance fixed the division-by-zero defect.

Adaptive maintenance adapted the application from a command-line environment to a web-based environment.

Preventive maintenance improved validation, error handling, type hints, and testing.

Perfective maintenance enhanced the application by adding factorial and percentage calculations.

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

The final project successfully passed:

Ran 16 tests
OK

In addition, four transformation and software analysis tools were applied:

Loguru
PySnooper
VizTracer
SnakeViz

These tools provided:

Loguru     → Logging
PySnooper  → Debugging and execution tracing
VizTracer  → Execution timeline and performance analysis
SnakeViz   → Profiling visualization

The practical use of these tools demonstrates how software analysis and transformation tools can support software maintenance.

They help developers understand existing code, investigate defects, trace execution, monitor application behavior, identify performance bottlenecks, and make informed maintenance decisions.

Therefore, the Math Problem Solver demonstrates a complete software maintenance lifecycle from V1 to V2.0 together with practical application of transformation and software analysis tools.



### Important


Your **four screenshots/figures should be inserted** where I marked:


1. **Figure 1 → Loguru output**
2. **Figure 2 → PySnooper trace**
3. **Figure 3 → VizTracer timeline**
4. **Figure 4 → SnakeViz visualization**


This matches the assignment requirement to **use the tools in your project, explain the output insight, give maintenance examples, and compare alternatives**. The uploaded project document also already records the same four tools and their respective purposes. :contentReference[oaicite:1]{index=1}


After pasting/updating `README.md`, run:


```powershell
git add README.md
git commit -m "Add transformation tools analysis"
git push
