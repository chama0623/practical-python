from collections import defaultdict


def log_missing() -> int:
    """stdout missing key log and return default value 0

    Returns:
        int: default value 0
    """
    print("Key added")
    return 0


def increments_with_report(
    current: dict[str, int], increments: list[tuple[str, int]]
) -> tuple[defaultdict[str, int], int]:
    """increments data and count missing key elements

    Args:
        current (dict[str, int]): current dict
        increments (list[tuple[str, int]]): increments dict

    Returns:
        defaultdict[str, int], int: _description_
    """
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count


class CountMissing:
    def __init__(self) -> None:
        self.added = 0

    def __call__(self) -> int:
        """increment missing count

        Returns:
            int: 0
        """
        self.added += 1
        return 0


if __name__ == "__main__":
    # hook : 関数を渡して振る舞いをカスタマイズできる仕組み
    # hookの例 : list.sort()はkeyに関数を受け取り, それに基づいてソートを行う
    names = ["Socrates", "Archimedes", "Plato", "Aristotle"]
    names.sort(key=len)
    print(names)

    # defaultdictのkeyがないときの振る舞いを関数で指定する
    current = {"green": 12, "blue": 3}
    increments = [("red", 5), ("blue", 17), ("orange", 9)]
    result = defaultdict(log_missing, current)
    print("Before:", dict(result))
    for key, amount in increments:
        result[key] += amount
    print("After #1:", dict(result))

    # keyがない要素の数をカウントできるように改善
    result, missing_count = increments_with_report(current, increments)
    print("After #2:", dict(result))
    print("Missing Key Count:", missing_count)

    # increments_with_reportは複雑なのでCountMissingクラスで分かりやすくする
    counter = CountMissing()
    result = defaultdict(counter, current)  # __call__()がhookされる
    for key, amount in increments:
        result[key] += amount
    print("After #3:", dict(result))
    print("Missing Key Count:", counter.added)
