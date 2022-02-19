def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    result = 0
    for i in range(2, n + 1):
        result = a + b
        a, b = b, a + b

    return result


if __name__ == "__main__":
    print(fib_iterative(10))
    print(fib_recursive(10))