# hello-there-cli

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
