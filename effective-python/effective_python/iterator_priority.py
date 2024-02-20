def normalize(numbers: list) -> list[int]:
    """リストの要素を正規化する

    Args:
        numbers (list): 数値のリスト

    Returns:
        list[int]: 正規化した数値のリスト
    """
    total = sum(numbers)
    result = []
    for number in numbers:
        percent = 100 * number / total
        result.append(percent)
    return result


def normalize_defensive(numbers) -> list[int]:
    """正規化する

    Args:
        numbers (Iterator): 正規化する数値のイテレータ

    Raises:
        TypeError: 引数でイテレータが渡されたとき

    Returns:
        list[int]: 正規化した数値のリスト
    """
    # Iterator : __iter__()が実装された反復可能なオブジェクトにアクセスするインターフェース(クラス)
    # Iterator Object : iter()で作成されるイテレータのインスタンス(オブジェクト)
    # iter(Iterator Object)を実行すると, そのIterator Object自身を返す
    if iter(numbers) is numbers:  # iterator objectが渡されたとき
        raise TypeError("Must supply a cpntainer")
    # iteratorが渡されたとき
    total = sum(numbers)
    result = []
    for number in numbers:
        percent = 100 * number / total
        result.append(percent)
    return result


class ReadVisits:
    def __init__(self, data_path: str) -> None:
        self.data_path = data_path

    def __iter__(self):
        """イテレータオブジェクトを返す
        __iter__はイテレータオブジェクトを返す特殊メソッド
        for x in fooという文はiter(foo)を呼び出す.
        iter(foo)はfoo.__iter__をStopIteration例外が発生するまで次々に呼び出す組み込み関数.

        Yields:
            int: 旅行者数
        """
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def read_visits(data_path: str):
    """上手くいかない例. ファイルから旅行者数を取得するジェネレータ

    Args:
        data_path (str): ファイルのパス

    Yields:
        int: 旅行者数
    """
    with open(data_path) as f:
        for line in f:
            yield int(line)


if __name__ == "__main__":
    # 旅行者の人数統計から, 各都市の旅行者の割合を求める
    visits = [15, 35, 80]
    percentages = normalize(visits)
    print(percentages)
    assert sum(percentages) == 100.0

    # すべての都市を含んだファイルからデータを使って分析する
    # StopIteration例外を起こしたイテレータ, ジェネレータはエラーが生じず反復が終了するため, 何も得られない
    it = read_visits("effective_python/dataset/my_numbers.txt")
    percentages = normalize(it)
    print(percentages)  # -> []

    # イテレータプロトコルを実装したコンテナプロトコルによる改善
    visits = ReadVisits("effective_python/dataset/my_numbers.txt")
    percentages = normalize(visits)
    print(percentages)
    assert sum(percentages) == 100.0

    # イテレータの動作確認用
    # for v in visits:
    #     print(v)

    # 正規化処理の改善結果
    visits = [15, 35, 80]
    percentages = normalize_defensive(visits)
    print(percentages)
    assert sum(percentages) == 100.0

    visits = ReadVisits("effective_python/dataset/my_numbers.txt")
    percentages = normalize_defensive(visits)
    print(percentages)
    assert sum(percentages) == 100.0

    # イテレータを渡すとエラーになる
    visits = [15, 35, 80]
    it = iter(visits)
    normalize_defensive(it)
