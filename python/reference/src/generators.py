def fibonacci_generator(n: int, /):
    """Generate a given number elements from the Fibonacci sequence."""
    if n < 0:
        raise ValueError("Number of elements should be non-negative.")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def accumulator():
    """Accumulate values via the send() method."""
    total = 0
    while True:
        value = yield
        print(f"Received {value}", end=" ")
        if value is None:
            break
        total += value
        print(f"Total is {total}")