# Iterator

### Definitions
An <u>*iterator*</u> is an object implementing two specific methods, which form the <u>*iterator protocol*</u>:

1. `__iter__()`
- Takes no arguments.
- Returns the object itself.

2. `__next__()`
- Takes no arguments.
- Returns the next item. When no items remain, raises the `StopIteration` exception.

An <u>*iterable*</u> is an object implementing method `__iter__()` which takes no arguments and returns an iterator.

A <u>*state*</u> is a private data attributes stored within an iterator.

### Features
- Stateful: Alows maintaining state between `__next__()` calls.
- Memory efficient: Allows for processing data sequentially avoiding full storage.
- `iter(iterable)` invokes `iterable.__iter__()`.
- `next(iterator)` invokes `iterator.__next__()`.

### Implementations
```python
class SimpleIterator():
    def __init__(self, data):
        self._data = data
        self._index = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index > 0:
            self._index -= 1
            return self._data[self._index]
        raise StopIteration
```

### Examples
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

### References
[1] [Python Glossary: Iterator](https://docs.python.org/3/glossary.html#term-iterator)

[2] [Python Docs: Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)

[3] [Python Docs: Iterator Type](https://docs.python.org/3/library/stdtypes.html#iterator-types)