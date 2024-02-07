if __name__ == "__main__":
    # シーケンス(list, str, bytes)のスライス
    a = ["a", "b", "c", "d", "e", "f", "g", "h"]
    print(a[3:5])  # d, e
    print(a[1:7])  # b, c, d, e, f, g
    print(a[:5])  # a, b, c, d, e
    print(a[-3:-1])  # f, g
    print(a[:20])  # a, b, c, d, e, f, g, h

    # スライスしたリストは, まったく新しいリストになる
    b = a[3:5]
    b[1] = "x"
    print(a)
    print(b)

    # aの全要素をbにコピーする
    # b=aにすると参照渡しになる
    b = a[:]
    a[0] = "x"
    print(a)
    print(b)
