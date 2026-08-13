# Math Problem Solver — Software Maintenance Project

## Project Overview

Math Problem Solver is a Python-based mathematical calculation application. The project initially provides basic and advanced mathematical operations through a command-line interface and is later adapted and improved through different software maintenance activities.

## Initial System — V1 Baseline

The initial version contains:

* Basic arithmetic operations
* Advanced mathematical operations
* Input validation
* Result formatting
* Logging
* Unit tests
* Integration testing

### Initial Project Structure

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
```

### Baseline Testing

The initial version successfully passed:

```text
Ran 10 tests
OK
```

---

# Maintenance History

## V1 — Initial Baseline

The original Math Problem Solver was developed as a command-line application.

```text
Initial V1 baseline
```

---

## V1.1 — Corrective Maintenance

### Problem

The division operation caused a `ZeroDivisionError` when the denominator was zero.

### Change

The `divide()` function was modified to detect division by zero and raise a meaningful error.

A regression test was also added.

### Result

Testing after the corrective maintenance:

```text
Ran 11 tests
OK
```

```text
Corrective: Fix division by zero
```

---

## V1.2 — Adaptive Maintenance

### Requirement

The original application was command-line based. The system needed to be adapted for browser-based use.

### Change

A Flask web interface was introduced while reusing the existing calculator modules.

The application now supports:

```text
Browser
   ↓
Flask app.py
   ↓
Calculator Modules
   ↓
Result
```

### Technology Added

* Flask
* HTML web interface

### Result

The Math Problem Solver can now be accessed through a web browser.

```text
Adaptive: Add Flask web interface
```

---

# Maintenance Progress

```text
Initial V1 baseline
       ↓
Corrective: Fix division by zero
       ↓
Adaptive: Add Flask web interface
       ↓
Preventive: Improve maintainability
       ↓
Perfective: Add/improve user features
```

> **Note:** Preventive and Perfective maintenance activities are still to be performed.
