def memoize(func):
    cache = {}

    def memoized_function(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_function


@memoize
def factorial(n: int) -> int:
    if n < 2:
        return 1
    return n * factorial(n - 1)


@memoize
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Factorial of 5:", factorial(5))
print("Factorial of 6:", factorial(6))
print("Fibonacci of 10:", fibonacci(10))
print("Fibonacci of 11:", fibonacci(11))
