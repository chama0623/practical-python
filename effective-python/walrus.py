def make_lemonade(count):
    print("made lemonade.")


def make_sider(count):
    print("made apple sider.")


def out_of_stock():
    print("Out of stock!")


if __name__ == "__main__":
    fresh_fruit = {"apple": 10, "banana": 8, "lemon": 5}

    # レモネードを1杯作るのにレモンが1つ必要
    # countはif文の第一ブロックでのみ使用する
    # count = fresh_fruit.get("lemon", 0)を事前に実行する必要がない
    if count := fresh_fruit.get("lemon", 0):
        make_lemonade(count)
        fresh_fruit["lemon"] -= 1
    else:
        out_of_stock()

    # アップルサイダーを1杯作るのにリンゴが4つ必要
    # 代入式を括弧でくくる
    if (count := fresh_fruit.get("apple", 0)) >= 4:
        make_sider(count)
        fresh_fruit["apple"] -= 4
    else:
        out_of_stock()

    print(fresh_fruit)
