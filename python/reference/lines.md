# Lines

### Definitions
A *token* is a small unit of source code, such as name, number, operator, newline or other element created by the lexical analyzer.

A *lexical analyzer* is a program that tokenizes Python source code.

A *parser* is a program that reads tokenized code.

A *physical line* is a sequence of characters terminated by the end-of-line character.

A *logical line* is a sequence of characters terminated by a `NEWLINE` token.

A *comment* is a subsequence of a physical line starting with the `#` character. The comment cannot start inside a string literal. Comments are ignored by the intepreter.

### Features
- UTF-8 is a default encoding.
- The encoding can be specified in the first or the second line of the source code file in the format: `coding[:=]\s*[-\w.]+`.
- Blank lines are ignored by the interpreter.
- `\` is used for explicit line joining.
- Expressions in parentheses, square brackets and curly braces can be split into several lines without `\`.
- Whitespace serves as a separator between tokens.

### Examples
```python
# coding: utf-8

color = 'green'
weight = 3

# Explicit line joining
if color == 'green' \
and weight > 1:
    print("Good choice!")

# Implicit line joining
arr = [
   1, 2, 3,
   4, 5, 6,
   7, 8, 9
]
```

### References
[1] [Python Language Reference: Line Structure](https://docs.python.org/3/reference/lexical_analysis.html#line-structure)

[2] [Python Glossary: Token](https://docs.python.org/3/glossary.html#term-token)