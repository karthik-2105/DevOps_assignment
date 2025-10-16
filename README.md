# Simple Calculator App (Python)

[![CI Pipeline for Calculator App](https://github.com/karthik-2105/Calculator_app_DG/actions/workflows/main.yml/badge.svg)](https://github.com/karthik-2105/Calculator_app_DG/actions/workflows/main.yml)

## CI Pipeline (GitHub Actions)

This repository uses a GitHub Actions pipeline to:
- Run automatically when code is pushed to the main branch
- Install dependencies and run unit tests using pytest
- Display build status via the badge above


Files:
- app/calculator.py : calculator functions (add, subtract, multiply)
- tests/test_calculator.py : pytest unit tests
- requirements.txt : Python test dependency

How to run locally:
1. python3 -m venv venv
2. source venv/bin/activate   (on Windows: venv\Scripts\activate)
3. pip install -r requirements.txt
4. pytest -q

Project created for DevOps CI/CD assignment.
