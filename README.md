# hello-there-cli

![Tests](https://github.com/jkitchin/hello-there-cli/actions/workflows/tests.yml/badge.svg)

A simple CLI that prints "hello there" with an optional named argument.

## Installation

```bash
pip install -e .
```

## Usage

```bash
hello-there
# hello there, World

hello-there --name Alice
# hello there, Alice
```

## Development

Run the tests:

```bash
pip install pytest
pytest tests/ -v
```
