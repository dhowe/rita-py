# rita-py

Python port of RiTa

## Features

- **RiScript Interpreter**: Parser with support for choices, gates, statics, dynamics, and transforms

## Examples

Run the included example to see RiScript in action:

```bash
PYTHONPATH=. python3 examples/riscript_examples.py
```

See [examples/riscript_examples.py](examples/riscript_examples.py) for code demonstrating:
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
result = rs.evaluate('The [ox | ox ].pluralize run')
print(result)  # Output: "The oxen run"

# Using dynamic values
result = rs.evaluate('$name.cap() went to the store.', {'name': 'john'})
print(result)  # Output: "John went to the store."

# Gate logic
result = rs.evaluate('[ @{$age: {@gte: 18}} adult || child ]', {'age': 20})
print(result)  # Output: "adult"

# Multi-pass evaluation
result = rs.evaluate('$name=John\n$name.cap() went home.')
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
## Core Concepts

### RiScript Statements

- **Dynamic statements** (`$foo=bar`) - Runtime assignments
- **Static statements** (`#foo=[a|b]`) - Compile-time replacements
- **Silent blocks** (`{$foo=bar}`) - Silent evaluation

### Choices

```
[option1 | option2 | option3]
```

Randomly selects one option (weights optional).

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

- **Areas**:
  - Gate evaluation (boolean, equality, comparison, existence, regex, deferred)
  - Choice selection (weighted, multi-word, transforms, spacing variants)
  - Transform system (custom, static, context-based, no-parens, old-style `$.fn`)
  - Statement handling (dynamic, static, silent `{$foo=...}`, line-break form)
  - Assignment types (inline `[$foo=...]`, line `$foo=...`, silent `{$foo=...}`, static `#foo=...`)
  - Object method/property access from context (`$obj.prop`, `$obj.method()`, `$obj.method` no-parens)
  - Comment stripping (`//` line comments, `/* */` block comments, `\r\n` line endings)
  - Continuation lines (`~\n` tilde and `\<newline>` backslash)
  - HTML entities (`&num;`, `&#x00023;`, `&nbsp;`, `&lpar;`, etc.)
  - Unicode, emoji, and Chinese character support
  - Query class (operand extraction, testing)
  - Hash utilities (string hashing, JSOL parsing)
  - Full JavaScript (riscript.tests.js + grammar.tests.js) parity

## Project Structure

```
rita-py/
├── riscript.py      # Core RiScript interpreter
├── randgen.py       # Seeded random number generator
├── util.py          # Utility functions
├── examples/
│   ├── riscript_examples.py  # Demo program
│   └── README.md              # Examples documentation
├── test_*.py        # Test suites
├── README.md        # This file
```

## License

GNU General Public License v3.0 (GPL-3.0)
