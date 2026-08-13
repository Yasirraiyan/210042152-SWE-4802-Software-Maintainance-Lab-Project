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


