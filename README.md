# All Tools

A repo where I plug _all_ Python code analyzers, checkers, linters, and so on that I find it interesting.

## Tools

### Formatter

* **Black** ― Executed on pre-commit

### Linter

* **Pylint** ― Executed on pre-commit

### Tester

* **pytest** ― Executed on pre-push
* **pytest-cov** ― Executed on pre-push with Pytest
* **hypothesis** ― Finally got around trying this! Really neat.

### Static Analyzers

* **Vulture** ― Detects dead code. Runs on CI
* [**wily**](https://wily.readthedocs.io/) ― Tracks application complexity. Currently broken on CI

### REST API Checkers

* **Schemathesis** ― hypothesis over OpenAPI Specs

### Misc

* **pre-commit** ― Manages git hooks
* **ipython** ― Python REPL, but better

### To Be Add

* Pyre
* Mypy
* Pysa
* Flake8
* Pytest Mock
* Logassert
* Rich (?)
