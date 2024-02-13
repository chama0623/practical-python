def remainder(number: int, divisor: int) -> int:
    """number/divisorの商を計算する

    Args:
        number (int): 被除数
        divisor (int): 除数

    Returns:
        int: number % divisor
    """
    return number % divisor


def print_parameters(**kwargs):
    """パラメータを出力する"""
    for key, value in kwargs.items():
        print(f"{key} = {value}")


if __name__ == "__main__":
    # 位置引数 : 引数の値 だけを記述する
    # キーワード引数 : キーワード=値 を記述する
    # 位置引数, キーワード引数, 可変長引数
    print(remainder(20, 7) == 6)
    print(remainder(20, divisor=7) == 6)
    print(remainder(number=20, divisor=7) == 6)
    print(remainder(divisor=7, number=20) == 6)
    # キーワード引数の後で位置引数は指定できない
    # print(remainder(number=20, 7)) # -> SyntaxError: positional argument follows keyword argument
    # 各引数は1回しか指定できない
    # print(remainder(20, number=7) == 6) # -> TypeError: remainder() got multiple values for argument 'number'

    # dictで引数を指定する
    my_kwargs = {"number": 20, "divisor": 7}
    print(remainder(**my_kwargs) == 6)
    # 位置・キーワード引数とdictを混在させる
    my_kwargs = {"divisor": 7}
    print(remainder(20, **my_kwargs) == 6)

    # 関数で名前付き引数を受け取る
    print_parameters(alpha=1.5, beta=9, gamma=4)
