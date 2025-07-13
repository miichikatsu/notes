# Identifiers

## Definitions
An *identifier (name)* is a sequence of characters in source code that refers to a function, variable, class, or other named entity. The identifier consists of `[a...zA...Z0...9_]` characters or Unicode characters categorized as letters. The identifier cannot start with a digit.

Certain classes of identifiers have special meanings in Python:
- `_*` - Not imported by `from module import *`.
- `_` - A soft keyword that denotes a wildcard in `match case` statements. It also stores the value of the last evaluation in interactive interpreter mode.
- `__*__` - System-defined (dunder) names. Dunder names are defined by the interpreter. User-defined dunder names can lead to breakage.
- `__*` - Class-private names. The interpreter mangles these names to avoid clashes between base and derived classes.

## Examples
[Identifiers](src/identifiers.py)

## References
[1] [Python Language Reference: Identifiers](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)

[2] [Python Language Reference: Reserved Classes of Identifiers](https://docs.python.org/3/reference/lexical_analysis.html#reserved-classes-of-identifiers)