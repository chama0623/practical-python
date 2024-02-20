if __name__ == "__main__":
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    # シーケンスのスライスは[start:stop:step]のようにストライドが指定できる
    odds = colors[::2]  # 奇数の要素をスライス
    evens = colors[1::2]  # 偶数の要素をスライス
    print(f"{odds=}")
    print(f"{evens=}")

    # ストライドに-1を指定するとバイト列の逆転ができる
    x, w = b"mongoose", "クジラ"
    y, z = x[::-1], w[::-1]
    print(y, z)

    # ストライドとスライドを同時に使うと紛らわしい -> 別々にスライスする
    # 時間, 目盛りに余裕がないときはitertools.isliceを使う
    x = ["a", "b", "c", "d", "e", "f", "g", "h"]
    # 悪い例
    y = x[2:-2:2]
    print(y)

    # 良い例
    y = x[::2]
    z = y[1:-1]
    print(z)
