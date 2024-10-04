# mk-project

## 1. Run Local Tests

Helpful prompts for running local tests and linting.

### 2.1. pytest

Must create a "../reports" directory in project root.

```cmd
python -m pytest --html=reports/report.html --cov=. --cov-branch --cov-report=html:reports/htmlcov --cov-config=.coveragerc
```

### 2.2. flake8

```cmd
python -m flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```
