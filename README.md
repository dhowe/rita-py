# rita-py
Python port of RiTa

# Status
In-progress, currently supports on RiScript subset

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/dhowe/rita-py.git
cd rita-py
pip install pytest
```

No other dependencies are required for core functionality.

## Running the Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest test_riscript.py
pytest test_grammar.py
```

Run a specific test class or method:

```bash
pytest test_riscript.py::TestGates
pytest test_riscript.py::TestGates::test_else_gates
```

Run with verbose output:

```bash
pytest -v
```
