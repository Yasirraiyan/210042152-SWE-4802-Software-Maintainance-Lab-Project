Change ID: CM-001
Type: Corrective Maintenance

Problem:
The application crashes when the user attempts to divide by zero.

Requested Change:
Add validation to the divide() function to prevent division by zero.

Priority:
High

Affected Component:
calculator/basic.py

calculator/basic.py  → Direct impact
main.py              → Indirect impact
tests/test_basic.py  → New regression test required
User
 ↓
main.py
 ↓
User selects Division
 ↓
divide(a, b)
 ↓
a / b
 ↓
b = 0
 ↓
Application crashes

Adaptive Maintenance

Change ID: CM-002

Problem/Requirement:
The current Math Problem Solver is a command-line application.
Users want to access the system through a web browser.

Requested Change:
Adapt the existing application to a web-based environment using Flask.

Reason:
The software needs to support browser-based interaction.

Affected Components:
- app.py
- requirements.txt
- New templates/index.html

Reusable Components:
- calculator/basic.py
- calculator/advanced.py
- calculator/validator.py
- utils/formatter.py
