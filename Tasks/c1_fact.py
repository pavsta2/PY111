def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError("n должно быть больше 0")
    if n == 0:
        return 1
    return factorial_recursive(n - 1) * n


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError("n должно быть больше 0")
    if n == 0:
        return 1
    result = 1
    while n > 0:
        result *= n
        n = n - 1
    return result


if __name__ == "__main__":
    print(factorial_recursive(5))
    print(factorial_iterative(5))
