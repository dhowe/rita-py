# rita-py
Python port of RiTa (in-progress)

## Installation

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/dhowe/rita-py.git
cd rita-py
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

## Run the tests

Activate your virtual environment (`source .venv/bin/activate`), then:

Run tests:

```bash
pytest
```

Run one test file:

```bash
pytest test_riscript.py
pytest test_grammar.py
```

Run a specific test class or method:

```bash
pytest test_riscript.py::TestGates
pytest test_riscript.py::TestGates::test_else_gates
```
