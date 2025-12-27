# Python Calculator

A lightweight Python calculation script that performs fast, accurate computations with clean logic and minimal overhead. Designed for simplicity, reliability, and easy reuse in larger projects.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division
- **Advanced Operations**: Power, modulo, square root
- **Error Handling**: Proper handling of division by zero, negative square roots, and invalid inputs
- **Clean API**: Simple Calculator class for easy integration into larger projects
- **CLI Interface**: Interactive command-line interface for standalone usage
- **Fully Tested**: Comprehensive unit tests ensuring reliability

## Usage

### As a Module

```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(10, 5)        # 15
result = calc.subtract(10, 5)   # 5
result = calc.multiply(10, 5)   # 50
result = calc.divide(10, 5)     # 2.0

# Advanced operations
result = calc.power(2, 3)       # 8
result = calc.modulo(10, 3)     # 1
result = calc.square_root(16)   # 4.0
```

### As a CLI Application

Run the calculator interactively:

```bash
python calculator.py
```

Follow the prompts to perform calculations:
1. Select an operation (1-8)
2. Enter the required numbers
3. View the result
4. Repeat or exit

## Running Tests

Run the unit tests to verify functionality:

```bash
python -m unittest test_calculator -v
```

## Requirements

- Python 3.6 or higher
- No external dependencies required
