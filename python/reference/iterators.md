# Iterators

## Definitions
An *iterator* is an object that implements two specific methods, which form the *iterator protocol*:

1. `__iter__()`
- Takes no arguments.
- Returns the object itself.

2. `__next__()`
- Takes no arguments.
- Returns the next item. When no items remain, raises the `StopIteration` exception.

An *iterable* is an object that implements the `__iter__()` method which takes no arguments and returns an iterator.

A *state* is internal information used for that maintains the current iteration progress. It consists of local variable values and the current execution point.

## Features
- Stateful: Allows maintaining state between `__next__()` calls.
- Memory-efficient: Enables sequential data processing without requiring full storage.
- `iter(iterable)` invokes `iterable.__iter__()`.
- `next(iterator)` invokes `iterator.__next__()`.

## Implementations
[Iterator](src/iterator.py)

## Examples
```python
>>> from src.iterator import SimpleIterator
>>> sit = SimpleIterator([1, 2, 3])
>>> sit == iter(sit)
True
>>> sit == sit.__iter__()
True
>>> next(sit)
3
>>> sit.__next__()
2
>>> next(sit)
1
>>> next(sit)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "src.iterator.py", line 13, in __next__
    raise StopIteration
StopIteration
```

## References
[1] [Python Glossary: Iterator](https://docs.python.org/3/glossary.html#term-iterator)

[2] [Python Docs: Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)

[3] [Python Docs: Iterator Type](https://docs.python.org/3/library/stdtypes.html#iterator-types)