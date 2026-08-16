# Math Problem Solver — Software Maintenance Project

## 1. Project Overview

Math Problem Solver is a Python-based mathematical calculation application.
The project initially provides basic and advanced mathematical operations
through a command-line interface and is later adapted and improved through
different software maintenance activities.

The project demonstrates the four major categories of software maintenance:

1. Corrective Maintenance
2. Adaptive Maintenance
3. Preventive Maintenance
4. Perfective Maintenance

For each category, the following activities were performed:

1. Program Comprehension
2. Change Management
3. Impact Analysis
4. Reverse Engineering
5. Refactoring

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
├── app.py
├── main.py
├── calculator/
│   ├── basic.py
│   ├── advanced.py
│   └── validator.py
├── utils/
│   ├── logger.py
│   └── formatter.py
├── tests/
│   ├── test_basic.py
│   ├── test_advanced.py
│   ├── test_validator.py
│   └── test_integration.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md


Baseline Testing

The initial version successfully passed:

Ran 10 tests
OK
3. Corrective Maintenance
Scenario

A defect was identified in the division operation. When the denominator
was zero, the application produced a ZeroDivisionError.

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

The divide() function was modified to validate the denominator before
performing the calculation.

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

The original application was command-line based. The system needed to be
adapted so that users could access it through a web browser.

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

The calculation modules were already separated from the main application
logic and could therefore be reused.

4.2 Change Management
Requirement

Adapt the existing command-line application to a web-based environment.

Change Implemented

A Flask web interface was introduced while reusing the existing calculator
modules.

Technology Added
Flask
HTML
Web interface
4.3 Impact Analysis

Affected components:

app.py               → Web application
requirements.txt     → Flask dependency
templates/index.html → Web interface

Reused components:

calculator/basic.py
calculator/advanced.py
calculator/validator.py
4.4 Reverse Engineering

The existing flow was analyzed:

CLI
 ↓
main.py
 ↓
Validation
 ↓
Calculator Function
 ↓
Result

The adapted flow became:

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

A Flask web interface was added without rewriting the existing calculator
logic.

The existing calculator functions are reused by app.py.

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

The application was working correctly, but improvements were required to
prevent future defects and make the system easier to maintain.

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

Potential invalid inputs were identified before they could cause
unexpected behavior.

5.5 Refactoring

The validation function was improved with type hints and better
exception handling:

def validate_number(value: str) -> float:
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(
            "Invalid number. Please enter a valid number."
        )

The advanced calculator was also improved to handle invalid square-root
and factorial inputs.

Additional validation tests were added.

Result

The software became easier to understand, maintain, and extend while
preserving its existing behavior.

Version
V1.2
 ↓
Preventive Maintenance
 ↓
V1.3
6. Perfective Maintenance
Scenario

Users requested additional mathematical functionality and an improved
web experience.

Change ID

CM-004

6.1 Program Comprehension

The existing advanced calculator and web application were analyzed to
determine where the new features should be integrated.

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

The web interface was updated to allow users to select the new
operations.

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
Ran 16 tests
OK
9. Git Maintenance History

The project maintenance was organized into separate Git commits:

Initial V1 baseline
        ↓
Corrective maintenance: fix division by zero
        ↓
Adaptive maintenance: add Flask web interface
        ↓
Preventive maintenance: improve validation and code quality
        ↓
Perfective maintenance: add percentage and factorial
        ↓
Complete software maintenance documentation
10. Comparison of Maintenance Categories
Maintenance Category	Purpose	Project Change
Corrective	Fix existing defects	Fixed division by zero
Adaptive	Adapt to a new environment	Added Flask web interface
Preventive	Prevent future problems	Improved validation, type hints, error handling, and testing
Perfective	Improve functionality	Added factorial and percentage
11. Conclusion

The Math Problem Solver was successfully used to simulate the four major
categories of software maintenance.

Corrective maintenance fixed an existing division-by-zero defect.
Adaptive maintenance adapted the application from a command-line
environment to a web-based environment. Preventive maintenance improved
validation, error handling, type hints, and testing. Finally, perfective
maintenance enhanced the application by adding factorial and percentage
calculations.

The final system successfully passed:

16 tests
OK

Therefore, the project demonstrates a complete software maintenance
lifecycle covering corrective, adaptive, preventive, and perfective
maintenance activities.


### Important

After replacing your current README with the above, **do not keep the old text below it**. Your current README has duplicate headings and this incorrect statement:

> "Preventive and Perfective maintenance activities are still to be performed."

That statement must be removed because you have already completed both.

Then run:

```powershell
git add README.md
git commit -m "Complete software maintenance documentation"
git push

10. Transformation and Software Analysis Tools

As part of the software maintenance activities, four transformation and software analysis tools were applied to the Math Problem Solver project:

Loguru
PySnooper
VizTracer
SnakeViz

These tools were used to understand program behavior, execution flow, debugging information, logging, and performance characteristics.

10.1 Loguru
Purpose

Loguru is a Python logging library used to record important events during program execution.

Usage in the Project

Loguru was integrated into the Math Problem Solver to record mathematical operations performed by the application.

For example, when the user performs an addition operation, the application produces a log message such as:

[LOG] Addition operation performed
Addition result: 7.0

The log provides information about which operation was performed and helps developers monitor application behavior.

Output Insight

The Loguru output confirms that:

The application received the requested operation.
The corresponding calculator function was executed.
A log message was generated.
The calculation completed successfully.

Figure 1: Loguru execution output

[Insert your Loguru screenshot here]

Maintenance Use

Loguru is useful during corrective maintenance because developers can inspect application logs when users report unexpected behavior. For example, if a calculation fails, the log can help identify which operation was executed before the failure.

10.2 PySnooper
Purpose

PySnooper is a debugging and execution-tracing tool that shows what happens inside Python functions while they are running.

Usage in the Project

PySnooper was applied to the mathematical functions of the Math Problem Solver. It was used to observe function execution, variable values, and returned results.

For example, when an arithmetic function executes, PySnooper can show:

Function call
Input values
Variable changes
Executed statements
Return value
Output Insight

The PySnooper output provides a detailed view of the internal execution flow. It helps developers understand how input values move through the calculation function and how the final result is produced.

Figure 2: PySnooper execution trace

[Insert your PySnooper screenshot here]

Maintenance Use

PySnooper can be used during corrective maintenance when a function produces an unexpected result. Developers can trace the function execution and identify where the incorrect behavior occurs.

For example, it can help investigate problems in:

divide()
square_root()
cube_root()
factorial()
percentage()
10.3 VizTracer
Purpose

VizTracer is an execution-tracing and performance-analysis tool for Python applications.

Usage in the Project

VizTracer was used to trace the execution of the Math Problem Solver application.

The application was executed through VizTracer, and the resulting trace was opened using the VizTracer viewer.

The trace provides information about:

Function calls
Execution sequence
Function duration
Program execution flow
Performance behavior
Output Insight

The VizTracer visualization provides a timeline of program execution. It allows developers to see which functions were called and how long different parts of the program took to execute.

Figure 3: VizTracer execution timeline

[Insert your VizTracer screenshot here]

Maintenance Use

VizTracer is useful for performance-related maintenance.

For example, if a new feature causes the Math Problem Solver to become slower, VizTracer can help developers identify the functions responsible for the increased execution time.

It can therefore support maintenance activities such as:

Performance optimization
Identifying slow functions
Understanding complex execution flows
Comparing execution behavior before and after modifications
10.4 SnakeViz
Purpose

SnakeViz is a graphical visualization tool for Python profiling data generated using cProfile.

Usage in the Project

The Math Problem Solver was profiled using Python's cProfile, and the resulting profiling data was visualized using SnakeViz.

The profiling process generated information about function calls and execution time.

SnakeViz was then used to display this information graphically.

Output Insight

The SnakeViz visualization helps identify:

Frequently executed functions
Function execution time
Number of function calls
Functions that consume more processing time
Potential performance bottlenecks

Figure 4: SnakeViz profiling visualization

[Insert your SnakeViz screenshot here]

Maintenance Use

SnakeViz can be used during performance-oriented maintenance.

For example, after adding new functionality such as factorial and percentage calculations, developers can profile the application to determine whether any function introduces unnecessary execution overhead.

The project already records these perfective changes and the final 16-test result.

11. Comparison of Transformation Tools
Tool	Main Purpose	Main Output	Maintenance Use
Loguru	Logging	Log messages	Error monitoring and debugging
PySnooper	Execution tracing	Line-by-line trace	Debugging functions
VizTracer	Execution/performance tracing	Timeline visualization	Performance analysis
SnakeViz	Profiling visualization	Graphical profile	Finding performance bottlenecks
12. Alternative Tools

There are several alternatives to the tools used in this project.

Used Tool	Alternative Tools
Loguru	Python logging, Structlog
PySnooper	pdb, debugpy
VizTracer	Pyinstrument, cProfile
SnakeViz	Py-Spy, Tuna
Preferred Tools

For a real software project, Loguru would be preferred for application logging because it provides simple and readable logging.

For performance analysis, VizTracer would be preferred because its timeline visualization makes it easier to understand function execution and identify performance problems.

13. Overall Insight from the Tools

The four tools provide different perspectives of the same Math Problem Solver application.

                 Math Problem Solver
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     Loguru          PySnooper        Profiling
        │                │                │
      Logs          Line-by-line     Performance
                       Trace          Analysis
                                         │
                                  ┌──────┴──────┐
                                  │             │
                              VizTracer     SnakeViz
                              Timeline      Profile

Loguru shows what happened, PySnooper shows how the code executed, VizTracer shows how execution progressed over time, and SnakeViz shows where the program spent its processing time.

Together, these tools provide useful information for software maintenance and help developers understand, debug, optimize, and maintain the application.

14. Conclusion

The Math Problem Solver project was used to demonstrate both software maintenance activities and transformation/analysis tools.

The project successfully went through Corrective, Adaptive, Preventive, and Perfective Maintenance, progressing from V1 to V2.0. The final system supports operations including addition, subtraction, multiplication, division, power, square root, cube root, factorial, and percentage, with 16 tests successfully passing.

In addition, Loguru, PySnooper, VizTracer, and SnakeViz were successfully simulated on the project. These tools provided logging, debugging traces, execution visualization, and profiling information.

Therefore, the project demonstrates how transformation and analysis tools can support real-world software maintenance by improving debugging, program comprehension, performance analysis, and maintainability.


## Initial Project Structure

```text
Math-Problem-Solver/
├── app.py
├── main.py
├── calculator/
│   ├── basic.py
│   ├── advanced.py
│   └── validator.py
├── utils/
│   ├── logger.py
│   └── formatter.py
├── tests/
│   ├── test_basic.py
│   ├── test_advanced.py
│   ├── test_validator.py
│   └── test_integration.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md


Baseline Testing

The initial version successfully passed:

Ran 10 tests
OK
3. Corrective Maintenance
Scenario

A defect was identified in the division operation. When the denominator
was zero, the application produced a ZeroDivisionError.

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

The divide() function was modified to validate the denominator before
performing the calculation.

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

The original application was command-line based. The system needed to be
adapted so that users could access it through a web browser.

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

The calculation modules were already separated from the main application
logic and could therefore be reused.

4.2 Change Management
Requirement

Adapt the existing command-line application to a web-based environment.

Change Implemented

A Flask web interface was introduced while reusing the existing calculator
modules.

Technology Added
Flask
HTML
Web interface
4.3 Impact Analysis

Affected components:

app.py               → Web application
requirements.txt     → Flask dependency
templates/index.html → Web interface

Reused components:

calculator/basic.py
calculator/advanced.py
calculator/validator.py
4.4 Reverse Engineering

The existing flow was analyzed:

CLI
 ↓
main.py
 ↓
Validation
 ↓
Calculator Function
 ↓
Result

The adapted flow became:

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

A Flask web interface was added without rewriting the existing calculator
logic.

The existing calculator functions are reused by app.py.

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

The application was working correctly, but improvements were required to
prevent future defects and make the system easier to maintain.

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

Potential invalid inputs were identified before they could cause
unexpected behavior.

5.5 Refactoring

The validation function was improved with type hints and better
exception handling:

def validate_number(value: str) -> float:
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(
            "Invalid number. Please enter a valid number."
        )

The advanced calculator was also improved to handle invalid square-root
and factorial inputs.

Additional validation tests were added.

Result

The software became easier to understand, maintain, and extend while
preserving its existing behavior.

Version
V1.2
 ↓
Preventive Maintenance
 ↓
V1.3
6. Perfective Maintenance
Scenario

Users requested additional mathematical functionality and an improved
web experience.

Change ID

CM-004

6.1 Program Comprehension

The existing advanced calculator and web application were analyzed to
determine where the new features should be integrated.

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

The web interface was updated to allow users to select the new
operations.

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
Ran 16 tests
OK
9. Git Maintenance History

The project maintenance was organized into separate Git commits:

Initial V1 baseline
        ↓
Corrective maintenance: fix division by zero
        ↓
Adaptive maintenance: add Flask web interface
        ↓
Preventive maintenance: improve validation and code quality
        ↓
Perfective maintenance: add percentage and factorial
        ↓
Complete software maintenance documentation
10. Comparison of Maintenance Categories
Maintenance Category	Purpose	Project Change
Corrective	Fix existing defects	Fixed division by zero
Adaptive	Adapt to a new environment	Added Flask web interface
Preventive	Prevent future problems	Improved validation, type hints, error handling, and testing
Perfective	Improve functionality	Added factorial and percentage
11. Conclusion

The Math Problem Solver was successfully used to simulate the four major
categories of software maintenance.

Corrective maintenance fixed an existing division-by-zero defect.
Adaptive maintenance adapted the application from a command-line
environment to a web-based environment. Preventive maintenance improved
validation, error handling, type hints, and testing. Finally, perfective
maintenance enhanced the application by adding factorial and percentage
calculations.

The final system successfully passed:

16 tests
OK

Therefore, the project demonstrates a complete software maintenance
lifecycle covering corrective, adaptive, preventive, and perfective
maintenance activities.


### Important

After replacing your current README with the above, **do not keep the old text below it**. Your current README has duplicate headings and this incorrect statement:

> "Preventive and Perfective maintenance activities are still to be performed."

That statement must be removed because you have already completed both.

Then run:

```powershell
git add README.md
git commit -m "Complete software maintenance documentation"
git push

10. Transformation and Software Analysis Tools

As part of the software maintenance activities, four transformation and software analysis tools were applied to the Math Problem Solver project:

Loguru
PySnooper
VizTracer
SnakeViz

These tools were used to understand program behavior, execution flow, debugging information, logging, and performance characteristics.

10.1 Loguru
Purpose

Loguru is a Python logging library used to record important events during program execution.

Usage in the Project

Loguru was integrated into the Math Problem Solver to record mathematical operations performed by the application.

For example, when the user performs an addition operation, the application produces a log message such as:

[LOG] Addition operation performed
Addition result: 7.0

The log provides information about which operation was performed and helps developers monitor application behavior.

Output Insight

The Loguru output confirms that:

The application received the requested operation.
The corresponding calculator function was executed.
A log message was generated.
The calculation completed successfully.

Figure 1: Loguru execution output

[Insert your Loguru screenshot here]

Maintenance Use

Loguru is useful during corrective maintenance because developers can inspect application logs when users report unexpected behavior. For example, if a calculation fails, the log can help identify which operation was executed before the failure.

10.2 PySnooper
Purpose

PySnooper is a debugging and execution-tracing tool that shows what happens inside Python functions while they are running.

Usage in the Project

PySnooper was applied to the mathematical functions of the Math Problem Solver. It was used to observe function execution, variable values, and returned results.

For example, when an arithmetic function executes, PySnooper can show:

Function call
Input values
Variable changes
Executed statements
Return value
Output Insight

The PySnooper output provides a detailed view of the internal execution flow. It helps developers understand how input values move through the calculation function and how the final result is produced.

Figure 2: PySnooper execution trace

[Insert your PySnooper screenshot here]

Maintenance Use

PySnooper can be used during corrective maintenance when a function produces an unexpected result. Developers can trace the function execution and identify where the incorrect behavior occurs.

For example, it can help investigate problems in:

divide()
square_root()
cube_root()
factorial()
percentage()
10.3 VizTracer
Purpose

VizTracer is an execution-tracing and performance-analysis tool for Python applications.

Usage in the Project

VizTracer was used to trace the execution of the Math Problem Solver application.

The application was executed through VizTracer, and the resulting trace was opened using the VizTracer viewer.

The trace provides information about:

Function calls
Execution sequence
Function duration
Program execution flow
Performance behavior
Output Insight

The VizTracer visualization provides a timeline of program execution. It allows developers to see which functions were called and how long different parts of the program took to execute.

Figure 3: VizTracer execution timeline

[Insert your VizTracer screenshot here]

Maintenance Use

VizTracer is useful for performance-related maintenance.

For example, if a new feature causes the Math Problem Solver to become slower, VizTracer can help developers identify the functions responsible for the increased execution time.

It can therefore support maintenance activities such as:

Performance optimization
Identifying slow functions
Understanding complex execution flows
Comparing execution behavior before and after modifications
10.4 SnakeViz
Purpose

SnakeViz is a graphical visualization tool for Python profiling data generated using cProfile.

Usage in the Project

The Math Problem Solver was profiled using Python's cProfile, and the resulting profiling data was visualized using SnakeViz.

The profiling process generated information about function calls and execution time.

SnakeViz was then used to display this information graphically.

Output Insight

The SnakeViz visualization helps identify:

Frequently executed functions
Function execution time
Number of function calls
Functions that consume more processing time
Potential performance bottlenecks

Figure 4: SnakeViz profiling visualization

[Insert your SnakeViz screenshot here]

Maintenance Use

SnakeViz can be used during performance-oriented maintenance.

For example, after adding new functionality such as factorial and percentage calculations, developers can profile the application to determine whether any function introduces unnecessary execution overhead.

The project already records these perfective changes and the final 16-test result.

11. Comparison of Transformation Tools
Tool	Main Purpose	Main Output	Maintenance Use
Loguru	Logging	Log messages	Error monitoring and debugging
PySnooper	Execution tracing	Line-by-line trace	Debugging functions
VizTracer	Execution/performance tracing	Timeline visualization	Performance analysis
SnakeViz	Profiling visualization	Graphical profile	Finding performance bottlenecks
12. Alternative Tools

There are several alternatives to the tools used in this project.

Used Tool	Alternative Tools
Loguru	Python logging, Structlog
PySnooper	pdb, debugpy
VizTracer	Pyinstrument, cProfile
SnakeViz	Py-Spy, Tuna
Preferred Tools

For a real software project, Loguru would be preferred for application logging because it provides simple and readable logging.

For performance analysis, VizTracer would be preferred because its timeline visualization makes it easier to understand function execution and identify performance problems.

13. Overall Insight from the Tools

The four tools provide different perspectives of the same Math Problem Solver application.

                 Math Problem Solver
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     Loguru          PySnooper        Profiling
        │                │                │
      Logs          Line-by-line     Performance
                       Trace          Analysis
                                         │
                                  ┌──────┴──────┐
                                  │             │
                              VizTracer     SnakeViz
                              Timeline      Profile

Loguru shows what happened, PySnooper shows how the code executed, VizTracer shows how execution progressed over time, and SnakeViz shows where the program spent its processing time.

Together, these tools provide useful information for software maintenance and help developers understand, debug, optimize, and maintain the application.

14. Conclusion

The Math Problem Solver project was used to demonstrate both software maintenance activities and transformation/analysis tools.

The project successfully went through Corrective, Adaptive, Preventive, and Perfective Maintenance, progressing from V1 to V2.0. The final system supports operations including addition, subtraction, multiplication, division, power, square root, cube root, factorial, and percentage, with 16 tests successfully passing.

In addition, Loguru, PySnooper, VizTracer, and SnakeViz were successfully simulated on the project. These tools provided logging, debugging traces, execution visualization, and profiling information.

Therefore, the project demonstrates how transformation and analysis tools can support real-world software maintenance by improving debugging, program comprehension, performance analysis, and maintainability.

