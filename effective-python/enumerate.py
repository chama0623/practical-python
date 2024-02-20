if __name__ == "__main__":
    # アイスクリームのフレーバーをランキング表示する
    flavor_list = ["vanilla", "chocolate", "pecan", "strawberry"]

    # it = enumerate(flavor_list)
    # print(next(it)) -> (0, 'vanilla')
    # print(next(it)) -> (1, 'chocolate')
    # enumerateの第二引数はカウント開始値
    for i, flavor in enumerate(flavor_list, 1):
        print(f"{i}: {flavor}")
