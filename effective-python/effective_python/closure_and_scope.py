from typing import Any


def sort_priority(values: list[int], group: set[int]) -> None:
    """groupに含まれる数が優先されるソート

    Args:
        values (list[int]): ソート列
        group (set[int]): 優先列
    """

    def helper(x: int) -> tuple[int, int]:
        """xの優先度を返す

        Args:
            x (int): 優先度を調べる整数

        Returns:
            tuple[int, int]: (優先度, 整数)のタプル. 優先度が0のとき優先順位が高く, 1のとき優先順位が低い.
        """
        if x in group:
            return (0, x)
        return (1, x)

    # sort内部では, indexが0番目の要素から順に比較される
    values.sort(key=helper)


def sort_priority2(values: list[int], group: set[int]) -> bool:
    """groupに含まれる数が優先されるソート. さらに優先度が高い数が含まれるかを返す.

    Args:
        values (list[int]): ソート列
        group (set[int]): 優先列

    Returns:
        bool: 優先度が高い数が含まれるときTrue
    """
    # スコープはsort_priority2
    found = False

    def helper(x: int) -> tuple[int, int]:
        """xの優先度を返す

        Args:
            x (int): 優先度を調べる整数

        Returns:
            tuple[int, int]: (優先度, 整数)のタプル. 優先度が0のとき優先順位が高く, 1のとき優先順位が低い.
        """
        # nonlocal文がないとfound = Trueのスコープはhelperになる
        # nonlocal文によりスコープの横断を示す
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    values.sort(key=helper)
    return found


class Sorter:
    def __init__(self, group: set[int]) -> None:
        """コンストラクタ

        Args:
            group (set[int]): 優先列
        """
        self.group = group
        self.found = False

    def __call__(self, x: int) -> tuple[int, int]:
        """xの優先度を返す

        Args:
            x (int): 優先度を調べる整数

        Returns:
            tuple[int, int]: (優先度, 整数)のタプル. 優先度が0のとき優先順位が高く, 1のとき優先順位が低い.
        """
        if x in self.group:
            self.found = True
            return (0, x)
        else:
            return (1, x)


if __name__ == "__main__":
    # 優先度付きのソート
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    sort_priority(numbers, group)
    print(numbers)

    # 優先度の高い数があるかを返す優先度付きソート
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    found = sort_priority2(numbers, group)
    print(numbers)
    print(f"is priority number: {found}")

    # nonlocalを使わない例
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    sorter = Sorter(group)
    numbers.sort(key=sorter)
    print(numbers)
    print(f"is priority number: {sorter.found}")
