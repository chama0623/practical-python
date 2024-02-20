if __name__ == "__main__":
    # タプルの作成
    snack_calories = {"chips": 140, "popcorn": 80, "nuts": 190}
    items = tuple(snack_calories.items())
    print(items)

    # インデックスでタプルの値を取得する
    print(items[0], items[1])

    # 新たな値をインデックス指定で代入できない(イミュータブル)
    # items[0] = ("donut", 250)
    # TypeError: 'tuple' object does not support item assignment

    # アンパック代入
    item = ("Peanut butter", "Jelly")
    a, b = item
    print(f"{a} and {b}")
