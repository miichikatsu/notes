# Iterator

### Definition
An <u>iterator</u> is an object implementing two specific methods:

1. `__iter__()`
- Takes no arguments.
- Returns the object itself.

2. `__next__()`
- Takes no argumens.
- Returns the next item and raises `StopIteration` when no items remain.

An <u>iterable</u> is an object implementing `__iter__()` method which takes no arguments and returns iterator.

### Key Features
- Stateful: Maintains state between `__next__()` calls.
- Memory efficient: Processes data without storing it in memory.
- `iter(iterable)` invokes `iterable.__iter__()`.
- `next(iterator)` invokes `iterator.__next__()`.

### Implementation
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

### Reference

[1] [docs.python.org/3/tutorial/classes.html#iterators](https://docs.python.org/3/tutorial/classes.html#iterators)