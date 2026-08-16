1)cd C:\Users\ASUS\Desktop\Math-Problem-Solver
2)python -m venv venv
3).\venv\Scripts\Activate.ps1
4)pip install flask sympy
5)pip install coverage radon snakeviz viztracer black yapf
6)python -m unittest discover -s tests -p "test_*.py"
    |
    |
   |................
  Output
----------------------------------------------------------------------
Ran 16 tests

OK

7)python main.py
8)python app.py
9)http://127.0.0.1:5000
10)C:\Users\ASUS\Desktop\Math-Problem-Solver
11.)cd C:\Users\ASUS\Desktop\Math-Problem-Solver
12.).\venv\Scripts\Activate.ps1
13.)pip install loguru pysnooper viztracer snakeviz
14.)python -m analysis.logging_demo
15.)dir analysis
16.)python -m analysis.pysnooper_demo
17.)viztracer main.py
18.)vizviewer result.json
19.)python -m cProfile -o profile.prof main.py
20.)snakeviz profile.prof
