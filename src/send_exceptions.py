def careful_divide(a: int, b: int) -> float | None:
    """a/bを求める悪い例. 0もNoneと判定されるため, 例外処理ではNoneを返さない方が良い

    Args:
        a (int): 被除数
        b (int): 除数

    Returns:
        float|None: a/b, b=0のときNone
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def careful_divide_except(a: int, b: int) -> float:
    """a/bを求める良い例. b=0のときは例外を送出する

    Args:
        a (int): 被除数
        b (int): 除数

    Raises:
        ValueError: b=0のとき

    Returns:
        float: 割り算の結果
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Invalid inputs")


if __name__ == "__main__":
    x, y = 1, 0
    result = careful_divide(x, y)
    if result is None:
        print("Invalid inputs")

    # x/yが0のときもNoneと判定される
    x, y = 0, 5
    result = careful_divide(x, y)
    if not result:
        print("Invalid inputs")

    # 改善例
    x, y = 0, 1
    try:
        result = careful_divide_except(x, y)
    except ValueError:
        print("Invalid inputs")
    else:
        print(f"{result=}")
