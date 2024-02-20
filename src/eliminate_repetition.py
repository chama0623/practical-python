def get_batches(count: int, size: int) -> int:
    """出荷する最低個数以上の在庫があるか計算する

    Args:
        count (int): 在庫数
        size (int): 出荷する最低個数

    Returns:
        int: 在庫が足りないとき0, それ以外のとき > 0
    """
    return count // size


if __name__ == "__main__":
    stock = {"nails": 125, "screws": 35, "wingnuts": 8, "washers": 24}
    order = ["screws", "wingnuts", "clips"]

    # 注文に応じられる在庫と, その在庫の出荷可能なバッチ数を調べる
    result = {}
    for name in order:
        count = stock.get(name, 0)
        batches = get_batches(count, 8)
        if batches:
            result[name] = batches
    print(result)

    # 内包表記による簡略化
    # get_batches(stock.get(name, 0), 8)の繰り返しで可読性が下がる
    result = {
        name: get_batches(stock.get(name, 0), 8)
        for name in order
        if get_batches(stock.get(name, 0), 8)
    }
    print(result)

    # walrus演算子を使って繰り返しをなくす
    result = {
        name: batches
        for name in order
        if (batches := get_batches(stock.get(name, 0), 8))
    }
    print(result)
    # print(batches) # walrus演算子で定義した変数はループ外にリークする
