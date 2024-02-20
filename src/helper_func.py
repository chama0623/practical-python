from urllib.parse import parse_qs


def get_first_int(values: dict[str, any], key: str, default: int = 0) -> int:
    """valuesからkeyに対応する値を取得し, その値を整数にして返す. 指定されたkeyが存在しない場合にはdefaultを返す

    Args:
        values (dict[str, any]): 検索する辞書
        key (str): 検索する値
        default (int, optional): デフォルト値. Defaults to 0.

    Returns:
        int: 整数値
    """
    found = values.get(key, [""])  # keyに対応する値を取得する. 無いときは[""]を返す
    if found[0]:
        return int(found[0])
    else:
        return default


if __name__ == "__main__":
    # クエリ文字列の復号をしたい
    query_str = "red=5&blue=0&green="
    my_values = parse_qs(
        query_str, keep_blank_values=True
    )  # クエリ値がないときは空白文字とみなす
    print(repr(my_values))

    # helper関数を使って値をクエリ値を取得する
    # 空文字列のとき0を代入する
    red = get_first_int(my_values, "red")
    blue = get_first_int(my_values, "blue")
    green = get_first_int(my_values, "green")
    print(f"{red=}, {blue=}, {green=}")
