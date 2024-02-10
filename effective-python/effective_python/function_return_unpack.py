from collections import namedtuple


def get_stats(numbers: list[int]) -> tuple[int, int, float, float, int]:
    """numbersの統計量を返す

    Args:
        numbers (list[int]): 観測データ

    Returns:
        tuple: 統計量のタプル
    """
    minimum = min(numbers)
    maximum = max(numbers)
    # 平均値
    count = len(numbers)
    average = sum(numbers) / count

    # 中央値
    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]

    return minimum, maximum, average, median, count


# namedtupleを使った改善
Stats = namedtuple("Stats", ["minimum", "maximum", "average", "median", "count"])


def get_stats_namedtuple(numbers: list[int]) -> Stats:
    """numbersの統計量を返す. 戻り値はnamedtupleである.

    Args:
        numbers (list[int]): 観測データ

    Returns:
        Stats: 統計量のタプル
    """
    minimum = min(numbers)
    maximum = max(numbers)
    # 平均値
    count = len(numbers)
    average = sum(numbers) / count

    # 中央値
    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]

    return Stats(minimum, maximum, average, median, count)


if __name__ == "__main__":
    # エリア別のワニの生息数
    lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
    # 4つ以上の戻り値があると, 順序を間違えやすい
    # PEP8スタイルガイドの1行の長さを超過し, 読みにくくなることも懸念される
    # -> 改善策 : クラスにする, nametupleを使う
    stats = get_stats_namedtuple(lengths)
    print(f"{stats}")
    print(f"{stats.median=}")
