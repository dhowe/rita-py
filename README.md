# rita-py

Python port of RiTa

## Features

- **RiScript Interpreter**: Parser with support for choices, gates, statics, dynamics, and transforms
- **RiTa Compatibility**: Full RiTa functionality including text analysis utilities

## Examples

Run the included example to see RiScript in action:

```bash
PYTHONPATH=. python3 examples/simple_example.py
```

See [examples/simple_example.py](examples/simple_example.py) for code demonstrating:
- Choice selection
- Word transformations
- Dynamic and static assignments
- Gate logic
- Context variables
- Multi-pass evaluation

## Installation

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/dhowe/rita-py.git
cd rita-py
python3 -m venv .venv
source .venv/bin/activate
```

## Quick Start

```python
from riscript import RiScript

rs = RiScript()

# Basic evaluation
result = rs.evaluate('The [ox | ox ].pluralize run', {})
print(result)  # Output: "The oxen run"

# Using dynamic values
result = rs.evaluate('$name.cap() went to the store.', {'name': 'john'})
print(result)  # Output: "John went to the store."

# Gate logic
result = rs.evaluate('[ @{$age:18} adult || child ]', {'age': 20})
print(result)  # Output: "adult"

# Multi-pass evaluation
result = rs.evaluate('$name=John\n$name.cap() went home.', {})
print(result)  # Output: "John went home."
```

## Running Tests

Activate a virtual environment (`source .venv/bin/activate`), then:

### Run tests

```bash
pytest
```

### Run specific test files

```bash
pytest test_riscript.py
pytest test_grammar.py
pytest test_rita.py
pytest test_util.py
pytest test_randgen.py
```

### Run specific test classes

```bash
pytest test_riscript.py::TestGates
pytest test_riscript.py::TestChoices
pytest test_riscript.py::TestTransforms
```

### Run specific test methods

```bash
pytest test_riscript.py::TestGates::test_else_gates
pytest test_riscript.py::TestChoices::test_multiword_choice
```

### Run with verbose output

```bash
pytest -v
```

## Core Concepts

### RiScript Statements

- **Dynamic statements** (`$foo=bar`) - Runtime assignments
- **Static statements** (`#foo=[a|b]`) - Compile-time replacements
- **Silent blocks** (`*content*`) - Ignored during output

### Choices

```
[option1 | option2 | option3]
```

Randomly selects one option (weighted by repetition).

### Gates

```
[ @{$value: {@gt: 10} } condition || alternative ]
```

Conditional logic using Mingo-style queries.

### Transforms

```
$word.lower() | $word.upper() | $word.pluralize()
```

Built-in transforms: articlize, lower, uc, pluralize, cap, etc.

## Test Coverage

- **Total Tests**: 300
- **Passing**: 300/300 (100%)
- **Coverage Areas**:
  - Gate evaluation (boolean, equality, comparison, existence)
  - Choice selection (weighted, multi-word, transforms)
  - Transform system (custom, static, context-based)
  - Statement handling (dynamic, static, silent)
  - Query class (operand extraction, testing)
  - Hash utilities (string hashing, parsing)
  - Unicode and emoji support
  - All JavaScript parity tests

## Project Structure

```
rita-py/
├── riscript.py      # Core RiScript interpreter
├── randgen.py       # Seeded random number generator
├── util.py          # Utility functions
├── examples/
│   ├── simple_example.py  # Demo program
│   └── README.md          # Examples documentation
├── test_*.py        # Test suites
├── README.md        # This file
```

## License

GNU General Public License v3.0 (GPL-3.0)
