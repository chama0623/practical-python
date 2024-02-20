def safe_division(
    number: float, divisor: float, ignore_overflow: bool, ignore_zero_division: bool
):
    """発散, 0除算のときを考慮した割り算を行う

    Args:
        number (float): 被除数
        divisor (float): 除数
        ignore_overflow (bool): overflow時の挙動を指定する. trueのとき0を返す.
        ignore_zero_division (bool): 0除算時の挙動を指定する. trueのときinfを返す.

    Returns:
        result: number / divisor
    """
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


def safe_division2(
    number: float,
    divisor: float,
    *,
    ignore_overflow: bool = False,
    ignore_zero_division: bool = False,
):
    """発散, 0除算のときを考慮した割り算を行う. 発散, 0除算のときの挙動はキーワード専用引数で指定する.

    Args:
        number (float): 被除数
        divisor (float): 除数
        ignore_overflow (bool): overflow時の挙動を指定する. trueのとき0を返す. Default to False.
        ignore_zero_division (bool): 0除算時の挙動を指定する. trueのときinfを返す. Default to False.

    Returns:
        result: number / divisor
    """
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


def safe_division3(
    number: float,
    divisor: float,
    /,
    *,
    ignore_overflow: bool = False,
    ignore_zero_division: bool = False,
):
    """発散, 0除算のときを考慮した割り算を行う.
    被除数, 除数は位置専用引数で指定する.
    発散, 0除算のときの挙動はキーワード専用引数で指定する.

    Args:
        number (float): 被除数
        divisor (float): 除数
        ignore_overflow (bool): overflow時の挙動を指定する. trueのとき0を返す. Default to False.
        ignore_zero_division (bool): 0除算時の挙動を指定する. trueのときinfを返す. Default to False.

    Returns:
        result: number / divisor
    """
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


def safe_division4(
    number: float,
    divisor: float,
    /,
    ndigits: int = 10,  # 位置, キーワード引数
    *,
    ignore_overflow: bool = False,
    ignore_zero_division: bool = False,
):
    """発散, 0除算のときを考慮した割り算を行う.
    被除数, 除数は位置専用引数で指定する.
    発散, 0除算のときの挙動はキーワード専用引数で指定する.
    四捨五入する桁を指定できる.

    Args:
        number (float): 被除数
        divisor (float): 除数
        ndigits (int): 四捨五入する桁.
        ignore_overflow (bool): overflow時の挙動を指定する. trueのとき0を返す. Default to False.
        ignore_zero_division (bool): 0除算時の挙動を指定する. trueのときinfを返す. Default to False.

    Returns:
        result: rount(number / divisor, ndigits)
    """
    try:
        fraction = number / divisor
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


if __name__ == "__main__":
    # 第三引数, 第四引数の順番が分かりにくい
    result = safe_division(1.0, 10**500, True, False)
    print(result)

    # キーワード専用引数による改善例
    # result = safe_division2(1.0, 10**500, True, False)
    # -> TypeError: safe_division2() takes 2 positional arguments but 4 were given
    result = safe_division2(
        1.0,
        10**500,
        ignore_overflow=True,
    )
    print(result)

    # number, divisorは仕様変更で名前が変わったときに, 呼び出し側でキーワード専用引数で指定した部分は変更が必要.
    # 位置専用引数による改善例
    # result = safe_division3(
    #    number=1.0,
    #    divisor=10**500,
    #    ignore_overflow=True,
    # )
    # -> TypeError: safe_division3() got some positional-only arguments passed as keyword arguments: 'number, divisor'
    result = safe_division3(
        1.0,
        10**500,
        ignore_overflow=True,
    )
    print(result)

    # 通常の位置, キーワード引数を追加する例
    result = safe_division4(22, 7, 5)
    print(result)
    result = safe_division4(22, 7, ndigits=2)
    print(result)
