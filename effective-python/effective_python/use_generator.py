def index_words(text: str) -> list[int]:
    """英語文字列中の単語の位置のインデックスを全て求める.
    ex) index_words("Underway on nuclear power.")
        -> [0, 9, 12, 20]
    Args:
        text (str): 英語文字列

    Returns:
        list[int]: 単語の位置のインデックス
    """
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index + 1)
    return result


def index_words_iter(text: str):
    """単語の位置のインデックスを返すジェネレータ

    Args:
        text (str): 英語文字列

    Yields:
        Iterator[int]: 単語の位置のインデックス
    """
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


if __name__ == "__main__":
    # 英語文字列中の単語の位置のインデックスをすべて求める
    # index_words関数は複雑で読みにくい
    address = "Underway on nuclear power"
    result = index_words(address)
    print(result)

    # ジェネレータによる改良
    # ジェネレータは1要素分しかメモリを占有しないため可変長の入力に用意に対応できる
    result = list(index_words_iter(address))
    print(result)
