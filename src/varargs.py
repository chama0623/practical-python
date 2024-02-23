def log(message: str, values: list[int]) -> None:
    """デバッグ情報のログを出力する

    Args:
        message (str): メッセージ
        values (list[int]): 数字の列
    """
    if not values:
        print(message)
    else:
        values_str = ",".join(str(x) for x in values)
        print(f"{message}: {values_str}")


def log2(message: str, *values: list[int]) -> None:
    """デバッグ情報のログを出力する. valuesは可変長引数.

    Args:
        message (str): メッセージ
    """
    if not values:
        print(message)
    else:
        values_str = ",".join(str(x) for x in values)
        print(f"{message}: {values_str}")


if __name__ == "__main__":
    # valuesがないときも空リストを渡さないといけない
    log("My numbers are", [1, 2])
    log("Hi there", [])

    # 可変長引数を用いた改善例
    # ただしこの方法では*valuesに渡す可変引数がタプルに変換されるため, 可変引数に比例してメモリ消費が増加する.
    # また仕様変更により位置引数を追加するときに, 呼び出し元も修正する必要がある.
    log2("My numbers are", 1, 2)
    log2("Hi there")
