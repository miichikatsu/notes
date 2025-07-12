# Generator

### Definitions
A <u>*generator*</u> is an iterator created by a generator function or expression.

A <u>*generator function*</u> is a function that contains one or more `yield` statements and returns a generator.

A <u>*generator expression*</u> is an expression that returns an iterator. It is formed by a normal expression followed by a `for` clause and an optional `if` clause: `item for item in iterable if condition`.

### Features
- Implements the `__iter__()` and `__next__()` methods.
- Maintains state between yield calls.
- Generates values one at a time, avoiding a full sequence storage.
- Allows binding the current `yield` statement to a value via the `send(value)` method.
- Supports raising exceptions or closing the generator at its current state via the `throw(Exception)` and `close()` methods.

### Implementations
```python
def fibonacci_generator(n: int, /):
    """Generate a given number elements from the Fibonacci sequence."""
    if n < 0:
        raise ValueError("Number of elements should be non-negative.")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def accumulator():
    total = 0
    while True:
        value = yield
        print(f"Recieved {value}", end=" ")
        if value is None:
            break
        total += value
        print(f"Total is {total}")
```

### Examples
```python
>>> sum(x ** 2 for x in range(1, 10))
285
>>> from src.generator import fibonacci_generator, accumulator
>>> next(fibonacci_generator(-1))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "src/generator.py", line 4, in fibonacci_generator
    raise ValueError("Number of elements should be non-negative.")
ValueError: Number of elements should be non-negative.
>>> fib = fibonacci_generator(7)
>>> fib == iter(fib)
True
>>> next(fib)
0
>>> next(fib)
1
>>> for x in fib:
...     print(x)
... 
1
2
3
5
8
>>> acc = accumulator() 
>>> acc.send(None)
>>> acc.send(10)
Recieved 10 Total is 10
>>> acc.send(12)
Recieved 12 Total is 22
>>> acc.send(17)
Recieved 17 Total is 39
>>> acc.close()
>>> acc
<generator object accumulator at 0x1027bc9e0>
>>> next(acc)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### References
[1] [Python Glossary: Generator](https://docs.python.org/3/glossary.html#term-generator)

[2] [Python Docs: Yield Statement](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement)

[3] [Python Docs: Generator Expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)