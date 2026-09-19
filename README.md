# Smart Calculator

A command-line calculator built with Python.

## Overview

This project is a calculator that supports basic arithmetic, mathematical operations, memory functions, and calculation history.

The project uses a class to organise the calculator's operations and stores calculation history during the current session.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Exponentiation
- Square root
- Percentage calculation
- Memory add
- Memory recall
- Memory clear
- Calculation history
- Input validation
- Division-by-zero handling

## Operations

| Input | Operation |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `^` | Exponentiation |
| `sqrt` | Square root |
| `%` | Percentage |
| `M+` | Add a value to memory |
| `MR` | Recall memory |
| `MC` | Clear memory |
| `H` | Show calculation history |
| `Q` | Quit |

## How It Works

The program creates a `SmartCalc` object that stores:

- The current memory value
- The calculation history

Each mathematical operation is handled by a separate method. Successful calculations are added to the history.

The program continues running until the user chooses `Q`.

## Project Structure

smart-calculator/
├── calculator.py
└── README.md

## Technologies Used

- Python
- `math`

## How to Run

Open the project folder in a terminal and run:

    python calculator.py

## Error Handling

The calculator handles common input errors, including:

- Invalid numerical input
- Division by zero
- Square root of a negative number
- Invalid operations

## Concepts Practised

- Classes and objects
- Methods
- Functions
- Conditional statements
- `while` loops
- User input
- Exception handling
- Lists
- String formatting
- Mathematical operations
- Using Python modules

## Possible Improvements

- Add trigonometric functions
- Add logarithms
- Add calculation history saved to a file
- Add more memory operations
- Add a graphical interface
- Allow complete expressions such as `2 + 3 * 4`

These features are not currently implemented.

## Author

Abiral Upreti

A Python project focused on practising object-oriented programming, mathematical operations, and user input handling.
