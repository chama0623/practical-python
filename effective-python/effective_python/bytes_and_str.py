def to_str(bytes_or_str: bytes | str) -> str:
    """decode input strings to str

    Args:
        bytes_or_str (bytes | str): input strings

    Returns:
        str: decoded str instance
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str: bytes | str) -> bytes:
    """encode strings to bytes

    Args:
        bytes_or_str (bytes | str): strings

    Returns:
        bytes: encoded bytes instance
    """
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value


if __name__ == "__main__":
    # bytes instance
    a = b"h\x65llo"  # 符号なし8bit
    print(list(a))
    print(a)

    # str instance
    a = "a\u0300 propos"  # Unicodeコードポイントを含む
    print(list(a))
    print(a)

    # Unicode Sandwich : 処理部ではstr型のみを使う
    # 入力文字列をdecode -> 処理(str) -> encodeした出力文字列
    # decode
    print(repr(to_str(b"foo")))
    print(repr(to_str("bar")))

    # encode
    print(repr(to_bytes(b"foo")))
    print(repr(to_bytes("bar")))
