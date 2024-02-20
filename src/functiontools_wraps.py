from functools import wraps


def trace(func):
    # 関数呼び出しの引数と戻り値を出力するラッパー
    def wrapper(*args, **kwargs):
        # *args: 可変長引数
        # **kwargs: キーワード引数
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args!r}, {kwargs!r})" f"-> {result!r}")
        return result

    return wrapper


def trace2(func):
    # functools.wrapsによる関数呼び出しの引数と戻り値を出力するラッパー
    @wraps(func)
    def wrapper(*args, **kwargs):
        # *args: 可変長引数
        # **kwargs: キーワード引数
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args!r}, {kwargs!r})" f"-> {result!r}")
        return result

    return wrapper


@trace
def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number

    Args:
        n (int): n-th

    Returns:
        int: n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


@trace2
def fibonacci2(n: int) -> int:
    """Return the n-th Fibonacci number

    Args:
        n (int): n-th

    Returns:
        int: n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    fibonacci(4)
    # デコレータから返される値はfibonacciではない
    print(fibonacci)  # -> <function trace.<locals>.wrapper at 0x7fbe3318dda0>
    """
    help(fibonacci) # fibonacciのhelpが表示されない
    > Help on function wrapper in module __main__:
    >
    > wrapper(*args, **kwargs)
    """

    # functools.wrapsによる改善例
    fibonacci2(4)
    print(fibonacci2)
