# s02p01-github-actions-basics-poc

A simple Python calculator module used to demonstrate GitHub Actions basics.

## Setup

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Running tests

```sh
.venv/bin/python -m pytest -v
```

## Linting

```sh
.venv/bin/ruff check src/ tests/
```
